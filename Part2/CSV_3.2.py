# CSV 화일을 읽어서, DB Table에 쓰는 예제. (레코드를 딕셔너리 형태로 읽음)

import pymysql
import csv

class DB_Utils:

    def updateExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='hyeokman', db=db, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()


class DB_Updates:

    def dropPlayerGK(self):
        sql = "DROP TABLE IF EXISTS playerGK"
        params = ()             # 넘겨줄 파라미터가 없음

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)

    def createPlayerGK(self):
        sql = '''CREATE TABLE playerGK (
                    player_id     CHAR(7) 		NOT NULL,
                    player_name   VARCHAR(20) 	NOT NULL,
                    team_id       CHAR(3) 		NOT NULL,
                    e_player_name VARCHAR(40),
                    nickname      VARCHAR(30),
                    join_YYYY     CHAR(4),
                    position      VARCHAR(10),
                    back_no       TINYINT,
                    nation        VARCHAR(20),
                    birth_date    DATE,
                    solar         CHAR(1),
                    height        SMALLINT,
                    weight        SMALLINT,
                    CONSTRAINT 	  pk_player 		PRIMARY KEY (player_id)
                )'''
        params = ()             # 넘겨줄 파라미터가 없음

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)

    def populatePlayerGK(self, player_id, player_name, team_id, e_player_name, nickname, join_YYYY, position, back_no, nation, birth_date, solar, height, weight):
        sql = "INSERT INTO playerGK VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (player_id, player_name, team_id, e_player_name, nickname, join_YYYY, position, back_no, nation, birth_date, solar, height, weight)

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)

#########################################

def readCSV_writeDB_Dictionary():

    # DB에 PlayerGK 테이블을 생성
    update = DB_Updates()
    update.dropPlayerGK()
    update.createPlayerGK()

    # CSV 화일을 읽기 모드로 생성, 딕셔너리로 읽음
    with open('playerGK.csv', 'r', encoding='utf-8') as f:
        players = list(csv.DictReader(f))       # csv.reader()로 읽은 결과는 iterator이므로 len()를 사용할 수 없음.
                                                # 따라서 list()를 적용하여, players을 리스트의 리스트로 만듬.
        print(players)
        print()

        # DB의 PlayerGK 테이블에 레코드를 삽입
        columnNames = list(players[0].keys())

        for player in players:
            row = []

            for columnName in columnNames:
                if columnName == 'BIRTH_DATE' and player[columnName] == '':     # MySQL에서 datetime 타입에 ''은 에러임. (BIRTH_DATE 처리)
                    player[columnName] = None

                row.append(player[columnName])

            print(row)

            update.populatePlayerGK(*row)       # * operator 사용
            # update.populatePlayerGK(row[0], row[1], ... row[12])

#       for rowIDX in range(len(players)):
#           row = list(players[rowIDX].values())
#           print(row)

#           update.populatePlayerGK(*row)  # * operator

readCSV_writeDB_Dictionary()