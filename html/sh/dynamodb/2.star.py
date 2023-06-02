import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')

choice = input("number 또는 name 중 하나를 선택하세요: ")

if choice == 'number':
    value = input("number 입력: ")
    response = dynamodb.query(
        TableName='test',
        KeyConditionExpression='#num = :val',
        ExpressionAttributeNames={
            '#num': 'number'
        },
        ExpressionAttributeValues={
            ':val': {'N': value}
        }
    )
elif choice == 'name':
    value = input("name 입력: ")
    response = dynamodb.scan(
        TableName='test',
        FilterExpression='#nm = :val',
        ExpressionAttributeNames={
            '#nm': 'name'
        },
        ExpressionAttributeValues={
            ':val': {'S': value}
        }
    )
else:
    print("잘못된 선택입니다.")
    exit(1)

items = response['Items']

for item in items:
    item['number'] = '*'  # number를 *로 대체
    print(item)
