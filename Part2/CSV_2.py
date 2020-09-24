# DB Table을 읽어서, CSV 화일로 쓰는 예제

import pymysql
import csv

class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='guest', password='bemyguest', db=db, charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     # dictionary based cursor
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:

    def selectPlayerUsingPosition(self, position):
        sql = "SELECT * FROM player WHERE position = %s"
        params = (position)                                 # 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

#########################################

def readDB_writeCSV():

    # DB 검색문 실행
    query = DB_Queries()
    players = query.selectPlayerUsingPosition("GK")     # 딕셔너리의 리스트
    # {'PLAYER_ID': '2007001', 'PLAYER_NAME': '정병지', 'TEAM_ID': 'K03', 'E_PLAYER_NAME': 'JEONG, BYUNGJI', 'NICKNAME': None, 'JOIN_YYYY': '2011', 'POSITION': 'GK', 'BACK_NO': 1, 'NATION': None, 'BIRTH_DATE': datetime.date(1980, 8, 4), 'SOLAR': '1', 'HEIGHT': 184, 'WEIGHT': 77}
    print(players)
    print()

    # CSV 화일을 쓰기 모드로 생성
    with open('playerGK.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)

        # 테이블 헤더를 출력
        columnNames = list(players[0].keys())
        # ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'E_PLAYER_NAME', 'NICKNAME', 'JOIN_YYYY', 'POSITION', 'BACK_NO', 'NATION', 'BIRTH_DATE', 'SOLAR', 'HEIGHT', 'WEIGHT']
        print(columnNames)
        print()

        wr.writerow(columnNames)
        # PLAYER_ID,PLAYER_NAME,TEAM_ID,E_PLAYER_NAME,NICKNAME,JOIN_YYYY,POSITION,BACK_NO,NATION,BIRTH_DATE,SOLAR,HEIGHT,WEIGHT

        # 테이블 내용을 출력
        for rowIDX in range(len(players)):
            row = list(players[rowIDX].values())
            print(row)
            # ['2007001', '정병지', 'K03', 'JEONG, BYUNGJI', '', '2011', 'GK', 1, '', datetime.date(1980, 8, 4), '1', 184, 77]

            wr.writerow(row)
            # 2007001,정병지,K03,"JEONG, BYUNGJI",,2011,GK,1,,1980-08-04,1,184,77
            # 날짜 변환 기능을 csv 패키지에서 제공함.

readDB_writeCSV()