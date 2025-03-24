const prompt = require('prompt-sync')()

const TEMPERATURAS = [];
const HORAS_DO_DIA = [
    "Meia-noite", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM",
    "8 AM", "9 AM", "10 AM", "11 AM", "Meio-dia", "1 PM", "2 PM", "3 PM",
    "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM"
];

function lerTemperaturas() {
    for (let i = 0; i < 24; i++) {
        const temperatura = parseFloat(prompt(`Informe a temperatura às ${HORAS_DO_DIA[i]} (em graus Celsius):`));

        if (isNaN(temperatura)) {
            console.log("Por favor, informe um valor numérico.");
            return;
        }

        TEMPERATURAS.push(temperatura);
    }
}

function calcularEExibirResultados() {
    let maiorTemperatura = Number.MIN_VALUE;
    let menorTemperatura = Number.MAX_VALUE;
    let horaMaiorTemperatura;
    let horaMenorTemperatura;
    let somaTemperaturas = 0;

    for (let i = 0; i < TEMPERATURAS.length; i++) {
        const temperatura = TEMPERATURAS[i];

        if (temperatura > maiorTemperatura) {
            maiorTemperatura = temperatura;
            horaMaiorTemperatura = i;
        }

        if (temperatura < menorTemperatura) {
            menorTemperatura = temperatura;
            horaMenorTemperatura = i;
        }

        somaTemperaturas += temperatura;
    }

    const mediaTemperaturas = somaTemperaturas / TEMPERATURAS.length;

    console.log("Maior temperatura:", maiorTemperatura, "°C, às", HORAS_DO_DIA[horaMaiorTemperatura]);
    console.log("Menor temperatura:", menorTemperatura, "°C, às", HORAS_DO_DIA[horaMenorTemperatura]);
    console.log("Média das TEMPERATURAS:", mediaTemperaturas.toFixed(2), "°C");
}

// Exemplo de uso
lerTemperaturas();
if (TEMPERATURAS) {
    calcularEExibirResultados();
}
