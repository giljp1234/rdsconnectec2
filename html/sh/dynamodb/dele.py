import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('test')

number = int(input("번호: "))
name = str(input("이름: "))

try:
    response = table.delete_item(
        Key={
            'number': number,
            'name': name
        }
    )
    print("삭제 완료")
except ClientError as e:
    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        print("데이터가 존재하지 않습니다.")
    else:
        print("삭제 과정에서 오류가 발생했습니다.")