// Función para realizar una solicitud a la API con el número ingresado
async function fetchFibonacci() {
    const numberInput = document.getElementById('numberInput');
    const resultPre = document.getElementById('fibonacci-result');

    // Validar que el número ingresado sea un entero positivo
    const n = parseInt(numberInput.value);
    if (isNaN(n) || n < 1) {
        alert('Ingresa un numero entero positivo.');
        return;
    }

    // Agregar un console.log para verificar el valor de n
    console.log(n);

    try {
        const response = await fetch(`http://127.0.0.1:5000/fibonacci?n=${n}`);

        if (response.ok) {
            const data = await response.json();
            // Mostrar el resultado en el espacio debajo del input
            resultPre.textContent = JSON.stringify(data, null, 2);
        } else {
            const errorMessage = await response.text();
            resultPre.textContent = `Error: ${response.status} - ${response.statusText}\n${errorMessage}`;
        }
    } catch (error) {
        console.error('Error fetching data:', error);
        // Mostrar un mensaje de error en caso de un problema durante la solicitud
        resultPre.textContent = 'Error fetching data. Please try again.';
    }
}

// Llamar a la función fetchFibonacci cuando se cargue la página
document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('fetchButton');
    if (button) {
        button.addEventListener('click', fetchFibonacci);
    } else {
        console.error("Button with id 'fetchButton' not found.");
    }
});
