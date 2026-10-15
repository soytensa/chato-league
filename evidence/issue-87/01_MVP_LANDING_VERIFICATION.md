# Evidencia Técnica y Auditoría de Integridad — Issue #87 (Revisión #3 — Contraste Visual y Responsive)
## Piensa pe Chato: Landing Pública Base en GitHub Pages para Liga Amateur

- **Proyecto:** `Piensa pe Chato`
- **Issue Central:** `soytensa/tensa-dev-workflow#87`
- **Repositorio Independiente:** `soytensa/piensa-pe-chato`
- **Rama:** `feat/landing-mvp-87`
- **Fecha:** 15 de octubre de 2026
- **Entorno Local:** `C:\Users\wesly\.gemini\antigravity\scratch\piensa-pe-chato`
- **Estado de Entrega:** `PENDING_REVIEW_BEFORE_PUBLISH` (Ajuste de contraste P1 aplicado y verificado con menú abierto; PR #1 conservado abierto, repositorio privado y GitHub Pages sin activar a la espera de autorización).

---

### 1. Detalle del Ajuste de Contraste (Revisión #3)

| Elemento | Diagnóstico Previo | Corrección Aplicada |
|---|---|---|
| **CTA Discord en Menú Móvil (`.mobile-discord-cta`)** | La regla general `.nav-links a` (especificidad `0,1,1`) sobrescribía a `.btn-primary` (`0,1,0`), asignando texto gris claro (`var(--text-muted)`) y hover blanco sobre el fondo degradado ámbar/naranja. | Añadida regla específica `.nav-links a.mobile-discord-cta, .nav-links a.mobile-discord-cta:hover, .nav-links a.mobile-discord-cta:focus, .nav-links a.mobile-discord-cta:active` forzando `color: #0f141c !important` (`rgb(15, 20, 28)`), `font-weight: 700 !important`, y suprimiendo el pseudo-elemento `::after` decorativo. |
| **Verificación de Contraste** | Contraste insuficiente en pantallas móviles y tablets. | Validado programáticamente vía CDP en Microsoft Edge headless: valor computado real **`color: rgb(15, 20, 28)`** con tipografía negrita **`700`**, garantizando legibilidad y cumplimiento WCAG AA. |

---

### 2. Resultados de la Auditoría Programática en Navegador Real (Edge Headless / CDP)

Ejecución de `tests/test_responsive_browser.py` midiendo dimensiones del DOM, ausencia de overflow y contraste con el menú desplegado:

```text
================== RESUMEN DE AUDITORIA RESPONSIVE Y CONTRASTE ==================
[PASS] mobile_320 (320px): scrollWidth=320px <= innerWidth=320px | Overflows=0 | Discord CTA Color: rgb(15, 20, 28) (Weight: 700)
[PASS] mobile_375 (375px): scrollWidth=375px <= innerWidth=375px | Overflows=0 | Discord CTA Color: rgb(15, 20, 28) (Weight: 700)
[PASS] mobile_390 (390px): scrollWidth=390px <= innerWidth=390px | Overflows=0 | Discord CTA Color: rgb(15, 20, 28) (Weight: 700)
[PASS] tablet_768 (768px): scrollWidth=768px <= innerWidth=768px | Overflows=0 | Discord CTA Color: rgb(15, 20, 28) (Weight: 700)
[PASS] desktop_1280 (1280px): scrollWidth=1280px <= innerWidth=1280px | Overflows=0
================================================================================
TODOS LOS BREAKPOINTS RESPONSIVE Y CONTRASTE SUPERADOS (0 OVERFLOWS, COLOR #0f141c VERIFICADO).
```

---

### 3. Inventario de Evidencias Visuales (Capturas de Pantalla)

Almacenadas en `evidence/issue-87/`:
- **Vistas Estándar:**
  * `render_mobile_320_320x640.png` (320x640, móvil compacto)
  * `render_mobile_375_375x812.png` / `render_mobile_375x812.png` (375x812, móvil estándar)
  * `render_mobile_390_390x844.png` (390x844, móvil moderno)
  * `render_tablet_768_768x1024.png` (768x1024, tablet vertical)
  * `render_desktop_1280_1280x800.png` / `render_desktop_1280x800.png` (1280x800, escritorio)
- **Vistas Específicas con Menú Abierto (Evidencia de Contraste del CTA):**
  * `render_menu_open_mobile_320_320x640.png` (320px, menú abierto con texto oscuro `#0f141c` visible)
  * `render_menu_open_mobile_375_375x812.png` (375px, menú abierto con texto oscuro `#0f141c` visible)
  * `render_menu_open_mobile_390_390x844.png` (390px, menú abierto con texto oscuro `#0f141c` visible)
  * `render_menu_open_tablet_768_768x1024.png` (768px, menú abierto con texto oscuro `#0f141c` visible)

---

### 4. Estado de la Suite de Pruebas Unitarias

Ejecución de `tests/test_landing.py` (8/8 pruebas superadas, 100% OK en 0.58s):
```text
test_01_required_files_exist ... ok
test_02_html_structure_and_relative_paths ... ok
test_03_inhouse_series_and_valve_application_status ... ok
test_04_discord_link_integrity ... ok
test_05_no_unverified_categorical_claims ... ok
test_06_proximamente_modules ... ok
test_07_accessibility_and_responsive_css ... ok
test_08_local_http_server_response ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.578s

OK
```

---

### 5. Estado de Entrega y Criterios de Seguridad

- **Rama:** `feat/landing-mvp-87` (sincronizada con origin).
- **Pull Request #1:** Conservado ABIERTO para revisión previa de ChatGPT/usuario.
- **Merge a main:** NO realizado.
- **GitHub Pages:** NO activado (repositorio permanece privado hasta autorización).
