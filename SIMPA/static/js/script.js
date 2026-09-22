// SIMPA - JavaScript inicial
// Este arquivo fica preparado para futuras interações do frontend.

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".question-form");
    const button = document.querySelector(".button");

    if (!form || !button) {
        return;
    }

    form.addEventListener("submit", () => {
        button.disabled = true;
        button.textContent = "Enviando...";
    });
});
