import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    table_name = 'NombreDeTuTabla'
    
    response = dynamodb.put_item(
        TableName=table_name,
        Item={
            'ID': {'S': 'ID-Único-AutoGenerado'},  # Puedes generar un ID único
            'Nombre': {'S': data['nombre']},
            'Foto': {'S': data['foto']},
            'Telefono': {'S': data['telefono']}
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Datos guardados con éxito')
    }
