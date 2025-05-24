document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const toggleBtn = document.getElementById("toggle-btn");

    const userBtn = document.getElementById('user-btn');
    const userContainer = document.getElementById('user-container');

    const notifBtn = document.getElementById('notif-btn');
    const notifContainer = document.getElementById('notification-container');

  
    // Toggle de sidebar
    toggleBtn.addEventListener("click", function () {
        sidebar.classList.toggle("collapsed");
    });

    // Botón de perfil de usuario
    userBtn.addEventListener('click', (event) => {
        
        event.stopPropagation(); // Evita que el clic llegue al document
        // Cierra notificaciones si están abiertas
        notifContainer.classList.add('d-none');
        // Toggle de user
        userContainer.classList.toggle('d-none');
    });

    // Botón de notificaciones
    notifBtn.addEventListener('click', (event) => {
        event.stopPropagation();
        // Cierra el perfil si está abierto
        userContainer.classList.add('d-none');
        // Toggle de notificaciones
        notifContainer.classList.toggle('d-none');
    });

    // Cerrar ambos al hacer clic fuera
    document.addEventListener('click', (event) => {
        // Si el clic NO fue dentro de los contenedores ni los botones
        if (!userContainer.contains(event.target) && !userBtn.contains(event.target)) {
            userContainer.classList.add('d-none');
        }

        if (!notifContainer.contains(event.target) && !notifBtn.contains(event.target)) {
            notifContainer.classList.add('d-none');
        }
    });
 
    document.getElementById('metodoPago').addEventListener('change', function () {
        const metodo = this.value;
        document.getElementById('tarjetaCreditoFields').classList.add('d-none');
        document.getElementById('pseFields').classList.add('d-none');

        if (metodo === 'TARJETA_CREDITO') {
            document.getElementById('tarjetaCreditoFields').classList.remove('d-none');
        } else if (metodo === 'PSE') {
            document.getElementById('pseFields').classList.remove('d-none');
        }
    });

        // Manejar el envío del formulario
        document.getElementById('registro-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevenir el comportamiento por defecto (enviar el formulario)

            // Obtener los valores del formulario
            const datos = {
                nombres: document.getElementById('nombres').value,
                apellidos: document.getElementById('apellidos').value,
                documentoIdent: document.getElementById('documentoIdent').value,
                codUniversidad: document.getElementById('codUniversidad').value,
                email: document.getElementById('email').value,
                password: document.getElementById('password').value,
                programa: document.getElementById('programa').value,
                fechaNacimiento: document.getElementById('fechaNacimiento').value,
                celular: document.getElementById('celular').value
            };

            // Enviar los datos a la API de Flask usando fetch
            fetch('http://localhost:3000/usuario/registro', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            })
            .then(response => response.json())
            .then(data => {
                // Mostrar mensaje de éxito o error
                alert(data.message || data.error);
            })
            .catch(error => {
                console.error('Error al registrar el usuario:', error);
                alert('Ocurrió un error al intentar registrar el usuario.');
            });
        });
  
});
