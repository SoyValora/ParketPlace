document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const toggleBtn = document.getElementById("toggle-btn");

    toggleBtn.addEventListener("click", function () {
        sidebar.classList.toggle("collapsed");
    });
});
document.addEventListener("DOMContentLoaded", function () {
    let username = "Invitado"; // Aquí debes obtener el nombre real

    // Actualizar en la barra superior
    document.getElementById("username").innerText = username;

    // Actualizar en el mensaje de bienvenida
    document.getElementById("user-name-display").innerText = username;
});

document.getElementById("user-btn").addEventListener("click", () => {
    alert("Aquí podrías abrir el perfil de usuario.");
});

document.getElementById("notif-btn").addEventListener("click", () => {
    alert("Aquí podrías mostrar las notificaciones.");
});

