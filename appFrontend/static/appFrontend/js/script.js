document.addEventListener('DOMContentLoaded', function() {
    // 1. Seleccionamos el navbar
    const navbar = document.getElementById('mainNav');

    // Si no existe el navbar en esta página, detenemos el script para evitar errores
    if (!navbar) return; 

    // 2. Creamos la función que evalúa el scroll
    function chequearScroll() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    }

    // 3. Ejecutamos la función una vez al cargar la página 
    // (Por si el usuario recarga la página estando ya a la mitad)
    chequearScroll();

    // 4. El Event Listener: Esto es lo que faltaba. Escucha cada movimiento de scroll.
    window.addEventListener('scroll', chequearScroll);
});