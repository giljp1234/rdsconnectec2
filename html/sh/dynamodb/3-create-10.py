import boto3

def batch_write_items(test, items):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(test)

    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

# 데이터 예시
items = [
#    {'number': 1, 'name': 'a'},
#   {'number': 2, 'name': 'b'},
#    {'number': 3, 'name': 'c'},
    # 나머지 데이터 추가
]
for i in range(1, 26):
    key = int(i)
    value = chr(ord('a') + i - 1)
    item = {'number': key, 'name': value}
    items.append(item)

print(items)

# DynamoDB 테이블 이름
table_name = 'test'

# 데이터 저장
batch_write_items(table_name, items)

## 데이터 값을 작성해서 받을 수 있고 
# 테스트 겸 1~26번까지 순서대로 데이터를 받고 
# a ~ y까지 순서대로 데이터를 저장하게 만듦
#위에 주석처럼 작성한 대로 저장하는 것도 가능
