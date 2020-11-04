import pymysql
from PyQt5.QtWidgets import *
import sys, datetime

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

    def updateExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='224800', db=db, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의
    def selectPlayerUsingPosition(self, position):
        sql = "SELECT * FROM player WHERE position = %s"
        params = (position)                                 # 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

class DB_Updates:
    # 모든 갱신문은 여기에 각각 하나의 메소드로 정의
    def insertPlayer(self, player_id, player_name, team_id, position):
        sql = "INSERT INTO player (player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
        params = (player_id, player_name, team_id, position)

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)

#########################################

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        # DB 검색문 실행
        query = DB_Queries()
        players = query.selectPlayerUsingPosition("GK")     # 딘셔너리의 리스트
        print(players)

        # 윈도우 설정
        self.setWindowTitle("DBAPI를 통한 테이블 위젯 생성 예제")
        self.setGeometry(0, 0, 1100, 600)

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        self.tableWidget.move(50, 50)
        self.tableWidget.resize(1000, 500)
        self.tableWidget.setRowCount(len(players))              # 43
        self.tableWidget.setColumnCount(len(players[0]))        # 13
        columnNames = list(players[0].keys())
        # ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'E_PLAYER_NAME', 'NICKNAME', 'JOIN_YYYY', 'POSITION', 'BACK_NO', 'NATION', 'BIRTH_DATE', 'SOLAR', 'HEIGHT', 'WEIGHT']
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX in range(len(players)):
            player = players[rowIDX]
            # {'PLAYER_ID': '2007001', 'PLAYER_NAME': '정병지', 'TEAM_ID': 'K03', 'E_PLAYER_NAME': 'JEONG, BYUNGJI', 'NICKNAME': None, 'JOIN_YYYY': '2011', 'POSITION': 'GK', 'BACK_NO': 1, 'NATION': None, 'BIRTH_DATE': datetime.date(1980, 8, 4), 'SOLAR': '1', 'HEIGHT': 184, 'WEIGHT': 77}

            for k, v in player.items():
                columnIDX = columnNames.index(k)

                if v == None:           # 파이썬이 DB의 널값을 None으로 변환함.
                    continue            # QTableWidgetItem 객체를 생성하지 않음
                elif isinstance(v, datetime.date):      # QTableWidgetItem 객체 생성
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

#########################################

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

main()