#!/usr/bin/env python3
"""
Test Suite de Integración y Validación para Chato League — Season Zero (Issue #92)
Valida archivos, rutas relativas, identidad de marca, Season Zero, Valve compliance,
aclaración comunitaria de Chupetines EU, enlaces de Discord y HTTP local.
"""

import http.server
import os
import socketserver
import threading
import time
import unittest
import urllib.request

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestChatoLeagueLanding(unittest.TestCase):

    def test_01_required_files_exist(self):
        """Verifica que todos los archivos requeridos existen y no están vacíos."""
        required_files = [
            "index.html",
            "styles.css",
            "app.js",
            "favicon.svg",
            "README.md",
            "LICENSE",
            ".gitignore",
        ]
        for fname in required_files:
            fpath = os.path.join(ROOT_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"Falta el archivo requerido: {fname}")
            self.assertGreater(os.path.getsize(fpath), 0, f"El archivo está vacío: {fname}")

    def test_02_html_structure_and_canonical_url(self):
        """Verifica que index.html contenga rutas relativas, canónica de chato-league y metadatos SEO / OG."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # HTML5 doctype y estructura
        self.assertIn("<!DOCTYPE html>", content)
        self.assertIn('<meta name="viewport"', content)
        self.assertIn('<meta property="og:title"', content)
        self.assertIn('<meta property="og:url"', content)

        # URL Canónica nueva
        self.assertIn('https://soytensa.github.io/chato-league/', content)

        # Rutas relativas seguras para GitHub Pages
        self.assertIn('href="./styles.css"', content)
        self.assertIn('src="./app.js"', content)
        self.assertIn('href="./favicon.svg"', content)

        # No debe contener rutas absolutas a localhost o rutas rotas de primer nivel
        self.assertNotIn('href="/styles.css"', content)
        self.assertNotIn('src="/app.js"', content)

    def test_03_chato_league_identity_and_season_zero(self):
        """Verifica la marca CHATO LEAGUE, SEASON ZERO, fechas y denominación de Valve."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Marca y edición
        self.assertIn("CHATO LEAGUE", content)
        self.assertIn("SEASON ZERO", content)
        self.assertIn("Chato League - Season Zero", content)

        # Fechas del piloto
        self.assertIn("noviembre de 2026", content.lower())

        # Pilares del formato
        self.assertIn("Captains Mode", content)
        self.assertIn("5v5", content)
        self.assertIn("Plantillas Dinámicas", content)

        # Relación comunitaria con Piensa pe Chato
        self.assertIn("Piensa pe Chato", content)

        # Independencia del Torneo de Diciembre y aclaración de Chupetines EU
        self.assertIn("Torneo de Diciembre", content)
        self.assertIn("Chupetines EU", content)
        content_lower = content.lower()
        self.assertIn("externa e independiente", content_lower)

        # Sección Valve: debe reflejar estado en preparación / pendiente de envío y evaluación por Valve
        self.assertIn("valve-compliance", content)
        self.assertIn("valve-lang-es", content)
        self.assertIn("valve-lang-en", content)
        self.assertIn("Solicitud en preparación", content)
        self.assertIn("Pending submission and evaluation by Valve", content)
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
        """Verifica la ausencia de afirmaciones categóricas falsas."""
        html_path = os.path.join(ROOT_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # No debe afirmar una región geográfica exclusiva no confirmada
        self.assertNotIn("Perú", content)
        self.assertNotIn("Sudamérica", content)

        # No debe afirmar procedimientos no comprobados como actas en Discord
        self.assertNotIn("actas en discord", content.lower())

        # No debe atribuir organización o representación oficial a Chupetines EU
        content_lower = content.lower()
        self.assertNotIn("organizado por chupetines eu", content_lower)

        # La limitación financiera debe atribuirse certeramente a la web
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
        self.assertIn(".nav-links a.mobile-discord-cta", css)
        self.assertIn("#0f141c", css)

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
