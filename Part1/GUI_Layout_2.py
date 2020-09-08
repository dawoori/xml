import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("QGridLayout 예제")
        self.setGeometry(0, 0, 300, 100)

        # 위젯 설정 (move()와 resize()를 사용하지 않음.)
        self.label1 = QLabel("아이디: ")
        self.label2 = QLabel("암  호: ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton= QPushButton("로그인")

        # 레이아웃의 생성, 위젯 연결, 레이아웃 설정
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton, 0, 2)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        self.setLayout(layout)

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()