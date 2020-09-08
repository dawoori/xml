import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):          # QWidget 클래스의 서브클래스
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("TableWidget 예제")
        self.setGeometry(0, 0, 400, 220)

        players = [
            {'PLAYER_ID':'2020001', 'PLAYER_NAME':'손홍민', 'TEAM_ID':'K01', 'POSITION':'FW'},
            {'PLAYER_ID':'2020002', 'PLAYER_NAME':'호날두', 'TEAM_ID':'K02', 'POSITION':'FW'},
            {'PLAYER_ID':'2020003', 'PLAYER_NAME':'메시', 'TEAM_ID':'K03', 'POSITION':'FW'}
        ]
        columnNames = list(players[0].keys())
        # ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'POSITION']

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self)   # QTableWidget 객체 생성
        self.tableWidget.move(50, 50)
        self.tableWidget.resize(300, 120)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setHorizontalHeaderLabels(columnNames)

        for rowIDX in range(len(players)):          # 테이블 위젯의 row index 할당
            player = players[rowIDX]

            for k, v in player.items():
                columnIDX = columnNames.index(k)    # 테이블 위젯의 column index 할당
                item = QTableWidgetItem(v)          # QTableWidgetItem 객체 생성
                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()