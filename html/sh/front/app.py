from flask import Flask, render_template, request, redirect, url_for
import boto3

app = Flask(__name__)

# AWS 설정
aws_region = 'ap-northeast-2'  # 본인이 사용하는 리전으로 변경하세요.
dynamodb_table_name = 'inttest'  # 본인이 사용하는 DynamoDB 테이블 이름으로 변경하세요.

# DynamoDB 클라이언트 생성
dynamodb = boto3.client('dynamodb', region_name=aws_region)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data_key = request.form['number']
    data_value = request.form['name']

    # 유효성 검증: key와 value가 비어있는지 확인
    if not data_key or not data_value:
        return 'Key와 Value를 모두 입력해주세요.'

    # DynamoDB에 데이터 저장
    dynamodb.put_item(
        TableName=dynamodb_table_name,
        Item={
            'number': {'N': data_key},
            'name': {'S': data_value}
        }
    )

    return redirect(url_for('success', number=data_key, name=data_value))
@app.route('/fail')
def fail():
    return render_template('fail.html')

@app.route('/list')
def data_list():
    page = int(request.args.get('page', 1))

    # DynamoDB에서 데이터 개수 및 페이지 계산
    response = dynamodb.scan(
        TableName=dynamodb_table_name,
        Select='COUNT'
    )
    total_items = response['Count']
    total_pages = ceil(total_items / items_per_page)

    # DynamoDB에서 데이터 가져오기
    response = dynamodb.scan(
        TableName=dynamodb_table_name,
        Limit=items_per_page,
        ExclusiveStartKey={
            'number': {'N': str((page - 1) * items_per_page + 1)}
        }
    )
    data_list = response['Items']

    # 이전 페이지 및 다음 페이지 계산
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None

    return render_template('list.html', data_list=data_list, prev_page=prev_page, next_page=next_page)

@app.route('/search')
def search_data():
    query = request.args.get('query')

    # DynamoDB에서 데이터 검색
    response = dynamodb.scan(
        TableName=dynamodb_table_name,
        FilterExpression='contains (#name, :query)',
        ExpressionAttributeNames={
            '#name': 'name'
        },
        ExpressionAttributeValues={
            ':query': {'S': query}
        }
    )
    data_list = response['Items']

    return render_template('list.html', data_list=data_list)

@app.route('/edit/<number>')
def edit_data(number):
    # DynamoDB에서 데이터 가져오기
    response = dynamodb.get_item(
        TableName=dynamodb_table_name,
        Key={
            'number': {'N': number}
        }
    )
    data = response['Item']
    data_key = data['number']['N']
    data_value = data['name']['S']

    return render_template('edit.html', data_key=data_key, data_value=data_value)

@app.route('/success')
def success():
    data_key = request.args.get('data_key')
    data_value = request.args.get('data_value')
    return render_template('success.html', data_key=data_key, data_value=data_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')