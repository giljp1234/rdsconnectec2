import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = dynamodb.Table('test')
number = int(input("번호: "))
name = str(input("이름: "))
addr = str(input("주소: "))

table.update_item(
    Key={
        'number': number,
        'name': name
    },
    UpdateExpression='SET addr = :val1',
    ExpressionAttributeValues={
        ':val1': addr
    }
)


print("데이터 수정 완료")