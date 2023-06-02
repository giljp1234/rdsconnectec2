import array
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('test2')

items = array.array('u')

num_items = int(input("저장할 아이템 수: "))

for i in range(num_items):
    number = input(f"number {i+1} 입력: ")
    name = input(f"name {i+1} 입력: ")

    items.extend(number)
    items.extend(name)

# 일괄 저장
with table.batch_writer() as batch:
    for i in range(0, len(items), 2):
        item = {'number': items[i], 'name': items[i+1]}
        batch.put_item(Item=item)

print("데이터 저장 완료")


# array 사용시 파일 이름 array.py 못함 
# array 사용시 문자열만 가능하다고 함 ; 왜지 ; ㅇㅇ
# 그래서 dynamoDB 생성시 아예 숫자 말고 문자열로 받아서
# 숫자를 '1' , '2' 이런식으로 문자열로 받아서하면 가능함
# ps) 1 = 숫자 '1'=문자열