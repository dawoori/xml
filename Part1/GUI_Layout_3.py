import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("중첩 Layout 예제")
        self.setGeometry(0, 0, 500, 200)

        # 필요한 모든 위젯 생성
        checkBox1 = QCheckBox("GK")
        checkBox2 = QCheckBox("DF")
        checkBox3 = QCheckBox("MF")
        checkBox4 = QCheckBox("FW")
        checkBox5 = QCheckBox("미정")

        groupBox = QGroupBox("포지션")

        tableWidget = QTableWidget(100, 8)
        tableWidget.setHorizontalHeaderLabels(["소속팀", "이름", "생일", "포지션", "백넘버", "출신국", "키", "몸무게"])
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        # 레이아웃의 생성, 위젯 연결, 레이아웃 설정
        leftInnerLayout = QVBoxLayout()
        leftInnerLayout.addWidget(checkBox1)
        leftInnerLayout.addWidget(checkBox2)
        leftInnerLayout.addWidget(checkBox3)
        leftInnerLayout.addWidget(checkBox4)
        leftInnerLayout.addWidget(checkBox5)

        groupBox.setLayout(leftInnerLayout)

        # 레이아웃의 생성, 위젯 연결
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(groupBox)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(tableWidget)

        # 레이아웃의 생성, 레이아웃 연결 (중첩 레이아웃), 레이아웃 설정
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)

        # 메인 윈도우에 레이아웃 설정
        self.setLayout(layout)

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()