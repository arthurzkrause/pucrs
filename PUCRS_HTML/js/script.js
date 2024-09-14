// script.js

// Exemplo de validação simples de formulário
function validateForm() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        const nameInput = document.getElementById('nome');
        if (nameInput.value === '') {
            alert('Por favor, preencha o nome.');
            event.preventDefault();
        }
    });
}
document.addEventListener('DOMContentLoaded', validateForm);

