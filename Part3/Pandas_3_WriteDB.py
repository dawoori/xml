# Pandas DataFrame을 읽어서, DB Table에 쓰는 예제.

import pymysql
import pandas as pd

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

def readPandas_writeDB():

    playersCW = {
        'PLAYER_ID': ['2007001', '2007020', '2007035', '2007067', '2007106', '2007130', '2007203', '2007227', '2007236', '2007255', '2007298', '2008138', '2008179', '2008410', '2008499', '2008902', '2009004', '2009045', '2009070', '2009101', '2009133', '2010057', '2010059', '2010108', '2010125', '2011018', '2011021', '2011052', '2011065', '2011069', '2011082', '2012006', '2012007', '2012039', '2012047', '2012052', '2012054', '2012076', '2012081', '2012088', '2012089', '2012094', '2012107'],
        'PLAYER_NAME': ['정병지', '서동명', '김운재', '정광수', '정이섭', '김대희', '조범철', '최종문', '조의손', '정해운', '이은성', '김용발', '최동우', '양지원', '김충호', '선원길', '최호진', '권찬수', '최창주', '양영민', '김준호', '김승준', '박유석', '정지혁', '백민철', '우태식', '이현', '정경진', '허인무', '최주호', '권정혁', '김창민', '최관민', '이무림', '강성일', '한동진', '남현우', '정용대', '정영광', '염동균', '김정래', '최동석', '정경두'],
        'TEAM_ID': ['K03', 'K01', 'K02', 'K02', 'K05', 'K03', 'K02', 'K07', 'K09', 'K08', 'K10', 'K05', 'K05', 'K01', 'K04', 'K13', 'K02', 'K08', 'K01', 'K08', 'K03', 'K10', 'K06', 'K06', 'K09', 'K09', 'K04', 'K06', 'K03', 'K03', 'K01', 'K05', 'K05', 'K01', 'K10', 'K04', 'K04', 'K06', 'K07', 'K07', 'K07', 'K09', 'K08'],
        'E_PLAYER_NAME': ['JEONG, BYUNGJI', 'SEO, DONGMYUNG', 'KIM, WOONJAE', 'JEONG, GWANGSOO', 'JEONG, ISUB', 'KIM, DAEHEE', 'CHO, BUMCHUL', None, None, 'JEONG, HAEWOON', 'LEE, EUNSUNG', 'KIM, YONGBAL', None, 'YANG, JIWON', None, None, 'CHOI, HOJIN', 'KWON, CHANSOO', 'CHOI, CHANGZOO', 'YANG, YOUNGMIN', 'KIM, 06HO', 'KIM, SEUNG06', None, None, None, None, None, None, 'HEO, INMOO', 'CHOI, JUHO', 'KWON, 06GHYUK', 'KIM, CHANGMIN', 'CHOI, KWANMIN', 'LEE, MOOLIM', 'KANG, SUNGIL', None, None, None, None, None, None, None, 'JEONG, KYOUNGDOO'],
        'NICKNAME': [None, None, None, None, '쾌남', None, None, None, None, None, '수호천황', None, None, None, None, None, None, None, None, None, None, '개구멍', '터프가이', None, None, None, None, '임꺽정', None, None, None, '고릴라', None, None, None, None, None, None, None, None, None, None, None],
        'JOIN_YYYY': ['2011', '2012', None, None, '2012', '2010', None, None, None, None, '2007', '2004', None, '2008', None, None, None, None, '2009', None, '2009', '2010', '2010', '2010', None, None, None, '2011', '2011', '2011', '2011', '2012', '2012', '2012', '2012', None, None, '2012', None, None, None, None, None],
        'POSITION': ['GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK', 'GK'],
        'BACK_NO': [1, 21, 1, 41, 45, 31, 21, 1, 44, 1, 21, 18, 60, 45, 60, 46, 31, 21, 40, 31, 21, 1, 1, 31, 21, 31, 1, 41, 41, 51, 1, 1, 31, 31, 30, 21, 31, 40, 41, 31, 33, 1, 41],
        'NATION': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        'BIRTH_DATE': ['1980-08-04', '1984-04-05', '1983-12-04', '1987-10-03', '1984-06-04', '1984-04-04', '1980-11-09', '1980-02-10', '1970-12-01', '1983-04-12', '1981-05-04', '1983-09-03', '1980-03-11', '1984-08-04', '1978-04-07', '1996-09-04', '1986-10-10', '1984-03-05', '1982-07-09', '1984-05-07', '1983-03-04', '1982-01-09', '1987-10-06', '1991-02-11', '1987-03-07', '1993-08-01', '1988-07-11', '1988-07-02', '1988-02-04', '1992-07-07', '1988-02-08', '1990-10-01', '1989-08-05', '1989-09-04', '1989-04-06', '1989-08-25', '1989-04-20', '1989-11-10', '1993-03-06', '1993-06-09', '1989-12-11', '1991-03-05', None],
        'SOLAR': ['1', '1', '1', '1', '1', '1', '2', '1', '1', '2', '1', '1', '1', '1', '2', '1', '1', '2', '1', '1', '1', '1', '2', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1'],
        'HEIGHT': [184, 196, 182, 182, 185, 192, 185, 185, 192, 185, 184, 183, 187, 181, 185, 174, 190, 183, 187, 190, 185, 183, 186, 187, 185, 185, 192, 186, 187, 185, 195, 191, 188, 185, 182, 183, 180, 189, 185, 189, 185, 190, 194],
        'WEIGHT': [77, 94, 82, 79, 78, 88, 85, 76, 87, 79, 82, 77, 78, 75, 83, 66, 82, 77, 86, 80, 77, 77, 78, 77, 78, 75, 85, 78, 81, 75, 80, 87, 85, 79, 80, 78, 72, 83, 80, 83, 81, 89, 76]
    }

    # dataframe 생성
    df = pd.DataFrame(playersCW)
    print(df)
    print()

    # dataframe에 대한 다양한 연산을 여기서 수행

    # dataframe을 파이썬 리스트로 변경
    players = df.values.tolist()
    print(players)
    print()

    # DB에 PlayerGK 테이블을 생성
    update = DB_Updates()
    update.dropPlayerGK()
    update.createPlayerGK()

    # 파이썬 리스트를 DB에 기록
    for player in players:
        update.populatePlayerGK(*player)  # * operator 사용
        # update.populatePlayerGK(player[0], player[1], ... player[12])

readPandas_writeDB()