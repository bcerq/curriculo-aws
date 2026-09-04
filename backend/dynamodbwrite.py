import boto3

#Definindo a tabela a ser usada
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('contador-visitante')

#Fazendo update 
response = table.update_item(
    Key={
        'id': '1'
    },
    UpdateExpression='SET numeroatual = numeroatual + :contador',
    ExpressionAttributeValues={
        ':contador': 1
    },
    ReturnValues='UPDATED_NEW'
)
print(response['Attributes'])
