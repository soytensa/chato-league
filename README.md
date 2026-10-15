# CHATO LEAGUE — SEASON ZERO (Landing Web Base)

🌐 **Sitio Web Oficial Publicado:** [https://soytensa.github.io/chato-league/](https://soytensa.github.io/chato-league/)

Repositorio de la landing oficial para la liga amateur piloto de Dota 2 **«CHATO LEAGUE — SEASON ZERO»** (periodo objetivo: 1 a 30 de noviembre de 2026), impulsada por la comunidad **«Piensa pe Chato»** como portal base de información y referencia para la tramitación de la solicitud de licencia amateur ante Valve Corporation.

---

## 🎯 Objetivo y Formato del Evento

- **Denominación Oficial ante Valve:** `Chato League - Season Zero`
- **Edición:** Season Zero (Liga amateur piloto y experimental).
- **Periodo:** 1 a 30 de noviembre de 2026 (sujeto a tramitación ante Valve).
- **Portal Base:** Web estática, responsive y accesible (HTML5 semántico, CSS3 moderno, Vanilla JavaScript) sin frameworks pesados, dependencias externas ni APIs de pago.
- **Formato Inhouse Fiel:** Partidas 5v5 en Captains Mode, plantillas dinámicas y rotativas, balance por capitanes y roles, lobbies organizados directamente en el cliente oficial de Dota 2 y cero datos simulados.
- **Independencia Operativa y Claridad Comunitaria:**
  - Separación explícita de la liga continua Inhouse frente al Torneo de Diciembre (que cuenta con su propio formato).
  - Lobbies de práctica y comunidad coordinados en el Discord oficial de Piensa pe Chato (`https://discord.gg/Ac2WWFJGfQ`).
  - Lobbies comunitarios pueden incluir partidas con jugadores de comunidades amigas como Chupetines EU; se aclara expresamente que Chupetines EU es una comunidad externa e independiente de la cual Piensa pe Chato no ostenta administración ni representación oficial.
- **Información de Solicitud Valve (Amateur League):** Sección bilingüe (Español / Inglés) estructurada según las pautas de Valve para licencias de torneos amateur ([Valve Tournament FAQ](https://help.steampowered.com/en/faqs/view/072E-47E8-B513-6E4E)), dejando claro que la solicitud está en preparación y la aprobación en trámite.
- **Comunidad & Discord:** Enlace oficial verificado a Discord (`https://discord.gg/Ac2WWFJGfQ`) con protección de datos y sin filtración de información privada.
- **Alcance No Transaccional de la Web:** Esta web estática no procesa pagos, venta de entradas ni gestión de apuestas. Los acuerdos privados entre participantes discurren fuera de la plataforma web.

---

## 🚀 Despliegue en GitHub Pages

La web se encuentra publicada de forma gratuita en GitHub Pages desde el repositorio público `soytensa/chato-league`:

- **Rama fuente:** `main`
- **Ruta fuente:** `/ (root)`
- **URL Canónica:**
  ```
  https://soytensa.github.io/chato-league/
  ```

> **Nota sobre Rutas Relativas**: Todos los assets (`styles.css`, `app.js`, `favicon.svg`) usan rutas relativas `./` para garantizar que la web funcione tanto bajo el subdirectorio de GitHub Pages (`/chato-league/`) como bajo un dominio raíz personalizado.

---

## 🛠️ Cómo Modificar Contenido

- **Textos y secciones**: Editar `index.html`.
- **Estilos, colores y tipografías**: Modificar las variables CSS en `:root` dentro de `styles.css`.
- **Configuración y enlaces**: Gestionar variables en `CONFIG` dentro de `app.js`.

---

## 🧪 Pruebas Automatizadas

El repositorio cuenta con tests unitarios y de integración para garantizar calidad técnica:

```bash
# Ejecutar suite de pruebas con pytest
pytest -v

# Ejecutar auditoría responsive y capturas con headless Edge (requiere Edge y websockets)
python tests/test_responsive_browser.py

# Ejecutar verificación de la web en vivo (producción)
python tests/test_live_pages.py
```

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
Dota 2 y sus marcas pertenecen a Valve Corporation. Este proyecto se rige por las directrices comunitarias de torneos amateur de Valve.
