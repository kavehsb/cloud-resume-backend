import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('crc-visitor-count-table')

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'test'},
        UpdateExpression='SET visitor_count = visitor_count + :val', 
        ExpressionAttributeValues={':val': 1},
        ReturnValues='UPDATED_NEW'
    )

    # Get the updated visitor count
    visitor_count = response['Attributes']['visitor_count']
    
    return {
        'statusCode': 200,
        'body': f'Visitor count updated to {visitor_count}'
    }