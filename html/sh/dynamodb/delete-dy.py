import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = dynamodb.Table('test')
number = int(input("번호: "))
name = str(input("이름: "))
addr = str(input("주소: "))

table.delete_item(
    Key = {
        'name': name,
        'number': number,
        'addr': addr
    }
    
)

if table.table_status == 'ACTIVE':
    print("삭제")
else:
    print("데이터 없음")
