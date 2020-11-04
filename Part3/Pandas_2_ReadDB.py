# DB Table을 읽어서, Pandas DataFrame으로 처리하는 예제

import pymysql
import pandas as pd

class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='224800', db=db, charset='utf8')

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

def readDB_writePandas():

    # DB 검색문 실행
    query = DB_Queries()
    players = query.selectPlayerUsingPosition("GK")     # 딕셔너리의 리스트
    # {'PLAYER_ID': '2007001', 'PLAYER_NAME': '정병지', 'TEAM_ID': 'K03', 'E_PLAYER_NAME': 'JEONG, BYUNGJI', 'NICKNAME': None, 'JOIN_YYYY': '2011', 'POSITION': 'GK', 'BACK_NO': 1, 'NATION': None, 'BIRTH_DATE': datetime.date(1980, 8, 4), 'SOLAR': '1', 'HEIGHT': 184, 'WEIGHT': 77}
    print(players)
    print()

    # 행 우선 구조를 열 우선 구조로 변환함.
    columnNames = list(players[0].keys())
    playersCW = {}

    for columnName in columnNames:
        playersCW[columnName] = []

    print(playersCW)
    print()

    for rowIDX in range(len(players)):
        for columnName in columnNames:              # BIRTH_DATE의 경우, 변환을 자동으로 해줌.
            playersCW[columnName].append(players[rowIDX][columnName])

    print(playersCW)
    print()

    # pandas DataFrame으로 생성
    df = pd.DataFrame(playersCW)
    print(df)

    print(df['BIRTH_DATE'])
    print()

readDB_writePandas()