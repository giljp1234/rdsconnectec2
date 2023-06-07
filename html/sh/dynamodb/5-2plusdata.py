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

#GPT 왈 된다된다된다하다가 마지막에!!!!!!!!!!!!!!!!

#업데이트하려는 속성 number가 키의 일부분이므로 업데이트할 수 없다는 것을 의미합니다.
#DynamoDB에서는 테이블의 키 속성은 변경할 수 없습니다. 키 속성은 데이터의 식별자이기 때문에 수정이 불가능합니다.
#만약 기존 데이터의 파티션 키에 새로운 값을 추가하고자 한다면, DynamoDB에서는 새로운 아이템으로 추가해야 합니다. 
# 이는 파티션 키를 변경하는 것이 아니라 새로운 아이템을 생성하는 것입니다.
#따라서, 기존 데이터의 파티션 키 값을 변경하는 것은 불가능하며, 새로운 아이템으로 추가해야 합니다.


#잘못된 정보를 삭제하고 새로운 데이터를 생성하는 것은 5-1 파일 !