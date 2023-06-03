#데이터 값들 중
#원하는 값을 가진 데이터를 골라서 볼 수 있음 

#-----ex 데이터 저장 값 
# number 100 , 100 , 100 , 90 , 80 
# name    a  ,  b  ,  c  ,  c ,  b

#number 선택 후 100 입력시
# name a, b, c 값 나옴

# name 선택 후 c 입력시
# number 100 , 90 나옴 ! 

import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')

choice = input("number 또는 name 중 하나를 선택하세요: ")

if choice == 'number':
    key_name = 'number'
elif choice == 'name':
    key_name = 'name'
else:
    print("잘못된 선택입니다.")
    exit(1)

value = input(f"{key_name} 입력: ")

if key_name == 'number':
    response = dynamodb.query(
        TableName='test',
        KeyConditionExpression='#num = :val',
        ExpressionAttributeNames={
            '#num': key_name
        },
        ExpressionAttributeValues={
            ':val': {'N': value}
        }
    )
else:
    response = dynamodb.scan(
        TableName='test',
        FilterExpression='#nm = :val',
        ExpressionAttributeNames={
            '#nm': key_name
        },
        ExpressionAttributeValues={
            ':val': {'S': value}
        }
    )

items = response['Items']

for item in items:
    item[key_name] = value  # number 또는 name을 *로 대체
    
    print(item)
