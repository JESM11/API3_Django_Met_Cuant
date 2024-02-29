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

async function fetchLcs() {
    const string1Input = document.getElementById('string1');
    const string2Input = document.getElementById('string2');
    const resultPre = document.getElementById('lcs-result');

    const string1 = string1Input.value;
    const string2 = string2Input.value;

    if (string1.trim() === '' || string2.trim() === '') {
        alert('Por favor ingrese ambos strings.');
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/lcsmain/${string1}/${string2}`
        );

        if (response.ok) {
            const data = await response.json();
            resultPre.textContent = JSON.stringify(data, null, 2);
        } else {
            console.log('pene');
            const errorMessage = await response.text();
            resultPre.textContent = `Error: ${response.status} - ${response.statusText}\n${errorMessage}`;
        }
    } catch (error) {
        console.error('Error fetching data:', error);
        // Handle the error
        // ...
    }

}

// Llamar a la función fetchFibonacci cuando se cargue la página
document.addEventListener('DOMContentLoaded', function() {
    const fibButton = document.getElementById('fibButton');
    if (fibButton) {
        fibButton.addEventListener('click', fetchFibonacci);
    } else {
        console.error("Button with id 'fetchButton' not found.");
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const lcsButton = document.getElementById('lcsButton');
    if (lcsButton) {
        lcsButton.addEventListener('click', fetchLcs);
    } else {
        console.error("Button with id 'lcsButton' not found.");
    }
});
