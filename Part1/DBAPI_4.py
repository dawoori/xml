# Dynamic SQL (SQL injection 공격에 대비)

import pymysql

conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db='kleague', charset='utf8')

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM player WHERE position = %s"        # dynamic SQL
        params = ('GK')
        cursor.execute(sql, params)
        players = cursor.fetchall()
        print(players)
except Exception as e:
    print(e)
    print(type(e))
finally:
    conn.close()