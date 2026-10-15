# Informe de Publicación y Verificación — CHATO LEAGUE: SEASON ZERO

- **Proyecto:** Chato League — Season Zero (migración de marca y URL oficial)
- **Repositorio oficial:** [soytensa/chato-league](https://github.com/soytensa/chato-league) (renombrado limpiamente desde `soytensa/piensa-pe-chato` preservando historial completo, commits y PRs)
- **Visibilidad:** `PUBLIC`
- **Rama:** `main`
- **Pull Request:** [#2](https://github.com/soytensa/chato-league/pull/2) (Squash & Merge)
- **Merge SHA:** `e095dd9713c9900b53ee9d18e1c92e839ffc1cc1`
- **URL Canónica Oficial:** https://soytensa.github.io/chato-league/
- **Fecha y Hora de Verificación:** 15/10/2026 19:40 CEST (España)
- **Estado General:** **PUBLISHED & VERIFIED (HTTP 200)**

---

## 1. Actualización de Marca, Identidad y Formato

1. **Marca y Edición:**
   - Nombre oficial del evento: **CHATO LEAGUE**
   - Edición: **SEASON ZERO**
   - Denominación oficial que debe figurar ante Valve: **`Chato League - Season Zero`**
2. **Formato Piloto Experimental:**
   - Temporada piloto del **1 al 30 de noviembre de 2026**.
   - Partidas privadas 5v5 en **Captains Mode**, alineaciones dinámicas y rotativas por jornada, balance competitivo dirigido por capitanes y roles.
   - Lobbies organizados directamente en el cliente oficial de Dota 2 sin software invasivo ni datos simulados.
3. **Claridad Comunitaria y Relación con Otras Comunidades:**
   - Impulsado por la comunidad y servidor de Discord de **Piensa pe Chato** (`https://discord.gg/Ac2WWFJGfQ`).
   - Independencia explícita frente al Torneo de Diciembre (que mantiene formato y cuadro propio).
   - Se aclara formalmente que partidas comunitarias pueden coincidir con miembros de comunidades amigas como **Chupetines EU**; se hace constar de forma transparente que Chupetines EU es una comunidad externa e independiente de la cual Piensa pe Chato no ostenta administración ni representación oficial.
4. **Transparencia y No Transaccionalidad:**
   - Web estática sin pasarelas de pago, sin cobro de entradas ni gestión de apuestas. Los acuerdos privados entre jugadores discurren al margen de la plataforma web.
   - Herramientas de analítica y estadísticas marcadas honestamente como "Próximamente".

---

## 2. Pruebas de Conectividad y Protocolo (Red Pública en Producción)

Peticiones HTTP/1.1 directas con TLS hacia el dominio público de GitHub Pages:

| Recurso | URL | HTTP Status | Tamaño recibido |
|---|---|---|---|
| Landing HTML | `https://soytensa.github.io/chato-league/` | **200 OK** | 26,096 bytes |
| Hoja de Estilos CSS | `https://soytensa.github.io/chato-league/styles.css` | **200 OK** | 21,042 bytes |
| Lógica interactiva JS | `https://soytensa.github.io/chato-league/app.js` | **200 OK** | 3,195 bytes |
| Favicon SVG | `https://soytensa.github.io/chato-league/favicon.svg` | **200 OK** | 1,816 bytes |

---

## 3. Auditoría de Renderizado y DOM en Microsoft Edge Headless (CDP)

Auditoría automatizada en directo ejecutada contra la URL oficial `https://soytensa.github.io/chato-league/`:

- **Título verificado:** `CHATO LEAGUE — SEASON ZERO | Dota 2 Amateur League & Comunidad`
- **Canónica & OpenGraph:** `https://soytensa.github.io/chato-league/`
- **Enlaces Discord:** 4 enlaces verificados hacia `https://discord.gg/Ac2WWFJGfQ`.
- **Desbordamiento horizontal (`scrollWidth > innerWidth`):** `False` (0 px de desbordamiento en todos los viewports: 320px, 375px, 390px, 768px y 1280px).
- **Menú Móvil y Accesibilidad:** Botón hamburguesa interactivo con `aria-expanded="true"`; botón CTA de Discord con contraste validado (`#0f141c` / `rgb(15, 20, 28)` sobre fondo dorado).
- **Pestañas Valve:** Selector de idioma (Español / English) interactivo y funcional.

---

## 4. Capturas de Pantalla de Producción (Web Pública)

- **Escritorio (1280x800):** `evidence/issue-92/live_desktop_1280_1280x800.png`
- **Móvil (375x812 - Vista estándar):** `evidence/issue-92/live_mobile_375_375x812.png`
- **Móvil (375x812 - Menú desplegado):** `evidence/issue-92/live_menu_open_mobile_375_375x812.png`

---

## 5. Estado de la Solicitud Valve

Conforme a las directrices de la Issue #92, el formulario de Valve **no ha sido manipulado ni enviado**. La URL limpia y estable `https://soytensa.github.io/chato-league/` queda lista y disponible para que el propietario la ingrese en su borrador de solicitud ante Valve.
