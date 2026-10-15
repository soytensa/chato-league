/**
 * Piensa pe Chato — Dota 2 Inhouse Series
 * JavaScript MVP (Vanilla, sin dependencias ni llamadas a APIs externas)
 */

const CONFIG = {
  // Enlace oficial de invitación Discord proporcionado para el MVP (Issue #87)
  discordInviteUrl: "https://discord.gg/Ac2WWFJGfQ",
  leagueName: "Piensa pe Chato — Inhouse Series 2026",
  season: "2026",
  githubRepo: "https://github.com/soytensa/piensa-pe-chato"
};

document.addEventListener("DOMContentLoaded", () => {
  // 1. Inicializar enlaces a Discord de forma centralizada
  const discordCtaButtons = document.querySelectorAll(".js-discord-cta");
  discordCtaButtons.forEach(btn => {
    btn.setAttribute("href", CONFIG.discordInviteUrl);
    btn.setAttribute("target", "_blank");
    btn.setAttribute("rel", "noopener noreferrer");
  });

  // 2. Control del menú de navegación móvil
  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const navLinks = document.getElementById("nav-links");

  const closeMobileMenu = () => {
    if (navLinks && navLinks.classList.contains("open")) {
      navLinks.classList.remove("open");
      if (mobileMenuBtn) {
        mobileMenuBtn.setAttribute("aria-expanded", "false");
      }
    }
  };

  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener("click", () => {
      const isOpen = navLinks.classList.toggle("open");
      mobileMenuBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    // Cerrar menú móvil al hacer clic en enlaces de navegación
    navLinks.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        closeMobileMenu();
      });
    });
  }

  // 3. Pestañas de información Valve (ES / EN)
  const tabButtons = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");

  const switchValveTab = (targetLang) => {
    tabButtons.forEach(b => {
      b.classList.remove("active");
      b.setAttribute("aria-selected", "false");
    });
    tabContents.forEach(c => c.classList.remove("active"));

    const activeBtn = document.querySelector(`.tab-btn[data-tab="${targetLang}"]`);
    if (activeBtn) {
      activeBtn.classList.add("active");
      activeBtn.setAttribute("aria-selected", "true");
    }

    const activeContent = document.getElementById(`valve-lang-${targetLang}`);
    if (activeContent) {
      activeContent.classList.add("active");
    }
  };

  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetLang = btn.getAttribute("data-tab");
      switchValveTab(targetLang);
    });
  });

  // 4. Selectores de acceso directo a la información de Valve (desktop y móvil)
  const setupValveQuickBtn = (btnId) => {
    const btn = document.getElementById(btnId);
    if (!btn) return;
    btn.addEventListener("click", () => {
      closeMobileMenu();
      const valveSection = document.getElementById("valve-compliance");
      if (valveSection) {
        valveSection.scrollIntoView({ behavior: "smooth" });
        switchValveTab("en");
      }
    });
  };

  setupValveQuickBtn("header-lang-toggle");
  setupValveQuickBtn("mobile-lang-toggle");
});
