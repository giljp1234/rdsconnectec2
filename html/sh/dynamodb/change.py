import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')

num_updates = int(input("수정할 데이터 개수를 입력하세요: "))

for i in range(num_updates):
    choice = input(f"수정할 데이터 {i+1}의 number 또는 name 중 하나를 선택하세요: ")

    if choice == 'number':
        value = input("number 입력: ")
        new_value = input("새로운 number 입력: ")
        response = dynamodb.update_item(
            TableName='test',
            Key={
                'number': {'N': value}
            },
            UpdateExpression='SET number = :val',
            ExpressionAttributeValues={
                ':val': {'N': new_value}
            }
        )
    elif choice == 'name':
        value = input("name 입력: ")
        new_value = input("새로운 name 입력: ")
        response = dynamodb.update_item(
            TableName='test',
            Key={
                'name': {'S': value}
            },
            UpdateExpression='SET name = :val',
            ExpressionAttributeValues={
                ':val': {'S': new_value}
            }
        )
    else:
        print("잘못된 선택입니다.")
        exit(1)

    print(f"데이터 {i+1} 수정이 완료되었습니다.")
