# 에러에 대비한 안전한 코드

import pymysql

conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db='kleague', charset='utf8')

try:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM player"    # 이 문장을 코멘트 처리할 경우
        cursor.execute(sql)
        players = cursor.fetchall()
        print(players)
except Exception as e:      # 예측 불가능한 모든 에러
    print(e)
    print(type(e))
finally:
    conn.close()