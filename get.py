import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    table_name = 'NombreDeTuTabla'
    
    response = dynamodb.scan(
        TableName=table_name
    )
    
    items = response.get('Items', [])
    data = []
    
    for item in items:
        data.append({
            'nombre': item['Nombre']['S'],
            'foto': item['Foto']['S'],
            'telefono': item['Telefono']['S']
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
