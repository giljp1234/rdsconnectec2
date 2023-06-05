import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')

number = input("number 입력: ")
name = input("name 입력: ")

response = dynamodb.query(
    TableName='test',
    KeyConditionExpression='#num = :val1 AND #nm = :val2',
    ExpressionAttributeNames={
        '#num': 'number',
        '#nm': 'name'
    },
    ExpressionAttributeValues={
        ':val1': {'N': number},
        ':val2': {'S': name}
    }
)

items = response['Items']

for item in items:
    print(item)