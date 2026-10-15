# Evidencia Técnica y Auditoría de Integridad — Issue #87 (Revisión PR #1)
## Piensa pe Chato: Landing Pública Base en GitHub Pages para Liga Amateur

- **Proyecto:** `Piensa pe Chato`
- **Issue Central:** `soytensa/tensa-dev-workflow#87`
- **Repositorio Independiente:** `soytensa/piensa-pe-chato`
- **Rama:** `feat/landing-mvp-87`
- **Fecha:** 15 de octubre de 2026
- **Entorno Local:** `C:\Users\wesly\.gemini\antigravity\scratch\piensa-pe-chato`
- **Estado de Entrega:** `PENDING_REVIEW_BEFORE_PUBLISH` (Correcciones P0 y P1 aplicadas en la misma rama; repositorio privado y GitHub Pages sin activar a la espera de autorización).

---

### 1. Resumen de Correcciones Aplicadas (Revisión PR #1)

| Aspecto | Corrección Aplicada | Archivos Modificados |
|---|---|---|
| **P0: Región de Servidor y Ámbito** | Eliminadas referencias no confirmadas a «Perú», «Sudamérica» o «servidores fijos». Sustituido por «comunidad hispanohablante e internacional» y «servidores coordinados según partida (España / Europa / internacional)». | `index.html`, `README.md`, `tests/test_landing.py` |
| **P0: Tratamiento Factual de Acuerdos / Apuestas** | Eliminadas afirmaciones falsas absolutas («100% Gratis / No Apuestas», «prohibición terminante en la comunidad»). El alcance no transaccional se circunscribe estrictamente a la **web estática en GitHub Pages** (sin pasarelas, cobro de entradas ni software de apuestas). Se declara con transparencia que los acuerdos privados entre jugadores discurren fuera de la web y que el organizador informará fielmente del contexto a Valve en la solicitud. | `index.html`, `README.md`, `tests/test_landing.py` |
| **P0: Estado de Acreditación ante Valve** | Sustituidos rótulos de «Compliance Oficial» o «Aprobación» por «Formato y Solicitud de Liga Amateur». Se incorpora aviso destacado de **Estado en trámite de presentación** indicando que el ticket y la elegibilidad están sujetos a resolución de Valve, y calificando las partidas actuales como «lobbies inhouse preparatorios». | `index.html`, `styles.css`, `README.md`, `tests/test_landing.py` |
| **P1: Balance y Herramientas** | Clarificado que las herramientas de balance asistido y MMR interno están en fase de diseño/estudio (no operativas en el MVP actual). | `index.html`, `README.md` |
| **P1: Suite de Pruebas Unitarias** | Ampliada la suite a 8 pruebas automatizadas (`tests/test_landing.py`), incluyendo comprobaciones de ausencia de afirmaciones categóricas falsas, accesibilidad semántica/ARIA y respuestas HTTP 200. | `tests/test_landing.py` |
| **P1: Evidencia Visual de Navegador** | Verificación real en navegador headless (Microsoft Edge) generando capturas a resolución de escritorio (1280x800) y móvil (375x812). | `evidence/issue-87/render_desktop_1280x800.png`, `evidence/issue-87/render_mobile_375x812.png` |

---

### 2. Resultados de Validación de la Suite de Pruebas

Ejecución de `tests/test_landing.py` (8/8 pruebas superadas, 100% OK):
```text
test_01_required_files_exist (tests.test_landing.TestPiensaPeChatoLanding.test_01_required_files_exist)
Verifica que todos los archivos requeridos del MVP existen y no están vacíos. ... ok
test_02_html_structure_and_relative_paths (tests.test_landing.TestPiensaPeChatoLanding.test_02_html_structure_and_relative_paths)
Verifica que index.html contenga rutas relativas y metadatos SEO / OpenGraph. ... ok
test_03_inhouse_series_and_valve_application_status (tests.test_landing.TestPiensaPeChatoLanding.test_03_inhouse_series_and_valve_application_status)
Verifica el formato Inhouse Series, independencia del torneo de diciembre y estado en trámite Valve. ... ok
test_04_discord_link_integrity (tests.test_landing.TestPiensaPeChatoLanding.test_04_discord_link_integrity)
Verifica que el enlace oficial de Discord https://discord.gg/Ac2WWFJGfQ esté presente y configurado. ... ok
test_05_no_unverified_categorical_claims (tests.test_landing.TestPiensaPeChatoLanding.test_05_no_unverified_categorical_claims)
Verifica la ausencia de afirmaciones categóricas falsas (región fija o negación de acuerdos entre jugadores). ... ok
test_06_proximamente_modules (tests.test_landing.TestPiensaPeChatoLanding.test_06_proximamente_modules)
Verifica que las funciones futuras estén honestamente marcadas como Próximamente. ... ok
test_07_accessibility_and_responsive_css (tests.test_landing.TestPiensaPeChatoLanding.test_07_accessibility_and_responsive_css)
Verifica etiquetas semánticas, accesibilidad ARIA y consultas de medios responsive en CSS. ... ok
test_08_local_http_server_response (tests.test_landing.TestPiensaPeChatoLanding.test_08_local_http_server_response)
Inicia un servidor HTTP local y verifica respuestas HTTP 200 de todos los recursos estáticos. ... 
127.0.0.1 - - [15/Oct/2026 15:06:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [15/Oct/2026 15:06:17] "GET /index.html HTTP/1.1" 200 -
127.0.0.1 - - [15/Oct/2026 15:06:17] "GET /styles.css HTTP/1.1" 200 -
127.0.0.1 - - [15/Oct/2026 15:06:17] "GET /app.js HTTP/1.1" 200 -
127.0.0.1 - - [15/Oct/2026 15:06:17] "GET /favicon.svg HTTP/1.1" 200 -
ok

----------------------------------------------------------------------
Ran 8 tests in 0.580s

OK
```

---

### 3. Comprobación de Renderizado Visual en Navegador

Se ejecutó un servidor HTTP local en puerto 8789 y se invocó el motor de Chromium/Edge en modo headless para capturar el renderizado visual exacto:
- **Vista Escritorio (1280x800):** Guardada en `evidence/issue-87/render_desktop_1280x800.png`. Barra de navegación expandida, banner hero centrado, panel de estadísticas con 4 columnas y aviso de estado de trámite.
- **Vista Móvil (375x812):** Guardada en `evidence/issue-87/render_mobile_375x812.png`. Botón hamburguesa accesible (`aria-expanded`), tarjetas apiladas fluidamente en una sola columna y textos ajustados sin desbordamiento horizontal.

---

### 4. Estado de Publicación y Criterios de Seguridad

- **Repositorio:** `soytensa/piensa-pe-chato` (Privado).
- **GitHub Pages:** NO activado ni publicado.
- **Pull Request #1:** https://github.com/soytensa/piensa-pe-chato/pull/1 actualizado con las correcciones.
- **Merge a main:** NO realizado (esperando revisión y aprobación explícita).
