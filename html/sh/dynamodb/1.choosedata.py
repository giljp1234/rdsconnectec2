import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')

number = input("number 입력: ")

response = dynamodb.query(
    TableName='test',
    KeyConditionExpression='#num = :val',
    ExpressionAttributeNames={
        '#num': 'number'
    },
    ExpressionAttributeValues={
        ':val': {'N': number}
    }
)

items = response['Items']

for item in items:
    print(item)

##import boto3: boto3 모듈을 임포트합니다. 이 모듈은 AWS SDK를 사용하여 DynamoDB와 상호작용하는 데 사용됩니다.

#dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2'): boto3를 사용하여 DynamoDB 클라이언트를 생성합니다. 이 클라이언트를 통해 DynamoDB와 통신할 수 있습니다.

#number = input("number 입력: "): 사용자로부터 number 값을 입력받습니다.

#response = dynamodb.query(...): dynamodb.query 메서드를 사용하여 DynamoDB 테이블을 쿼리합니다. TableName에는 테이블의 이름인 'test'를 지정하고, 
#KeyConditionExpression에는 쿼리 조건을 설정합니다. 여기서는 number를 기준으로 항목을 가져오기 위해 '#num = :val'을 사용합니다. 
#ExpressionAttributeNames는 쿼리에서 사용되는 속성 이름을 정의하고, ExpressionAttributeValues는 쿼리에서 사용되는 값을 정의합니다.

#items = response['Items']: 쿼리 결과인 response에서 실제 항목들을 가져옵니다. response['Items']는 리스트 형태로 반환되며, 각 항목은 딕셔너리 형태로 표현됩니다.

#for item in items: ...: 가져온 항목들을 반복하면서 각 항목을 출력합니다. 이 부분을 원하는대로 수정하여 항목의 특정 속성만 출력하거나 원하는 방식으로 활용할 수 있습니다.

# number 를 고르면 
# 그에 맞는 데이터가 쭉 나옴 !
