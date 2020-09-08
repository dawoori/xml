import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("QInputDialog 예제")
        self.setGeometry(0, 0, 300, 300)

        # 필요한 모든 위젯 생성
        self.pushButton1 = QPushButton("Input number")
        self.pushButton1.clicked.connect(self.pushButton1_Clicked)

        self.pushButton2 = QPushButton("Input position")
        self.pushButton2.clicked.connect(self.pushButton2_Clicked)

        self.label = QLabel()

        # 레이아웃 생성, 위젯 연결, 레이아웃 설정
        layout = QVBoxLayout()

        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButton1_Clicked(self):
        text, ok = QInputDialog.getInt(self, "나이 입력", "나이를 입력하세요.")
        print(text, ok)

        if ok:
            self.label.setText(str(text))

    def pushButton2_Clicked(self):
        items = ("GK", "DF", "MF", "FW", "미정")
        item, ok = QInputDialog.getItem(self, "포지션 선택", "포지션을 선택하세요.", items, 0, False)
        if ok and item:
            self.label.setText(item)

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()