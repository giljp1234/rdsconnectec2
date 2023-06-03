import boto3

def batch_write_items(test, items):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(test)

    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

# 데이터 예시
items = []

num_items = int(input("저장할 아이템 수: "))

for i in range(num_items):
    number = int(input(f"Number {i+1} 입력"))
    name = input(f"Name {i+1} 입력: ")

    item = {'number': number, 'name': name}
#    item = {'number': i+1, 'name': name}  #number 값 1번부터 순서대로

    items.append(item)

print(items)

# DynamoDB 테이블 이름
table_name = 'test'

# 데이터 저장
batch_write_items(table_name, items)


# 첫번째 Number 의 값은 순서대로 저장 되고 
# name의 값만 input으로 받아서 
# 원하는 name을 저장할 수 있음  
# ex(17과 20 주석 후에 >> 21번 주석풀고 사용시  number 값만 1부터 순서대로 됨
# ex ) 
# number 16  /  name = kil
# number 42  /  name = hyeon
# number 773 /  name = haeun
# number 66  /  name = sik
# number (원하는 숫자)  /  name = (설정하는대로)