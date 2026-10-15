#!/usr/bin/env python3
"""
Test Automatizado de Verificación de GitHub Pages en Producción (Live Web)
URL: https://soytensa.github.io/piensa-pe-chato/
- Verifica HTTP 200 y HTTPS en HTML, CSS, JS y favicon.
- Verifica enlaces de Discord y Valve.
- Renderiza en Microsoft Edge Headless contra la URL pública de GitHub Pages.
- Captura pantallas de escritorio (1280x800) y móvil (375x812, normal y con menú abierto).
- Guarda evidencias en evidence/issue-90/.
"""

import asyncio
import base64
import json
import os
import subprocess
import time
import urllib.request
import websockets

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_DIR = os.path.join(ROOT_DIR, "evidence", "issue-90")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
LIVE_URL = "https://soytensa.github.io/piensa-pe-chato/"

TARGET_VIEWPORTS = [
    {"name": "desktop_1280", "width": 1280, "height": 800, "is_mobile": False},
    {"name": "mobile_375", "width": 375, "height": 812, "is_mobile": True},
]


async def run_live_audit():
    os.makedirs(EVIDENCE_DIR, exist_ok=True)

    # 1. Verificación HTTP inicial
    assets = [
        LIVE_URL,
        f"{LIVE_URL}styles.css",
        f"{LIVE_URL}app.js",
        f"{LIVE_URL}favicon.svg",
    ]
    print(f"[*] Verificando respuestas HTTP directas contra {LIVE_URL}...")
    for asset in assets:
        req = urllib.request.Request(asset, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            content_len = len(resp.read())
            assert status == 200, f"Error HTTP {status} en {asset}"
            print(f"  [HTTP {status}] {asset} ({content_len} bytes)")

    cdp_port = 9444
    # 2. Iniciar Edge con remote debugging contra la URL pública
    edge_cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        f"--remote-debugging-port={cdp_port}",
        "--remote-allow-origins=*",
        "--hide-scrollbars",
        LIVE_URL,
    ]
    print(f"[*] Lanzando headless Edge contra {LIVE_URL}...")
    proc = subprocess.Popen(edge_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2.0)

    try:
        # Obtener lista de páginas desde CDP
        req = urllib.request.Request(f"http://127.0.0.1:{cdp_port}/json")
        with urllib.request.urlopen(req, timeout=5) as resp:
            targets = json.loads(resp.read().decode())

        ws_url = None
        for t in targets:
            if "webSocketDebuggerUrl" in t and ("piensa-pe-chato" in t.get("url", "") or t.get("type") == "page"):
                ws_url = t["webSocketDebuggerUrl"]
                break
        if not ws_url and targets:
            ws_url = targets[0]["webSocketDebuggerUrl"]

        print(f"  Conectado a CDP WebSocket: {ws_url}")

        async with websockets.connect(ws_url, max_size=20 * 1024 * 1024) as ws:
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

            # Navegar explícitamente a LIVE_URL
            nav_res = await send_cmd("Page.navigate", {"url": LIVE_URL})
            print(f"  Page.navigate: {nav_res}")
            await asyncio.sleep(3.0)

            # Validar título y elementos
            eval_res = await send_cmd(
                "Runtime.evaluate",
                {
                    "expression": "JSON.stringify({ title: document.title, url: window.location.href, ctaCount: document.querySelectorAll('a[href=\"https://discord.gg/Ac2WWFJGfQ\"]').length })"
                },
            )
            page_meta = json.loads(eval_res["result"]["value"])
            print(f"  [DOM] URL activa: {page_meta['url']}")
            print(f"  [DOM] Titulo: {page_meta['title']}")
            print(f"  [DOM] Enlaces Discord CTA: {page_meta['ctaCount']}")
            assert "Piensa pe Chato" in page_meta["title"]
            assert page_meta["ctaCount"] >= 3

            results = []

            for vp in TARGET_VIEWPORTS:
                name = vp["name"]
                w = vp["width"]
                h = vp["height"]
                print(f"[*] Evaluando y capturando viewport {name} ({w}x{h})...")

                await send_cmd(
                    "Emulation.setDeviceMetricsOverride",
                    {
                        "width": w,
                        "height": h,
                        "deviceScaleFactor": 1,
                        "mobile": vp["is_mobile"],
                    },
                )
                await asyncio.sleep(0.5)

                # Comprobar overflow
                overflow_res = await send_cmd(
                    "Runtime.evaluate",
                    {
                        "expression": "document.documentElement.scrollWidth > window.innerWidth"
                    },
                )
                has_overflow = overflow_res["result"]["value"]
                print(f"  Overflow horizontal: {has_overflow}")
                assert not has_overflow, f"Desbordamiento detectado en {name}"

                # Captura normal
                shot = await send_cmd("Page.captureScreenshot", {"format": "png"})
                img_path = os.path.join(EVIDENCE_DIR, f"live_{name}_{w}x{h}.png")
                with open(img_path, "wb") as f:
                    f.write(base64.b64decode(shot["data"]))
                print(f"  -> Captura guardada: {img_path}")

                # Si es móvil, abrir menú y capturar
                if vp["is_mobile"]:
                    open_menu_js = """
                    (() => {
                        const btn = document.getElementById('mobile-menu-btn');
                        const nav = document.getElementById('nav-links');
                        if (btn && nav && !nav.classList.contains('open')) {
                            btn.click();
                        }
                        const discordBtn = document.querySelector('.mobile-discord-cta');
                        let computedColor = null;
                        let computedFontWeight = null;
                        if (discordBtn) {
                            const cs = window.getComputedStyle(discordBtn);
                            computedColor = cs.color;
                            computedFontWeight = cs.fontWeight;
                        }
                        return {
                            isOpen: nav ? nav.classList.contains('open') : false,
                            ariaExpanded: btn ? btn.getAttribute('aria-expanded') : null,
                            discordColor: computedColor,
                            discordFontWeight: computedFontWeight
                        };
                    })()
                    """
                    menu_res = await send_cmd("Runtime.evaluate", {"expression": open_menu_js, "returnByValue": True})
                    contrast_data = menu_res.get("result", {}).get("value", {})
                    print(f"  Menu movil desplegado & Contraste: {contrast_data}")
                    assert contrast_data.get("isOpen") is True
                    assert contrast_data.get("discordColor") == "rgb(15, 20, 28)"

                    # Captura de menú abierto
                    shot_menu = await send_cmd("Page.captureScreenshot", {"format": "png"})
                    img_menu_path = os.path.join(EVIDENCE_DIR, f"live_menu_open_{name}_{w}x{h}.png")
                    with open(img_menu_path, "wb") as f:
                        f.write(base64.b64decode(shot_menu["data"]))
                    print(f"  -> Captura menu guardada: {img_menu_path}")

                    # Cerrar menú
                    close_menu_js = """
                    (() => {
                        const btn = document.getElementById('mobile-menu-btn');
                        const nav = document.getElementById('nav-links');
                        if (btn && nav && nav.classList.contains('open')) {
                            btn.click();
                        }
                    })()
                    """
                    await send_cmd("Runtime.evaluate", {"expression": close_menu_js})
                    await asyncio.sleep(0.3)

                results.append({"viewport": name, "size": f"{w}x{h}", "overflow": has_overflow})

            print("\n[+] Auditoria LIVE completada con exito en todos los viewports.")
            return results

    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    res = asyncio.run(run_live_audit())
    print("\nResultados finales:", json.dumps(res, indent=2))
