import boto3

def select_update_item(table_name, condition_key, condition_value, update_key, update_value):
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table = dynamodb.Table('test')

    response = table.scan(
        FilterExpression=boto3.dynamodb.conditions.Key(condition_key).eq(condition_value)
    )
    
    items = response['Items']

    for item in items:
        item[update_key] = update_value
        table.put_item(Item=item)

# DynamoDB 테이블 이름
table_name = 'test'

# 사용자로부터 조건 및 업데이트 값 입력 받기
condition_key = input("파티션 키: ")
condition_value = input("정렬 키: ")
update_key = input("업데이트 파티션 키 입력: ")
update_value = input("새로운 정렬 키 입력: ")

# 데이터 select 후 update
select_update_item(table_name, condition_key, condition_value, update_key, update_value)



#안됨
# 숫자도 안되고
# 문자도 안됨
# 왜 안됨 
#왬놀얌ㄴ어햐ㅐㅓ맺겨ㅐㅅㅎㅈ댜ㅕㅗㅇ너ㅔㅐㅓㅎ매서
