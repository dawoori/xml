# DB Table을 읽어서, XML 화일에 쓰는 예제

import pymysql
import xml.etree.ElementTree as ET
import datetime

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

def readDB_writeXML():

    # DB 검색문 실행
    query = DB_Queries()
    players = query.selectPlayerUsingPosition("GK")     # 딕셔너리의 리스트
    # {'PLAYER_ID': '2007001', 'PLAYER_NAME': '정병지', 'TEAM_ID': 'K03', 'E_PLAYER_NAME': 'JEONG, BYUNGJI', 'NICKNAME': None, 'JOIN_YYYY': '2011', 'POSITION': 'GK', 'BACK_NO': 1, 'NATION': None, 'BIRTH_DATE': datetime.date(1980, 8, 4), 'SOLAR': '1', 'HEIGHT': 184, 'WEIGHT': 77}
    print(players)
    print()

    # 애트리뷰트 BIRTH_DATE의 값을 MySQL datetime 타입에서 스트링으로 변환함. (CSV에서는 패키지가 변환함.)
    for player in players:
        for k, v in player.items():
            if isinstance(v, datetime.date):
                player[k] = v.strftime('%Y-%m-%d')      # 키가 k인 item의 값 v를 수정

    newDict = dict(playerGK = players)
    print(newDict)

    # XDM 트리 생성
    tableName = list(newDict.keys())[0]
    tableRows = list(newDict.values())[0]

    rootElement = ET.Element('Table')
    rootElement.attrib['name'] = tableName

    for row in tableRows:
        rowElement = ET.Element('Row')
        rootElement.append(rowElement)

        for columnName in list(row.keys()):
            if row[columnName] == None:  # NICKNAME, JOIN_YYYY, NATION 처리
                rowElement.attrib[columnName] = ''
            else:
                rowElement.attrib[columnName] = row[columnName]

            if type(row[columnName]) == int:  # BACK_NO, HEIGHT, WEIGHT 처리
                rowElement.attrib[columnName] = str(row[columnName])

    # XDM 트리를 화일에 출력
    ET.ElementTree(rootElement).write('playerGK.xml', encoding='utf-8', xml_declaration=True)

readDB_writeXML()