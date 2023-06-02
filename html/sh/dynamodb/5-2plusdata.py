import boto3

def select_update_item(table_name, condition_key, condition_value, update_key, additional_value):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    response = table.get_item(
        Key={
            condition_key: condition_value
        }
    )
    
    item = response.get('Item')
    
    if item:
        new_value = item.get(update_key, '') + additional_value
        
        table.update_item(
            Key={
                condition_key: condition_value
            },
            UpdateExpression=f'SET {update_key} = :val',
            ExpressionAttributeValues={
                ':val': new_value
            }
        )
        print(f"Item updated: {item}")
    else:
        print("Item not found.")

# DynamoDB 테이블 이름
table_name = 'test'

# 사용자로부터 조건 및 추가할 문자열 입력 받기
condition_key = input("파티션 키: ")
condition_value = input("정렬 키: ")
update_key = input("업데이트 파티션 키 입력: ")
additional_value = input("추가할 문자열 입력: ")

# 데이터 select 후 update
select_update_item(table_name, condition_key, condition_value, update_key, additional_value)



# 이것도 안됨 
# 5번은 다시 해봐야댐
# 5번은 다시해
# 5번 다시