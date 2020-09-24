# CSV 화일을 읽어서, DB Table에 쓰는 예제. (레코드를 리스트 형태로 읽음)

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

def readCSV_writeDB_List():

    # DB에 PlayerGK 테이블을 생성
    update = DB_Updates()
    update.dropPlayerGK()
    update.createPlayerGK()

    # CSV 화일을 읽기 모드로 생성, 리스트로 읽음
    with open('playerGK.csv', 'r', encoding='utf-8') as f:
        players = list(csv.reader(f))       # csv.reader()로 읽은 결과는 iterator이므로 len()를 사용할 수 없음.
                                    # 따라서 list()를 적용하여, players을 리스트의 리스트로 만듬.
        print(players)
        print()

        # PlayerGK 테이블에 레코드를 삽입
        for rowIDX in range(len(players)):
            if rowIDX == 0:
                print(players[rowIDX])
                print()
                continue
            else:
                row = players[rowIDX]                   # row는 리스트임.
                print(row)
                update.populatePlayerGK(*row)       # * operator
                # update.populatePlayerGK(row[0], row[1], ... row[12])

readCSV_writeDB_List()