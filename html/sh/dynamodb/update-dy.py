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
    UpdateExpression='SET addr = :val1, ',
    ExpressionAttributeValues={
        ':val1': addr
    }
)


print("데이터 수정 완료")




#숙 제 5번 : select랑 합쳐서 원하는 데이터값을 수정할 수 있게 ????? 
# +++++++ 기존에 있는 걸 불러와서 문자열을 추가해서 넣을 수 있게 만들어보기..?????
