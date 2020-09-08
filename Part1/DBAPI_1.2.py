# PyMySQL 사용 절차 (단일 갱신문)

import pymysql

conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db='kleague', charset='utf8')

cursor = conn.cursor()	    # tuple based cursor

sql = "INSERT INTO player(player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
cursor.execute(sql, ('2020001', '손홍민', 'K01', 'FW'))
cursor.execute(sql, ('2020002', '호날두', 'K02', 'FW'))
conn.commit()

sql = "SELECT * FROM player"
cursor.execute(sql)
tuples = cursor.fetchall()
print(tuples)
print(len(tuples))
print()

sql = "DELETE FROM player WHERE player_id = %s"
cursor.execute(sql, '2020001')
cursor.execute(sql, '2020002')
conn.commit()

sql = "SELECT * FROM player"
cursor.execute(sql)
tuples = cursor.fetchall()
print(tuples)
print(len(tuples))

conn.close()