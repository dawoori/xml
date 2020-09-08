# PyMySQL 사용 절차

import pymysql

conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db='kleague', charset='utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor)	# dictionary based cursor

sql = "SELECT * FROM player"
cursor.execute(sql)

tuples = cursor.fetchall()      # 딕셔너리 타입의 리스트, 어레이 처럼 처리
print(tuples)
print(len(tuples))
print('')

print(tuples[0])
# {'PLAYER_ID': '2000001', 'PLAYER_NAME': '김태호', 'TEAM_ID': 'K10', 'E_PLAYER_NAME': None, 'NICKNAME': None, 'JOIN_YYYY': None, 'POSITION': 'DF', 'BACK_NO': None, 'NATION': None, 'BIRTH_DATE': datetime.date(1971, 1, 29), 'SOLAR': '1', 'HEIGHT': None, 'WEIGHT': None}
print('')

# value만 출력할 때
columnNames = list(tuples[0].keys())
for tuple in tuples:
    for columnName in columnNames:
        print(tuple[columnName], end=' ')
    print('')

print('')

# Key와 value를 같이 출력할 때
for tuple in tuples:
    kvlist = list(tuple.items())
    for (k, v) in kvlist:
        print(k, v, end=', ')
    print('')

conn.close()