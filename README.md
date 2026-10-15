# Piensa pe Chato — Dota 2 Inhouse Series (Landing Web Base)

🌐 **Sitio Web Oficial Publicado:** [https://soytensa.github.io/piensa-pe-chato/](https://soytensa.github.io/piensa-pe-chato/)

Repositorio de la landing pública para la comunidad amateur de Dota 2 **«Piensa pe Chato»**, diseñada como portal base de información y referencia para la tramitación de la solicitud de licencia de liga amateur **«Piensa pe Chato — Inhouse Series 2026»** ante Valve Corporation.

---

## 🎯 Objetivo y Alcance del MVP

- **Portal Base**: Web estática, responsive y accesible (HTML5 semántico, CSS3 moderno, Vanilla JavaScript) sin frameworks pesados, dependencias externas ni APIs de pago.
- **Formato Inhouse Fiel**: Documentación clara de partidas 5v5 en Captains Mode, plantillas rotativas, balance por capitanes y roles, lobbies en cliente oficial y cero datos simulados.
- **Independencia Operativa**: Separación explícita de la liga continua Inhouse frente al Torneo de Diciembre (que cuenta con su propio formato).
- **Información de Solicitud Valve (Amateur League)**: Sección bilingüe (Español / Inglés) estructurada según las pautas de Valve para licencias de torneos amateur ([Valve Tournament FAQ](https://help.steampowered.com/en/faqs/view/072E-47E8-B513-6E4E)), dejando claro que el ticket y la aprobación están en trámite.
- **Comunidad & Discord**: Enlace oficial verificado a Discord (`https://discord.gg/Ac2WWFJGfQ`) con protección de datos y sin filtración de información privada.
- **Alcance No Transaccional de la Web**: Esta web estática no procesa pagos, venta de entradas ni gestión de apuestas. Los acuerdos privados entre participantes discurren fuera de la plataforma web.

---

## 🚀 Despliegue en GitHub Pages (Guía Paso a Paso)

Para publicar la web de forma gratuita en GitHub Pages una vez autorizada la entrega:

1. **Visibilidad del Repositorio**:
   - En **Settings** > **Danger Zone** > **Change repository visibility**, cambiar a **Public** (si la cuenta es GitHub Free, Pages requiere repositorio público).
2. **Configuración de Pages**:
   - Ir a la pestaña **Settings** del repositorio.
   - En el menú lateral izquierdo, seleccionar **Pages** (dentro de la sección *Code and automation*).
   - En **Build and deployment** > **Source**, seleccionar: **Deploy from a branch**.
   - En **Branch**, seleccionar la rama `main` (o la rama de publicación deseada) y la carpeta `/ (root)`.
   - Pulsar el botón **Save**.
3. **Verificación de URL**:
   - Tras unos segundos o minutos, GitHub Pages publicará el sitio en la URL:
     ```
     https://soytensa.github.io/piensa-pe-chato/
     ```
   - Probar la URL en el navegador y verificar que responde con código **HTTP 200**.

> **Nota sobre Rutas Relativas**: Todos los assets (`styles.css`, `app.js`, `favicon.svg`) usan rutas relativas `./` para garantizar que la web funcione tanto bajo el subdirectorio de GitHub Pages (`/piensa-pe-chato/`) como bajo un dominio raíz personalizado.

---

## 🌐 Configuración de Dominio Personalizado (Opcional)

Si posteriormente se desea vincular un dominio propio (por ejemplo, `piensapechato.com` o similar):

1. En **Settings** > **Pages** > **Custom domain**, escribir el dominio deseado y hacer clic en **Save**.
2. GitHub creará automáticamente un archivo `CNAME` en la raíz del repositorio.
3. En el proveedor de DNS del dominio (Cloudflare, Namecheap, etc.), crear:
   - Registro `CNAME`: nombre `www` apuntando a `soytensa.github.io`.
   - O registros `A` apuntando a las IPs oficiales de GitHub Pages:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
4. Marcar la casilla **Enforce HTTPS** en los ajustes de Pages una vez emitido el certificado SSL.

---

## 🛠️ Cómo Modificar Contenido

- **Actualizar Enlace de Discord**:
  - Modificar la propiedad `discordInviteUrl` en `app.js`.
  - Actualizar los atributos `href` de clase `.js-discord-cta` en `index.html`.
- **Modificar Reglas o Formato Inhouse**:
  - Editar la sección `<section id="inhouse-series">` en `index.html`.
- **Actualizar Información de Solicitud Valve**:
  - Editar los paneles `#valve-lang-es` y `#valve-lang-en` dentro de `index.html`.
- **Estilos Visuales**:
  - Editar `styles.css`. Las variables principales (colores, fuentes, espaciados) se encuentran al inicio en `:root`.

---

## 🛡️ Políticas de Seguridad y Uso Aceptable de la Web

1. **Naturaleza Estática e Informativa**:
   - Este sitio web alojado en GitHub Pages no incluye ni incluirá pasarelas de pago, cobro de entradas, venta de ítems ni módulos de apuestas deportivas.
   - Es una herramienta puramente informativa y comunitaria. Cualquier interacción o acuerdo privado entre jugadores se efectúa fuera de la web y queda a criterio de evaluación de Valve en la solicitud.
2. **Privacidad de la Comunidad**:
   - No se publican nombres reales, números telefónicos, domicilios ni claves privadas de jugadores o administradores.
3. **Propiedad Intelectual y Marcas**:
   - Dota 2 y Valve son marcas registradas de Valve Corporation. Este portal es una iniciativa comunitaria amateur.
   - El favicon y diseño gráfico son de autoría original sin reutilizar logotipos de terceros con derechos reservados.

---

## 📂 Estructura del Proyecto

```text
piensa-pe-chato/
├── index.html           # Landing page principal (HTML5 accesible y responsive)
├── styles.css           # Estilos temáticos esports dark mode (sin frameworks)
├── app.js               # Lógica ligera (configuración de enlaces, tabs Valve, menú móvil)
├── favicon.svg          # Emblema vectorizado original
├── README.md            # Documentación de uso, despliegue y mantenimiento
├── tests/               # Pruebas automatizadas de integridad local
│   └── test_landing.py
└── evidence/            # Registro de auditoría y verificación TensaDev
    └── issue-87/
        └── 01_MVP_LANDING_VERIFICATION.md
```
