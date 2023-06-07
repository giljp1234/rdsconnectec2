############
############
#새로운 key 를 생성하고 (파티션키, 정렬키 이후 새로운 키 )
## EX ) number 와 name 의 키값 존재한다고 가정
## address 를 키값으로 추가해서 주소의 정보도 받고 싶다 
## 현재 데이터값이 number = 1 name = cms 라고 했을때
# ( 원래 테이블안에 존재하는 데이터 값)
## partition_key_value 값에 1
## sort_key_value 값에 cms 

## 여기서 부터 새로 추가 !!!!------------
## new_attr_key 값에 addr 
## new_attr_value 값에 Seoul 
# 이렇게 작성하면 addr 이라는 키와 그 안에 Seoul 이라는 데이터가 등록됨 

## 다른 키값을 추가할 수 있고,   Key 값은 데이터정보들의 대표 이름 !!!!!!!!!

## 3번째에 input에 있는 new_attr_key값에 addr 치고 속성값 입력시 수정도 가능 
###  3번째 input에 phone 을 쓸 경우 또 키값 추가 가능 
## 이후 3번째 input은 number와 name 을 제외한 새로 추가한 키값들에 대해 불러와서 
## 4번째 input을 통해 데이터 수정 및 추가가 가능 .....
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('strtest')

partition_key_value = input("새로운 파티션 키 값을 입력하세요: ")
sort_key_value = input("새로운 정렬 키 값을 입력하세요: ")
new_attr_key = input("새로운 속성 키 값을 입력하세요: ")
new_attr_value = input("새로운 속성 값을 입력하세요: ")

item_key = {'number': partition_key_value, 'name': sort_key_value}

update_expression = f'SET {new_attr_key} = :new_value'

response = table.update_item(
    Key=item_key,
    UpdateExpression=update_expression,
    ExpressionAttributeValues={
        ':new_value': new_attr_value
    }
)

print("새로운 키 값이 추가되었습니다.")