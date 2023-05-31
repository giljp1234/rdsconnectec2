import pymysql


cursor = conn.cursor()

data = input("데이터를 입력하세요: ")
query = "INSERT INTO number (id) VALUES (%s)"
cursor.execute(query, (data,))

conn.commit()
cursor.close()
conn.close()
