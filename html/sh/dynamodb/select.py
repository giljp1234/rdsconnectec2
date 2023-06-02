import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('test')

number = int(input("번호: "))
name = input("이름: ")
response = table.get_item(
    Key={
        'number': number,
        'name': name
    }
)

item = response.get('Item')

if item:
    addr = item.get('addr')

    print("번호:", number)
    print("이름:", name)
    print("주소:", addr)
else:
    print("해당 번호의 데이터가 존재하지 않습니다.")
