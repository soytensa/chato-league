#!/usr/bin/env python3
"""
Test Suite de Integración y Validación para Piensa pe Chato — Landing MVP (Issue #87)
Actualizada según revisión de PR #1: valida archivos, rutas relativas, ausencia de afirmaciones
categóricas falsas (región fija/cero apuestas comunitarias), estado pendiente Valve y HTTP local.
"""

import http.server
import os
import socketserver
import threading
import time
import unittest
import urllib.request

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestPiensaPeChatoLanding(unittest.TestCase):

    def test_01_required_files_exist(self):
        """Verifica que todos los archivos requeridos del MVP existen y no están vacíos."""
        required_files = [
            "index.html",
            "styles.css",
            "app.js",
            "favicon.svg",
            "README.md",
            "LICENSE",
            ".gitignore"
        ]
        for fname in required_files:
            fpath = os.path.join(ROOT_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"Falta el archivo requerido: {fname}")
            self.assertGreater(os.path.getsize(fpath), 0, f"El archivo está vacío: {fname}")

    def test_02_html_structure_and_relative_paths(self):
        """Verifica que index.html contenga rutas relativas y metadatos SEO / OpenGraph."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # HTML5 doctype y estructura
        self.assertIn("<!DOCTYPE html>", content)
        self.assertIn("<meta name=\"viewport\"", content)
        self.assertIn("<meta property=\"og:title\"", content)
        self.assertIn("<meta property=\"og:url\"", content)

        # Rutas relativas seguras para GitHub Pages
        self.assertIn('href="./styles.css"', content)
        self.assertIn('src="./app.js"', content)
        self.assertIn('href="./favicon.svg"', content)

        # No debe contener rutas absolutas a localhost o rutas rotas de primer nivel
        self.assertNotIn('href="/styles.css"', content)
        self.assertNotIn('src="/app.js"', content)

    def test_03_inhouse_series_and_valve_application_status(self):
        """Verifica el formato Inhouse Series, independencia del torneo de diciembre y estado en trámite Valve."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Marca y título
        self.assertIn("Piensa pe Chato", content)
        self.assertIn("Inhouse Series 2026", content)

        # Pilares del formato inhouse
        self.assertIn("Captains Mode", content)
        self.assertIn("5v5", content)
        self.assertIn("Plantillas Dinámicas", content)
        self.assertIn("Torneo de Diciembre", content)  # Independencia operativa documentada

        # Sección Valve: debe reflejar estado en trámite / pendiente de aprobación
        self.assertIn("valve-compliance", content)
        self.assertIn("valve-lang-es", content)
        self.assertIn("valve-lang-en", content)
        self.assertIn("En trámite de presentación", content)
        self.assertIn("pending review", content.lower())
        self.assertIn("072E-47E8-B513-6E4E", content)  # Enlace FAQ Valve

    def test_04_discord_link_integrity(self):
        """Verifica que el enlace oficial de Discord https://discord.gg/Ac2WWFJGfQ esté presente y configurado."""
        official_discord = "https://discord.gg/Ac2WWFJGfQ"

        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        self.assertIn(official_discord, html_content)

        js_path = os.path.join(ROOT_DIR, "app.js")
        with open(js_path, "r", encoding="utf-8") as f:
            js_content = f.read()
        self.assertIn(official_discord, js_content)

    def test_05_no_unverified_categorical_claims(self):
        """Verifica la ausencia de afirmaciones categóricas falsas (región fija o negación de acuerdos entre jugadores)."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # No debe afirmar una región geográfica exclusiva no confirmada
        self.assertNotIn("Perú", content)
        self.assertNotIn("Sudamérica", content)

        # No debe hacer declaraciones falsas absolutas sobre ausencia de dinero/apuestas en la comunidad
        content_lower = content.lower()
        self.assertNotIn("cero cuotas / no apuestas", content_lower)
        self.assertNotIn("prohibición terminante", content_lower)
        self.assertNotIn("zero real-money gambling", content_lower)

        # La limitación debe atribuirse certeramente a la web y su hosting
        self.assertIn("web estática", content_lower)
        self.assertIn("sin pasarelas", content_lower)

    def test_06_proximamente_modules(self):
        """Verifica que las funciones futuras estén honestamente marcadas como Próximamente."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("Próximamente", content)
        self.assertIn("Historial de Partidas", content)
        self.assertIn("Estadísticas Comunitarias", content)
        self.assertIn("Pabellón de Héroes", content)

    def test_07_accessibility_and_responsive_css(self):
        """Verifica etiquetas semánticas, accesibilidad ARIA y consultas de medios responsive en CSS."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()

        self.assertIn("<header", html)
        self.assertIn("<nav", html)
        self.assertIn("<main", html)
        self.assertIn("<section", html)
        self.assertIn("<footer", html)
        self.assertIn('role="tablist"', html)
        self.assertIn('role="tab"', html)
        self.assertIn('aria-selected', html)

        css_path = os.path.join(ROOT_DIR, "styles.css")
        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()

        self.assertIn("@media (max-width: 868px)", css)
        self.assertIn(":focus-visible", css)
        self.assertIn("color-scheme: dark", css)

    def test_08_local_http_server_response(self):
        """Inicia un servidor HTTP local y verifica respuestas HTTP 200 de todos los recursos estáticos."""
        port = 8788
        handler = http.server.SimpleHTTPRequestHandler
        class QuietServer(socketserver.TCPServer):
            allow_reuse_address = True

        os.chdir(ROOT_DIR)
        httpd = QuietServer(("127.0.0.1", port), handler)
        server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        server_thread.start()
        time.sleep(0.5)

        try:
            endpoints = [
                ("/", 200, "text/html"),
                ("/index.html", 200, "text/html"),
                ("/styles.css", 200, "text/css"),
                ("/app.js", 200, "javascript"),
                ("/favicon.svg", 200, "image/svg+xml"),
            ]
            for path, expected_code, expected_type_substr in endpoints:
                url = f"http://127.0.0.1:{port}{path}"
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req, timeout=5) as resp:
                    self.assertEqual(resp.status, expected_code, f"Fallo al cargar {url}")
                    content_type = resp.headers.get("Content-Type", "")
                    self.assertIn(expected_type_substr, content_type.lower())
        finally:
            httpd.shutdown()
            httpd.server_close()


if __name__ == "__main__":
    unittest.main()
