import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('contador-visitante')

def lambda_handler(event, context):
    response = table.get_item(
        Key={'id': '1'},
        ProjectionExpression='numeroatual'
    )
    
    # Pega o número e converte direto para string
    numero = response['Item']['numeroatual']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': str(numero)
    }

# --- TRUQUE PARA TESTAR LOCALMENTE ---
if __name__ == '__main__':
    print("Testando a Lambda localmente...")
    resultado = lambda_handler({}, {})
    print("Retorno da função:", resultado)