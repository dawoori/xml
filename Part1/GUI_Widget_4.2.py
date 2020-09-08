import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):          # QWidget 클래스의 서브클래스
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("TableWidget 예제")
        self.setGeometry(0, 0, 400, 220)

        players = {
            'PLAYER_ID': ['2020001', '2020002', '2020003'],
            'PLAYER_NAME': ['손홍민', '호날두', '메시'],
            'TEAM_ID': ['K01', 'K02', 'K03'],
            'POSITION': ['FW', 'FW', 'FW']
        }
        columnNames = list(players.keys())
        # ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'POSITION']

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        self.tableWidget.move(50, 50)
        self.tableWidget.resize(300, 120)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setHorizontalHeaderLabels(columnNames)

        for k, v in players.items():
            columnIDX = columnNames.index(k)    # 테이블 위젯의 column index 할당

            for rowIDX, val in enumerate(v):    # 테이블 위젯의 row index 할당
                item = QTableWidgetItem(val)    # QTableWidgetItem 객체 생성
                if columnIDX == 1:
                    item.setTextAlignment(Qt.AlignRight)
                self.tableWidget.setItem(rowIDX, columnIDX, item)    # QTableWidget 객체에 QTableWidgetItem 객체를 할당

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()