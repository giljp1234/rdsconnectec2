#!bin/bash



sudo python3 -m pip install boto3

##Role 생성
# AWS Service >>> EC2 연결
#AmazonDynamoDBReadOnlyAccess 추가
#Role 이름 정하고  (ec2-dynamo)
#role 생성하고 ec2 인스턴스로 이동
#작업> 보안 > iam역할 수정
#ec2-dynamo 선택 후 저장 
#ec2로 가서 명령어 진행 

aws dynamodb scan --table-name test --region ap-northeast-2

python3 dynamodb.py