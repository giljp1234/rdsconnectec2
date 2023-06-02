import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = dynamodb.Table('test')
number = int(input("번호: "))
name = str(input("이름: "))
addr = str(input("주소: "))

table.put_item(
    Item={
        'number': number,
        'name': name,
        'addr': addr
    }
)

print("데이터 등록 완료")