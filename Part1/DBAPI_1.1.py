# PyMySQL 사용 절차 (검색문)

import pymysql

conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db='kleague', charset='utf8')

cursor = conn.cursor()	    # tuple based cursor

sql = "SELECT * FROM player"
cursor.execute(sql)

tuples = cursor.fetchall()      # 투플 타입의 투플, 어레이 처럼 처리
print(len(tuples))
print(tuples)
print()

print(tuples[0])
# ('2000001', '김태호', 'K10', None, None, None, 'DF', None, None, datetime.date(1971, 1, 29), '1', None, None)
print()

for rowIDX in range(len(tuples)):
    for columnIDX in range(len(tuples[0])):
        print(tuples[rowIDX][columnIDX], end=' ')       # 출력 후 줄바꿈 대신 끝문자(end로 정의)를 출력(한 줄에 결과값을 이어서 출력함.)
    print()                                           # print 문은 출력 후 줄바꿈함.

conn.close()