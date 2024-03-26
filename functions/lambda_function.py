import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('crc-visitor-count')
tableName = 'crc-visitor-count'


def lambda_handler(event, context):
    print(event)
    