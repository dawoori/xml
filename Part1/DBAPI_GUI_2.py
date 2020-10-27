import pymysql
from PyQt5.QtWidgets import *
import sys, datetime

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

class DB_Queries:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의

    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingPosition(self, value):
        if value == '없음':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE position = %s"
            params = (value)         # SQL문의 실제 파라미터 값의 튜플

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

        # 윈도우 설정
        self.setWindowTitle("DBAPI를 통한 테이블 위젯 제어 예제")
        self.setGeometry(0, 0, 1100, 620)

        # 라벨 설정
        self.label = QLabel("POSITION", self)
        self.label.move(200, 50)
        self.label.resize(100, 20)

        # 콤보박스 설정
        self.comboBox = QComboBox(self)

        # DB 검색문 실행
        query = DB_Queries()
        rows = query.selectPlayerPosition()        # rows은 dictionary의 리스트
        print(rows)
        print()
        # [{'position': 'DF'}, {'position': 'FW'}, {'position': None}, {'position': 'MF'}, {'position': 'GK'}]

        columnName = list(rows[0].keys())[0]
        items = ['없음' if row[columnName] == None else row[columnName] for row in rows]
        self.comboBox.addItems(items)

        # for row in rows:
        #     item = list(row.values()).pop(0)
        #     if item == None:
        #         self.comboBox.addItem('없음')
        #     else:
        #         self.comboBox.addItem(item)

        self.comboBox.move(300, 50)
        self.comboBox.resize(100, 20)
        self.comboBox.activated.connect(self.comboBox_Activated)

        # 푸쉬버튼 설정
        self.pushButton = QPushButton("Search", self)
        self.pushButton.move(600, 50)
        self.pushButton.resize(100, 20)
        self.pushButton.clicked.connect(self.pushButton_Clicked)

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        self.tableWidget.move(50, 100)
        self.tableWidget.resize(1000, 500)

    def comboBox_Activated(self):

        self.positionValue = self.comboBox.currentText()  # positionValue를 통해 선택한 포지션 값을 전달

    def pushButton_Clicked(self):

        # DB 검색문 실행
        query = DB_Queries()
        players = query.selectPlayerUsingPosition(self.positionValue)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(players))
        self.tableWidget.setColumnCount(len(players[0]))
        columnNames = list(players[0].keys())
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for rowIDX in range(len(players)):
            player = players[rowIDX]

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