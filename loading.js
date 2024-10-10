document.getElementById('loadButton').addEventListener('click', function() {
    
    // para mostrar la pantalla de carga

    const loadingScreen = document.getElementById('loadingScreen');
    
    loadingScreen.style.display = 'flex';

    // Permite poner un temporizador a la pantalla de carga
    
    setTimeout(function() {
        loadingScreen.style.display = 'none';

    }, 2000); // Cambiar el 3000 al numero de milisegundos que quieres que la pantalla se muestre
});