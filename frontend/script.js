// Substitua pela Invoke URL completa do seu API Gateway (aquela que pega lá em Stages)
const API_URL = 'https://SUA-URL-DO-API-GATEWAY.execute-api.us-east-1.amazonaws.com';

async function carregarContador() {
    try {
        // Faz a requisição GET para a sua Lambda de leitura
        let resposta = await fetch(`${API_URL}/get`);
        let valor = await resposta.json();
        
        // Joga o valor dentro da tag HTML que tem o ID 'contador'
        document.getElementById('contador').innerText = valor;
    } catch (erro) {
        console.error("Erro ao carregar o contador:", erro);
        document.getElementById('contador').innerText = "--";
    }
}

// Executa assim que a página abre
carregarContador();