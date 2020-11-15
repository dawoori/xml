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
    def selectPlayerTeam(self):
        sql = "SELECT DISTINCT team_id FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerNation(self):
        sql = "SELECT DISTINCT nation FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayerUsingPosition(self, value):
        if value == '미정':
            sql = "SELECT * FROM player WHERE position IS NULL"
            params = ()
        else:
            sql = "SELECT * FROM player WHERE position = %s"
            params = (value)         # SQL문의 실제 파라미터 값의 튜플

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectPlayer(self, sql):
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def makeQuery(self, team, position, nation, height, heightUpDown, weight, weightUpDown):
        sql = "SELECT * FROM player"
        where = []
        if team == "미정":
            where.append("team_id IS NULL")
        elif team != "사용안함":
            where.append("team_id = \"" + team + "\"")

        if position == "미정":
            where.append("position IS NULL")
        elif position != "사용안함":
            where.append("position = \"" + position + "\"")

        if nation == "대한민국":
            where.append("nation IS NULL")
        elif nation != "사용안함":
            where.append("nation = \"" + nation + "\"")

        if heightUpDown == "이상":
            where.append("height >= " + height)
        elif heightUpDown == "미만":
            where.append("height < " + height)

        if weightUpDown == "이상":
            where.append("weight >= " + weight)
        elif weightUpDown == "미만":
            where.append("weight < " + weight)

        if len(where) == 0:
            return sql
        else:
            sql = sql + " WHERE"

        for idx, q in enumerate(where):
            if idx == 0:
                sql = sql + " " + q
            else:
                sql = sql + " AND " + q

        return sql

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
        self.setWindowTitle("선수 테이블 검색")
        self.setGeometry(0, 0, 1100, 620)

        # 라벨 설정
        self.teamLabel = QLabel("팀명", self)
        self.teamLabel.move(100, 25)
        self.teamLabel.resize(50, 20)

        self.positionLabel = QLabel("포지션", self)
        self.positionLabel.move(320, 25)
        self.positionLabel.resize(50, 20)

        self.nationLabel = QLabel("출신국", self)
        self.nationLabel.move(550, 25)
        self.nationLabel.resize(50, 20)

        self.heightLabel = QLabel("키", self)
        self.heightLabel.move(100, 50)
        self.heightLabel.resize(50, 20)

        self.weightLabel = QLabel("몸무게", self)
        self.weightLabel.move(550, 50)
        self.weightLabel.resize(50, 20)

        # 콤보박스
        query = DB_Queries()
        positionRows = query.selectPlayerPosition()
        teamRows = query.selectPlayerTeam()
        nationRows = query.selectPlayerNation()

        self.teamComboBox = QComboBox(self)
        self.teamComboBox.move(150, 25)
        self.teamComboBox.resize(100, 20)

        self.positionComboBox = QComboBox(self)
        self.positionComboBox.move(370, 25)
        self.positionComboBox.resize(100, 20)

        self.nationComboBox = QComboBox(self)
        self.nationComboBox.move(600, 25)
        self.nationComboBox.resize(100, 20)

        teamColumnName = list(teamRows[0].keys())[0]
        items = ['없음' if row[teamColumnName] == None else row[teamColumnName] for row in teamRows]
        items.insert(0, "사용안함")
        self.teamComboBox.addItems(items)

        positionColumnName = list(positionRows[0].keys())[0]
        items = ['미정' if row[positionColumnName] == None else row[positionColumnName] for row in positionRows]
        items.insert(0, "사용안함")
        self.positionComboBox.addItems(items)

        nationColumnName = list(nationRows[0].keys())[0]
        items = ['대한민국' if row[nationColumnName] == None else row[nationColumnName] for row in nationRows]
        items.insert(0, "사용안함")
        self.nationComboBox.addItems(items)

        self.teamComboBox.activated.connect(self.comboBox_Activated)
        self.positionComboBox.activated.connect(self.comboBox_Activated)
        self.nationComboBox.activated.connect(self.comboBox_Activated)

        #
        self.heightLine = QLineEdit(self)
        self.heightLine.move(150, 50)
        self.heightLine.resize(100, 20)

        self.weightLine = QLineEdit(self)
        self.weightLine.move(600, 50)
        self.weightLine.resize(100, 20)

        #
        self.btngroup1 = QButtonGroup()
        self.heightRadioBtn1 = QRadioButton("사용안함", self)
        self.heightRadioBtn1.move(260, 50)
        self.heightRadioBtn1.setChecked(True)
        self.heightRadioBtn1.clicked.connect(self.heightRadioBtn_Clicked)

        self.heightRadioBtn2 = QRadioButton("이상", self)
        self.heightRadioBtn2.move(350, 50)
        self.heightRadioBtn2.clicked.connect(self.heightRadioBtn_Clicked)

        self.heightRadioBtn3 = QRadioButton("미만", self)
        self.heightRadioBtn3.move(410, 50)
        self.heightRadioBtn3.clicked.connect(self.heightRadioBtn_Clicked)

        self.btngroup1.addButton(self.heightRadioBtn1)
        self.btngroup1.addButton(self.heightRadioBtn2)
        self.btngroup1.addButton(self.heightRadioBtn3)

        self.btngroup2 = QButtonGroup()
        self.weightRadioBtn1 = QRadioButton("사용안함", self)
        self.weightRadioBtn1.move(260 + 400, 50)
        self.weightRadioBtn1.setChecked(True)
        self.weightRadioBtn1.clicked.connect(self.weightRadioBtn_Clicked)

        self.weightRadioBtn2 = QRadioButton("이상", self)
        self.weightRadioBtn2.move(350 + 400, 50)
        self.weightRadioBtn2.clicked.connect(self.weightRadioBtn_Clicked)

        self.weightRadioBtn3 = QRadioButton("미만", self)
        self.weightRadioBtn3.move(410 + 400, 50)
        self.weightRadioBtn3.clicked.connect(self.weightRadioBtn_Clicked)

        self.btngroup2.addButton(self.weightRadioBtn1)
        self.btngroup2.addButton(self.weightRadioBtn2)
        self.btngroup2.addButton(self.weightRadioBtn3)

        # 푸쉬버튼 설정
        self.searchButton = QPushButton("검색", self)
        self.searchButton.move(900, 50)
        self.searchButton.resize(100, 20)
        self.searchButton.clicked.connect(self.searchButton_Clicked)

        self.resetButton = QPushButton("초기화", self)
        self.resetButton.move(900, 25)
        self.resetButton.resize(100, 20)
        self.resetButton.clicked.connect(self.resetButton_Clicked)


        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        self.tableWidget.move(50, 100)
        self.tableWidget.resize(1000, 500)

    def comboBox_Activated(self):
        self.teamValue = self.teamComboBox.currentText()
        self.positionValue = self.positionComboBox.currentText()
        self.nationValue = self.nationComboBox.currentText()

    def heightRadioBtn_Clicked(self):
        msg = ""
        if self.heightRadioBtn1.isChecked():
            msg = "사용안함"
        elif self.heightRadioBtn2.isChecked():
            msg = "이상"
        else:
            msg = "미만"
        self.heightUpDown = msg

    def weightRadioBtn_Clicked(self):
        msg = ""
        if self.weightRadioBtn1.isChecked():
            msg = "사용안함"
        elif self.weightRadioBtn2.isChecked():
            msg = "이상"
        else:
            msg = "미만"
        self.weightUpDown = msg

    def resetButton_Clicked(self):
        print(self.heightLine.text())
        # DB 검색문 실행
        query = DB_Queries()
        sql = query.makeQuery("사용안함", "DF", "대한민국", "150", "이상", "70", "이상")
        print(sql)
        players = query.selectPlayer(sql)

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

    def searchButton_Clicked(self):
        print(self.heightLine.text())
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

if __name__ == "__main__":
    main()