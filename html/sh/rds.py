import pymysql
import sys
import os
import base64
#import requests
import time
import logging


# RDS 연결 설정
rds_host = "mysql-cluster-test.cluster-ceu1cbdwfs8l.ap-northeast-2.rds.amazonaws.com"  # RDS 엔드포인트(endpoint) 입력
db_username = "admin"  # RDS 사용자명 입력
db_password = "wnsvy486"  # RDS 비밀번호 입력
db_name = "test"  # RDS 데이터베이스명 입력

# RDS에 연결
try:
    conn = pymysql.connect(
        host=rds_host,
        user=db_username,
        password=db_password,
        database=db_name,
        connect_timeout=5
    )
    cursor = conn.cursor()
    
    print("RDS에 성공적으로 연결되었습니다.")

    # 연결에 대한 추가 작업 수행
    # ...

except pymysql.Error as e:
    print("RDS 연결 오류:", e)
    
finally :
    

    data = input("데이터를 입력하세요: ")
    query = "INSERT INTO number (id) VALUES (%s)"
    cursor.execute(query, (data,))

    conn.commit()
    cursor.close()
    conn.close()


    print("MYSQL Connection End")

#conn = connection
#cursor = 이를 통해서 mysql 쿼리를 실행 할 수 있다?....