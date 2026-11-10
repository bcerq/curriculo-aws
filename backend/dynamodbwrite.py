import boto3

def lambda_handler(event, context):
    # Toda a sua lógica principal que roda tanto na AWS quanto na sua máquina
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('contador-visitante')

    # Realiza o incremento atômico no DynamoDB
    response = table.update_item(
        Key={'id': '1'},
        UpdateExpression='SET numeroatual = numeroatual + :contador',
        ExpressionAttributeValues={':contador': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    # Pega o valor atualizado de forma segura
    attributes = response.get('Attributes', {})
    numero_atual = attributes.get('numeroatual', 0)
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': str(numero_atual)
    }

# --- TRUQUE PARA TESTAR LOCALMENTE ---
if __name__ == '__main__':
    print("Testando a Lambda localmente...")
    resultado = lambda_handler({}, {})
    print("Retorno da função:", resultado)