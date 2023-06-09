import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = dynamodb.Table('inttest')


number = int(input("번호: "))
name = str(input("이름: "))


table.put_item(
    Item={
        'number': number,
        'name': name

    }
)

print("데이터 등록 완료")

# 숙 제 3 : select 여러번하려면 데이터가 많아야되는데 
# 반복문안에서 다른 데이터들을 저장하는 코드 만들어보기  (for문)

# 숙 제 4 : 
# array를 이용해서 put item 한번해서 
# 10개의 데이터를 한번에 저장해보는 거 ????????????????????????????????????
# 배열 구조로 된 파일을 만들어서 파일자체를 저장하는 방법

