const API_URL = 'https://j6cpp0mx8a.execute-api.us-east-1.amazonaws.com';

async function atualizarEContarVisita() {
    try {
        // 1. Faz um POST para a  Lambda de escrita somar +1 visita no DynamoDB
        await fetch(`${API_URL}/post`, {
            method: 'POST'
        });

        // 2. Logo em seguida, faz o GET para ler o valor atualizado e jogar na tela
        let resposta = await fetch(`${API_URL}/get`);
        let valor = await resposta.json();
        
        // Exibe o número na tag HTML com id="contador"
        document.getElementById('contador').innerText = valor;
    } catch (erro) {
        console.error("Erro ao atualizar o contador:", erro);
        document.getElementById('contador').innerText = "--";
    }
}

// Roda assim que a página é aberta
atualizarEContarVisita();