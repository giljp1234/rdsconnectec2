import boto3

def select_update_item(table_name, condition_number, condition_name, update_number, update_name):
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table = dynamodb.Table(table_name)

    response = table.query(
        KeyConditionExpression='#num = :val',
        ExpressionAttributeNames={
            '#num': 'number'
        },
        ExpressionAttributeValues={
            ':val': int(condition_number)
        }
    )
    
    items = response['Items']

    for item in items:
        # Delete the item with the old partition key
        table.delete_item(Key={'number': int(condition_number), 'name': condition_name})
        
        # Create a new item with the updated partition key
        new_item = {
            'number': int(update_number),
            'name': update_name
        }
        
        try:
            table.put_item(Item=new_item)
            print("데이터 저장 성공")
        except Exception as e:
            print("데이터 저장 실패:", str(e))

# DynamoDB 테이블 이름
table_name = 'test'

# 사용자로부터 조건 및 업데이트 값 입력 받기
condition_number = input(" original number: ")
condition_name = input("original name: ")
update_number = input("update number: ")
update_name = input("update name: ")

# 데이터 select 후 update
select_update_item(table_name, condition_number, condition_name, update_number, update_name)


#데이터가 저장되어있는 상태에서 수정하려면
#데이터를 삭제하고 다시 만들어야한다고함 .....
# 그래서 데이터 정보 확인 > 삭제 > 생성 으로해서 가능.