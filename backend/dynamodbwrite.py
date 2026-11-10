#testee deploy
import boto3

def lambda_handler(event, context):
    # Toda a sua lógica principal que roda tanto na AWS quanto na sua máquina
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('contador-visitante')

    response = table.update_item(
        Key={'id': '1'},
        UpdateExpression='SET numeroatual = numeroatual + :contador',
        ExpressionAttributeValues={':contador': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    print(response['Attributes'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': str(response['Attributes']['numeroatual'])
    }

# --- TRUQUE PARA TESTAR LOCALMENTE ---
# A AWS ignora este bloco quando o código roda lá na nuvem.
# Mas na sua máquina, se você rodar "python dynamodbwrite.py", ele executa isso aqui embaixo!
if __name__ == '__main__':
    print("Testando a Lambda localmente...")
    # Simula o event e o context que a AWS mandaria
    lambda_handler({}, {})