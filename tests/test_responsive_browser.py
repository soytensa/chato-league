#!/usr/bin/env python3
"""
Test Automatizado de Renderizado Responsive con Headless Edge y CDP (Chrome DevTools Protocol)
Verifica programáticamente que no haya desbordamiento horizontal en 320px, 375px, 390px, 768px y 1280px.
Toma capturas PNG reales en cada breakpoint y las guarda en evidence/issue-87/.
"""

import asyncio
import http.server
import json
import os
import socketserver
import subprocess
import threading
import time
import urllib.request
import websockets

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_DIR = os.path.join(ROOT_DIR, "evidence", "issue-87")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

TARGET_VIEWPORTS = [
    {"name": "mobile_320", "width": 320, "height": 640},
    {"name": "mobile_375", "width": 375, "height": 812},
    {"name": "mobile_390", "width": 390, "height": 844},
    {"name": "tablet_768", "width": 768, "height": 1024},
    {"name": "desktop_1280", "width": 1280, "height": 800},
]

class QuietServer(socketserver.TCPServer):
    allow_reuse_address = True

async def run_cdp_audit():
    # 1. Iniciar servidor HTTP local
    port = 8792
    os.chdir(ROOT_DIR)
    httpd = QuietServer(("127.0.0.1", port), http.server.SimpleHTTPRequestHandler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    time.sleep(0.5)

    cdp_port = 9333
    os.makedirs(EVIDENCE_DIR, exist_ok=True)

    # 2. Iniciar Edge con remote debugging
    edge_cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        f"--remote-debugging-port={cdp_port}",
        "--remote-allow-origins=*",
        "--hide-scrollbars",
        f"http://127.0.0.1:{port}/index.html"
    ]
    proc = subprocess.Popen(edge_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(1.5)

    results = []

    try:
        # Obtener lista de páginas desde CDP
        req = urllib.request.Request(f"http://127.0.0.1:{cdp_port}/json")
        with urllib.request.urlopen(req, timeout=5) as resp:
            targets = json.loads(resp.read().decode())
        
        ws_url = None
        for t in targets:
            if "webSocketDebuggerUrl" in t and "index.html" in t.get("url", ""):
                ws_url = t["webSocketDebuggerUrl"]
                break
        if not ws_url and targets:
            ws_url = targets[0]["webSocketDebuggerUrl"]

        print(f"Conectado a CDP WebSocket: {ws_url}")

        async with websockets.connect(ws_url, max_size=20*1024*1024) as ws:
            msg_id = 1

            async def send_cmd(method, params=None):
                nonlocal msg_id
                cid = msg_id
                msg_id += 1
                payload = {"id": cid, "method": method}
                if params:
                    payload["params"] = params
                await ws.send(json.dumps(payload))
                while True:
                    raw = await ws.recv()
                    data = json.loads(raw)
                    if data.get("id") == cid:
                        return data.get("result", {})

            await send_cmd("Page.enable")
            await send_cmd("DOM.enable")
            await send_cmd("Runtime.enable")

            for vp in TARGET_VIEWPORTS:
                w = vp["width"]
                h = vp["height"]
                vname = vp["name"]
                print(f"\n--- Probando Viewport: {vname} ({w}x{h}) ---")

                # Emular tamaño de pantalla
                await send_cmd("Emulation.setDeviceMetricsOverride", {
                    "width": w,
                    "height": h,
                    "deviceScaleFactor": 1,
                    "mobile": (w < 800)
                })
                await asyncio.sleep(0.3)

                # Evaluar dimensiones reales del DOM
                eval_js = """
                (() => {
                    const docEl = document.documentElement;
                    const scrollWidth = docEl.scrollWidth;
                    const innerWidth = window.innerWidth;
                    const hasOverflow = scrollWidth > innerWidth;

                    const allElements = Array.from(document.querySelectorAll('*'));
                    const overflowing = [];
                    for (const el of allElements) {
                        const rect = el.getBoundingClientRect();
                        if (rect.right > innerWidth + 0.5) {
                            overflowing.push({
                                tag: el.tagName,
                                id: el.id,
                                class: el.className,
                                right: Math.round(rect.right),
                                width: Math.round(rect.width)
                            });
                        }
                    }

                    return {
                        scrollWidth: scrollWidth,
                        innerWidth: innerWidth,
                        hasOverflow: hasOverflow,
                        overflowCount: overflowing.length,
                        overflowSamples: overflowing.slice(0, 5)
                    };
                })()
                """
                res = await send_cmd("Runtime.evaluate", {
                    "expression": eval_js,
                    "returnByValue": True
                })
                dom_result = res.get("result", {}).get("value", {})
                print(f"DOM Metrics: scrollWidth={dom_result.get('scrollWidth')}px, innerWidth={dom_result.get('innerWidth')}px, hasOverflow={dom_result.get('hasOverflow')}")
                if dom_result.get("overflowCount", 0) > 0:
                    print(f"ALERTA: {dom_result['overflowCount']} elementos desbordan! Muestras: {dom_result['overflowSamples']}")

                # Captura de pantalla PNG
                shot = await send_cmd("Page.captureScreenshot", {"format": "png"})
                import base64
                img_data = base64.b64decode(shot["data"])
                screenshot_filename = f"render_{vname}_{w}x{h}.png"
                screenshot_path = os.path.join(EVIDENCE_DIR, screenshot_filename)
                with open(screenshot_path, "wb") as f_img:
                    f_img.write(img_data)
                print(f"Captura guardada: {screenshot_path} ({len(img_data)} bytes)")

                # Probar interactividad móvil si corresponde (botón hamburguesa y pestañas Valve)
                if w <= 868:
                    # Clic en botón hamburguesa
                    click_menu_js = """
                    (() => {
                        const btn = document.getElementById('mobile-menu-btn');
                        if (btn) btn.click();
                        const nav = document.getElementById('nav-links');
                        return {
                            isOpen: nav ? nav.classList.contains('open') : false,
                            ariaExpanded: btn ? btn.getAttribute('aria-expanded') : null
                        };
                    })()
                    """
                    menu_res = await send_cmd("Runtime.evaluate", {"expression": click_menu_js, "returnByValue": True})
                    menu_data = menu_res.get("result", {}).get("value", {})
                    print(f"Menú Móvil interactividad: {menu_data}")

                # Probar cambio de pestaña Valve (EN)
                click_tab_js = """
                (() => {
                    const enBtn = document.querySelector('.tab-btn[data-tab="en"]');
                    if (enBtn) enBtn.click();
                    const enContent = document.getElementById('valve-lang-en');
                    return {
                        tabActive: enBtn ? enBtn.classList.contains('active') : false,
                        contentActive: enContent ? enContent.classList.contains('active') : false
                    };
                })()
                """
                tab_res = await send_cmd("Runtime.evaluate", {"expression": click_tab_js, "returnByValue": True})
                tab_data = tab_res.get("result", {}).get("value", {})
                print(f"Pestañas Valve interactividad: {tab_data}")

                results.append({
                    "viewport": vname,
                    "width": w,
                    "height": h,
                    "scrollWidth": dom_result.get("scrollWidth"),
                    "innerWidth": dom_result.get("innerWidth"),
                    "hasOverflow": dom_result.get("hasOverflow"),
                    "overflowCount": dom_result.get("overflowCount", 0),
                    "screenshot": screenshot_filename
                })

    finally:
        proc.kill()
        httpd.shutdown()
        httpd.server_close()

    print("\n================== RESUMEN DE AUDITORIA RESPONSIVE ==================")
    all_passed = True
    for r in results:
        status = "PASS" if not r["hasOverflow"] and r["overflowCount"] == 0 else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"[{status}] {r['viewport']} ({r['width']}px): scrollWidth={r['scrollWidth']}px <= innerWidth={r['innerWidth']}px | Overflows={r['overflowCount']}")
    print("=====================================================================")
    if not all_passed:
        raise AssertionError("Fallo en auditoría responsive: se detectaron desbordamientos horizontales.")
    else:
        print("TODOS LOS BREAKPOINTS RESPONSIVE SUPERADOS SIN DESBORDAMIENTOS (0 OVERFLOWS).")

if __name__ == "__main__":
    asyncio.run(run_cdp_audit())
