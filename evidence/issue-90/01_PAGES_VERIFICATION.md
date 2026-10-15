# Informe de Despliegue y Verificación en Producción — GitHub Pages

- **Proyecto:** Piensa pe Chato
- **Repositorio:** `soytensa/piensa-pe-chato`
- **Visibilidad:** `PUBLIC` (cambiado de privado a público con autorización del usuario)
- **Rama fuente:** `main` (SHA: `4c1b8b3c5e5e9067682284ff39e12382f7c40f01`)
- **Ruta fuente:** `/` (root)
- **URL Oficial:** https://soytensa.github.io/piensa-pe-chato/
- **Fecha y Hora de Verificación:** 15/10/2026 18:55 CEST (España)
- **Estado General:** **PUBLISHED & VERIFIED (HTTP 200)**

---

## 1. Verificación de Accesibilidad y Protocolo HTTP (Red Pública)

Se realizaron peticiones HTTP/1.1 con TLS hacia el dominio público de GitHub Pages obteniendo código 200 en todos los recursos estáticos requeridos:

| Recurso | URL | HTTP Status | Tamaño recibido |
|---|---|---|---|
| Landing HTML | `https://soytensa.github.io/piensa-pe-chato/` | **200 OK** | 24,873 bytes |
| Hoja de Estilos CSS | `https://soytensa.github.io/piensa-pe-chato/styles.css` | **200 OK** | 20,668 bytes |
| Lógica interactiva JS | `https://soytensa.github.io/piensa-pe-chato/app.js` | **200 OK** | 3,173 bytes |
| Favicon SVG | `https://soytensa.github.io/piensa-pe-chato/favicon.svg` | **200 OK** | 1,816 bytes |

---

## 2. Auditoría DOM y Responsive en Microsoft Edge Headless (CDP)

Se ejecutó una auditoría automatizada en directo contra la URL pública `https://soytensa.github.io/piensa-pe-chato/` vía Chrome DevTools Protocol:

- **Título de página:** `Piensa pe Chato — Dota 2 Inhouse Series & Comunidad`
- **Integridad de CTA Discord:** 4 enlaces apuntando exactamente a `https://discord.gg/Ac2WWFJGfQ` (Header, Hero, Sección Comunidad, Footer).
- **Desbordamiento horizontal (`scrollWidth > innerWidth`):** `False` (0 px de desbordamiento en desktop y móvil).
- **Menú Móvil Interactivo:** Despliegue correcto con toggle accesible (`aria-expanded="true"`), botón Discord con contraste verificado (`rgb(15, 20, 28)` sobre fondo dorado).
- **Pestañas Valve Tournament License:** Selector bilingüe (ES / EN) operativo.

---

## 3. Capturas de Pantalla de la Web Pública

Las siguientes capturas fueron tomadas directamente desde la URL de producción en GitHub Pages:

- **Escritorio (1280x800):** `evidence/issue-90/live_desktop_1280_1280x800.png`
- **Móvil (375x812 - Vista estándar):** `evidence/issue-90/live_mobile_375_375x812.png`
- **Móvil (375x812 - Menú desplegado):** `evidence/issue-90/live_menu_open_mobile_375_375x812.png`

---

## 4. Estado de la Solicitud Valve

Conforme a las instrucciones recibidas, la solicitud de Valve y su formulario **no han sido enviados ni manipulados**. La landing muestra con total transparencia el borrador oficial y el estado "En preparación", quedando lista para que el propietario del proyecto realice el envío manual tras confirmar la URL.
