document.addEventListener('DOMContentLoaded', function () {

    // MENU MOBILE
    const menuButton = document.querySelector('.menu-button-container');
    const menu = document.querySelector('.menu');

    if (menuButton) {
        menuButton.addEventListener('click', function () {
            this.classList.toggle('active');
            menu.classList.toggle('active');
        });
    }

    // NAVEGAÇÃO SUAVE
    const menuLinks = document.querySelectorAll('.menu-item-link');

    menuLinks.forEach(link => {
        link.addEventListener('click', e => {
            const href = link.getAttribute('href');

            // Se for link externo (como sobre.html), deixa ir normalmente
            if (!href.startsWith('#')) return;

            e.preventDefault();

            const alvo = document.querySelector(href);
            if (alvo) {
                window.scrollTo({
                    top: alvo.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // REVEAL ANIMATION
    function revealSections() {
        const reveals = document.querySelectorAll('.revelar');

        reveals.forEach(element => {
            const windowHeight = window.innerHeight;
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;

            if (elementTop < windowHeight - elementVisible) {
                element.classList.add('visivel');
            }
        });
    }

    window.addEventListener('scroll', revealSections);
    revealSections();

    // INTERAÇÃO DO BANNER
    const btnEnviarInteresse = document.getElementById('btnEnviarInteresse');
    const inputInteresse = document.getElementById('inputInteresse');
    const respostaInteresse = document.getElementById('respostaInteresse');

    if (btnEnviarInteresse) {
        btnEnviarInteresse.addEventListener('click', () => {
            const interesse = inputInteresse.value.trim();

            if (interesse) {
                respostaInteresse.textContent =
                    `Ótima escolha! Vamos te ajudar a aprender sobre ${interesse}.`;
                inputInteresse.value = '';
            } else {
                respostaInteresse.textContent = 'Por favor, digite um tópico de interesse.';
            }
        });

        inputInteresse.addEventListener('keypress', e => {
            if (e.key === 'Enter') btnEnviarInteresse.click();
        });
    }

// =============================
// INTERAÇÃO COM USUÁRIO
// =============================
const btnEnviar = document.getElementsByClassName('btn-enviar');
const usuarioInput = document.getElementById('usuario-input');
const respostaUsuario = document.getElementById('resposta-usuario');

document.querySelectorAll('.btn-enviar').forEach(btn => {
    btn.addEventListener('click', () => {
        const valor = usuarioInput.value.trim();

        if (!valor) {
            respostaUsuario.textContent = "Por favor, digite algo!";
            return;
        }

        respostaUsuario.textContent =
            `Que ótimo! Temos conteúdos incríveis sobre "${valor}" esperando por você. 🚀`;

        usuarioInput.value = '';
    });
});


///////////////////////////////////////////////
//  LOGIN - CADASTRO
///////////////////////////////////////////////
const forms = document.getElementById("forms");
const loginBox = document.getElementById("loginBox");
const cadastroBox = document.getElementById("cadastroBox");
const toCadastro = document.getElementById("toCadastro");
const toLogin = document.getElementById("toLogin");

toCadastro.addEventListener("click", () => {
    forms.style.transform = "translateX(-50%)";
    loginBox.classList.remove("active");
    cadastroBox.classList.add("active");
});

toLogin.addEventListener("click", () => {
    forms.style.transform = "translateX(0%)";
    cadastroBox.classList.remove("active");
    loginBox.classList.add("active");
});

// Mostrar/ocultar senha
document.querySelectorAll(".toggle-password").forEach(toggle => {
    toggle.addEventListener("click", () => {
        const input = toggle.previousElementSibling;
        if (input.type === "password") {
            input.type = "text";
            toggle.textContent = "🙈";
        } else {
            input.type = "password";
            toggle.textContent = "👁️";
        }
    });
});
     
// Validação extra
document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", (e) => {
        if (!form.checkValidity()) {
            e.preventDefault();
            alert("Por favor, preencha todos os campos corretamente!");
        }
    });
});
