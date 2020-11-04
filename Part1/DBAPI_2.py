# PyMySQL 사용 절차

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='224800', db='kleague', charset='utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor)    # dictionary based cursor, 딕셔너리의 리스트

sql = "SELECT * FROM player"
cursor.execute(sql)

players = cursor.fetchall()      # 딕셔너리의 리스트
print(len(players))
print(players)
print()

print(players[0])
# {'PLAYER_ID': '2000001', 'PLAYER_NAME': '김태호', 'TEAM_ID': 'K10', 'E_PLAYER_NAME': None, 'NICKNAME': None, 'JOIN_YYYY': None, 'POSITION': 'DF', 'BACK_NO': None, 'NATION': None, 'BIRTH_DATE': datetime.date(1971, 1, 29), 'SOLAR': '1', 'HEIGHT': None, 'WEIGHT': None}
print()

# value만 출력할 때
columnNames = list(players[0].keys())
print(columnNames)
print()

for player in players:              # player는 딕셔너리임.
    for columnName in columnNames:
        print(player[columnName], end=' ')
    print()

print()

# Key와 value를 같이 출력할 때
for player in players:              # player는 딕셔너리임.
    kvlist = list(player.items())
    for (k, v) in kvlist:
        print(k, v, end=', ')
    print()

conn.close()