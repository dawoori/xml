import pymysql
from PyQt5.QtWidgets import *
import sys, datetime
import csv
import json
import xml.etree.ElementTree as ET

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
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의
    def selectPlayerTeam(self):
        sql = "SELECT DISTINCT team_id FROM player"
        params = ()

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

    def selectTeam(self):
        sql = "SELECT team_id, team_name FROM team"
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

#########################################

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        # 윈도우 설정
        self.setWindowTitle("선수 테이블 검색")
        self.setGeometry(0, 0, 1100, 720)

        # 라벨 설정
        self.teamLabel = QLabel("팀명", self)
        self.teamLabel.move(80, 25)
        self.teamLabel.resize(50, 20)

        self.positionLabel = QLabel("포지션", self)
        self.positionLabel.move(300, 25)
        self.positionLabel.resize(50, 20)

        self.nationLabel = QLabel("출신국", self)
        self.nationLabel.move(510, 25)
        self.nationLabel.resize(50, 20)

        self.heightLabel = QLabel("키", self)
        self.heightLabel.move(80, 50)
        self.heightLabel.resize(50, 20)

        self.weightLabel = QLabel("몸무게", self)
        self.weightLabel.move(510, 50)
        self.weightLabel.resize(50, 20)

        # 콤보박스
        query = DB_Queries()
        positionRows = query.selectPlayerPosition()
        teamRows = query.selectPlayerTeam()
        nationRows = query.selectPlayerNation()
        self.teams = query.selectTeam()

        self.teamComboBox = QComboBox(self)
        self.teamComboBox.move(130, 25)
        self.teamComboBox.resize(100, 20)

        self.positionComboBox = QComboBox(self)
        self.positionComboBox.move(350, 25)
        self.positionComboBox.resize(100, 20)

        self.nationComboBox = QComboBox(self)
        self.nationComboBox.move(560, 25)
        self.nationComboBox.resize(100, 20)

        teamColumnName = list(teamRows[0].keys())[0]
        items = ['없음' if row[teamColumnName] == None else self.teamNameId(row[teamColumnName]) for row in teamRows]
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

        #
        self.heightLine = QLineEdit(self)
        self.heightLine.move(130, 50)
        self.heightLine.resize(100, 20)

        self.weightLine = QLineEdit(self)
        self.weightLine.move(560, 50)
        self.weightLine.resize(100, 20)

        #
        self.btngroup1 = QButtonGroup()
        self.heightRadioBtn1 = QRadioButton("사용안함", self)
        self.heightRadioBtn1.move(240, 50)
        self.heightRadioBtn1.setChecked(True)

        self.heightRadioBtn2 = QRadioButton("이상", self)
        self.heightRadioBtn2.move(330, 50)

        self.heightRadioBtn3 = QRadioButton("미만", self)
        self.heightRadioBtn3.move(390, 50)

        self.btngroup1.addButton(self.heightRadioBtn1)
        self.btngroup1.addButton(self.heightRadioBtn2)
        self.btngroup1.addButton(self.heightRadioBtn3)

        self.btngroup2 = QButtonGroup()
        self.weightRadioBtn1 = QRadioButton("사용안함", self)
        self.weightRadioBtn1.move(670, 50)
        self.weightRadioBtn1.setChecked(True)

        self.weightRadioBtn2 = QRadioButton("이상", self)
        self.weightRadioBtn2.move(760, 50)

        self.weightRadioBtn3 = QRadioButton("미만", self)
        self.weightRadioBtn3.move(820, 50)

        self.btngroup2.addButton(self.weightRadioBtn1)
        self.btngroup2.addButton(self.weightRadioBtn2)
        self.btngroup2.addButton(self.weightRadioBtn3)

        self.btngroup = QButtonGroup()
        self.CSVRadioBtn = QRadioButton("CSV", self)
        self.CSVRadioBtn.move(670, 630)
        self.CSVRadioBtn.setChecked(True)

        self.JSONRadioBtn = QRadioButton("JSON", self)
        self.JSONRadioBtn.move(740, 630)

        self.XMLRadioBtn = QRadioButton("XML", self)
        self.XMLRadioBtn.move(820, 630)

        self.btngroup.addButton(self.CSVRadioBtn)
        self.btngroup.addButton(self.JSONRadioBtn)
        self.btngroup.addButton(self.XMLRadioBtn)

        # 푸쉬버튼 설정
        self.searchButton = QPushButton("검색", self)
        self.searchButton.move(900, 50)
        self.searchButton.resize(100, 20)
        self.searchButton.clicked.connect(self.searchButton_Clicked)

        self.resetButton = QPushButton("초기화", self)
        self.resetButton.move(900, 25)
        self.resetButton.resize(100, 20)
        self.resetButton.clicked.connect(self.resetButton_Clicked)

        self.resetButton = QPushButton("저장", self)
        self.resetButton.move(900, 630)
        self.resetButton.resize(100, 20)
        self.resetButton.clicked.connect(self.saveButton_Clicked)

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        self.tableWidget.move(50, 100)
        self.tableWidget.resize(1000, 500)

    def resetButton_Clicked(self):
        self.teamComboBox.setCurrentIndex(0)
        self.nationComboBox.setCurrentIndex(0)
        self.positionComboBox.setCurrentIndex(0)
        self.heightRadioBtn1.setChecked(True)
        self.weightRadioBtn1.setChecked(True)
        self.heightLine.setText("")
        self.weightLine.setText("")

    def searchButton_Clicked(self):
        self.teamValue = self.teamNameId(self.teamComboBox.currentText())
        self.positionValue = self.positionComboBox.currentText()
        self.nationValue = self.nationComboBox.currentText()

        self.heightValue = self.heightLine.text()
        if self.heightRadioBtn1.isChecked():
            self.heightUpDown = "사용안함"
        elif self.heightRadioBtn2.isChecked():
            self.heightUpDown = "이상"
        else:
            self.heightUpDown = "미만"

        self.weightValue = self.weightLine.text()
        if self.weightRadioBtn1.isChecked():
            self.weightUpDown = "사용안함"
        elif self.weightRadioBtn2.isChecked():
            self.weightUpDown = "이상"
        else:
            self.weightUpDown = "미만"

        # DB 검색문 실행
        query = DB_Queries()
        sql = query.makeQuery(self.teamValue, self.positionValue, self.nationValue, self.heightValue, self.heightUpDown, self.weightValue, self.weightUpDown)
        players = query.selectPlayer(sql)
        self.players = players

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

                if v == None:
                    continue
                elif isinstance(v, datetime.date):
                    item = QTableWidgetItem(v.strftime('%Y-%m-%d'))
                else:
                    item = QTableWidgetItem(str(v))

                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def saveButton_Clicked(self):
        if self.CSVRadioBtn.isChecked():
            self.writeCSV()
        elif self.JSONRadioBtn.isChecked():
            self.writeJSON()
        else:
            self.writeXML()

    def writeCSV(self):
        players = self.players
        with open('player.csv', 'w', encoding='utf-8', newline='') as f:
            wr = csv.writer(f)

            columnNames = list(players[0].keys())

            wr.writerow(columnNames)
            for rowIDX in range(len(players)):
                row = list(players[rowIDX].values())
                wr.writerow(row)

    def writeJSON(self):
        players = self.players

        for player in players:
            for k, v in player.items():
                if isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')

        newDict = dict(player = players)

        with open('player.json', 'w', encoding='utf-8') as f:
            json.dump(newDict, f, ensure_ascii=False)

    def writeXML(self):
        players = self.players
        for player in players:
            for k, v in player.items():
                if isinstance(v, datetime.date):
                    player[k] = v.strftime('%Y-%m-%d')

        newDict = dict(player = players)

        tableName = list(newDict.keys())[0]
        tableRows = list(newDict.values())[0]

        rootElement = ET.Element('Table')
        rootElement.attrib['name'] = tableName

        for row in tableRows:
            rowElement = ET.Element('Row')
            rootElement.append(rowElement)

            for columnName in list(row.keys()):
                if row[columnName] == None:
                    rowElement.attrib[columnName] = ''
                else:
                    rowElement.attrib[columnName] = row[columnName]

                if type(row[columnName]) == int:
                    rowElement.attrib[columnName] = str(row[columnName])

        ET.ElementTree(rootElement).write('player.xml', encoding='utf-8', xml_declaration=True)

    def teamNameId(self, teamV):
        teams = self.teams
        for team in teams:
            if team['team_id'] == teamV:
                return team['team_name']

        for team in teams:
            if team['team_name'] == teamV:
                return team['team_id']

        return teamV


#########################################

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()