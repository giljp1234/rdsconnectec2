import boto3 #(aws에서 제공하는 서비스에 접근할 수 있도록 만들어진 라이브러리)

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


#숙 제 1 번 : 한번에 여러개의 정보를 불러오는 방법 ? 골라서 

#숙 제 2 번 : Key 값 안에 number or name 둘 중 하나를 * 로 바꾸고 했을때 나오는 결과 
