import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('test')

items = []

num_items = int(input("저장할 아이템 수: "))

for i in range(num_items):
    number = int(input(f"number {i+1} 입력: "))
    name = input(f"name {i+1} 입력: ")

    item = {'number': number, 'name': name}
    items.append(item)

# 일괄 저장
with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

print("데이터 저장 완료")

#dynamoDB 생성 시
#schema에 맞게 해야함 
#ex) DB생성시 (number = 숫자 , name=문자열로 test라는 테이블 만듬)
#코드에서도 number ==int name == 문자 (string) 으로 지정해야하고
#그에 맞는 값 number == 1 , name == something 처럼 받아야
#저장이 가능한 것 같음 !

