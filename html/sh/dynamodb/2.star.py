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


# number 를 * 로 설정하고 
# number 값에 (?) 를 넣으면 
# number 값에 (?) 로 되어있는 
# 모든 name 값이 나옴 
# ex) number 입력: 1
#{'number': '*', 'name': {'S': 'a'}}
#{'number': '*', 'name': {'S': 'abc'}}
#{'number': '*', 'name': {'S': 'agg'}}
#{'number': '*', 'name': {'S': 'awehagn'}}
#{'number': '*', 'name': {'S': 'hareahf'}}
#{'number': '*', 'name': {'S': 'kil'}}
#'number': '*', 'name': {'S': 'wehq'}}
# * = 1 
#이 코드는 number 가 * 로 설정되어있어서 
# name을 c 선택했을땐 데이터가 여러개여도
# name 값이 c 로 고정되고 
# number 는 * 로 나옴 
# 왜 ? 38번 라인에 그렇게 되어있음 
# 수정해보기.. 둘다 되는걸로 ;
