# PyMySQL 사용 절차 (갱신문 n번 실행)

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='224800', db='kleague', charset='utf8')

cursor = conn.cursor()	    # tuple based cursor

newPlayers = (
    ('2020001', '손홍민', 'K01', 'FW'),
    ('2020002', '호날두', 'K02', 'FW'),
    ('2020003', '메시', 'K03', 'FW')
)
sql = "INSERT INTO player(player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, newPlayers)
conn.commit()

sql = "SELECT * FROM player"
cursor.execute(sql)
tuples = cursor.fetchall()
print(tuples)
print(len(tuples))

conn.close()