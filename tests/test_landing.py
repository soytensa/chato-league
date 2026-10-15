#!/usr/bin/env python3
"""
Test Suite de Integración y Validación para Piensa pe Chato — Landing MVP (Issue #87)
Verifica integridad de archivos, sintaxis, rutas relativas, compliance y respuesta HTTP local.
"""

import http.server
import os
import re
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

        # No debe contener rutas absolutas a localhost o rutas rotas
        self.assertNotIn('href="/styles.css"', content)
        self.assertNotIn('src="/app.js"', content)

    def test_03_inhouse_series_and_valve_requirements(self):
        """Verifica que el contenido refleje fielmente el formato Inhouse Series y la información para Valve."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Marca y título
        self.assertIn("Piensa pe Chato", content)
        self.assertIn("Inhouse Series 2026", content)

        # Pilares del formato
        self.assertIn("Captains Mode", content)
        self.assertIn("5v5", content)
        self.assertIn("Plantillas", content)
        self.assertIn("Torneo de Diciembre", content)  # Debe clarificar la independencia

        # Sección Valve bilingüe
        self.assertIn("valve-compliance", content)
        self.assertIn("valve-lang-es", content)
        self.assertIn("valve-lang-en", content)
        self.assertIn("Non-Commercial Nature", content)
        self.assertIn("072E-47E8-B513-6E4E", content)  # Enlace FAQ Valve

    def test_04_discord_link_integrity(self):
        """Verifica que el enlace oficial de Discord https://discord.gg/Ac2WWFJGfQ esté presente y configurado."""
        official_discord = "https://discord.gg/Ac2WWFJGfQ"

        # En index.html
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        self.assertIn(official_discord, html_content)

        # En app.js
        js_path = os.path.join(ROOT_DIR, "app.js")
        with open(js_path, "r", encoding="utf-8") as f:
            js_content = f.read()
        self.assertIn(official_discord, js_content)

    def test_05_proximamente_and_anti_gambling_compliance(self):
        """Verifica que las funciones futuras estén marcadas como Próximamente y no haya apuestas ni pasarelas."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Marcadores transparentes
        self.assertIn("Próximamente", content)
        self.assertIn("Historial de Partidas", content)
        self.assertIn("Estadísticas y Rankings", content)
        self.assertIn("Pabellón de Héroes", content)

        # Reglas de uso aceptable: no apuestas ni transacciones
        forbidden_commercial_terms = [
            "apostar dinero",
            "casino",
            "cuota de pago",
            "paypal checkout",
            "stripe checkout",
            "apuestas deportivas"
        ]
        for term in forbidden_commercial_terms:
            self.assertNotIn(term, content.lower())

    def test_06_local_http_server_response(self):
        """Inicia un servidor HTTP local y verifica respuestas HTTP 200 de todos los recursos."""
        port = 8787
        handler = http.server.SimpleHTTPRequestHandler
        # Usar un servidor multihilo o simple en daemon
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
