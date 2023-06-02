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
    name = input(f"Value {i+1} 입력: ")
    
    item = {'number': i+1, 'name': name}
    items.append(item)

print(items)

# DynamoDB 테이블 이름
table_name = 'test'

# 데이터 저장
batch_write_items(table_name, items)


# 첫번째 Number 의 값은 순서대로 저장 되고 
# name의 값만 input으로 받아서 
# 원하는 name을 저장할 수 있음 
# ex ) 
# number 1  /  name = kil
# number 2  /  name = hyeon
# number 3  /  name = haeun
# number 4  /  name = sik
# number ~~~/  name = (설정하는대로)