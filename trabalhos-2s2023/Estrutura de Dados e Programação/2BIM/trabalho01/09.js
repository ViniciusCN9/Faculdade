function analisarLancamentos(dados) {
    if (dados.length !== 50) {
        console.log("O vetor deve ter exatamente 50 elementos.");
        return;
    }

    const contagemFaces = [0, 0, 0, 0, 0, 0]; // Inicializa a contagem para as faces de 1 a 6

    // Conta o número de ocorrências de cada face
    for (let i = 0; i < dados.length; i++) {
        const resultado = dados[i];

        if (resultado >= 1 && resultado <= 6) {
            contagemFaces[resultado - 1]++;
        } else {
            console.log(`Resultado inválido na posição ${i + 1}. Ignorando.`);
        }
    }

    // Calcula a porcentagem de ocorrência de cada face
    const porcentagens = contagemFaces.map((ocorrencias) => (ocorrencias / 50) * 100);

    // Exibe os resultados
    console.log("Número de ocorrências de cada face:", contagemFaces);
    console.log("Porcentagem de ocorrência de cada face:", porcentagens.map((percent) => percent.toFixed(2) + "%"));
}

// Simula 50 lançamentos de um dado (substitua isso pelos seus resultados reais)
const resultadosLancamentos = Array.from({ length: 50 }, () => Math.floor(Math.random() * 6) + 1);

// Exemplo de uso
analisarLancamentos(resultadosLancamentos);
