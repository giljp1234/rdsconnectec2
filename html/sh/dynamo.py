
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = dynamodb.Table('test')
table = dynamodb.list_tables()
print(tables)


# import boto3

#dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
#table = dynamodb.Table('test')

allData = table.scan()

print(allData['Items'])