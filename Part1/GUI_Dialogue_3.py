import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("메인 윈도우와 서브 윈도우의 상호작용 에제")

        self.pushButton = QPushButton("Sign In")
        self.pushButton.clicked.connect(self.pushButton_Clicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButton_Clicked(self):
        dialogue = LogInSubwindow()     # QDialog 클래스의 subwindow 객체 생성
        dialogue.exec_()                # subwindow 객체를 실행함. (다이얼로그 창을 modal 형태로 출력함)
                                        # subwindow 객체가 닫히면 계속 진행됨.
        id = dialogue.id
        password = dialogue.password
        self.label.setText("id: %s password: %s" % (id, password))

class LogInSubwindow(QDialog):      # QDialog 클래스의 서브클래스
    def __init__(self):
        super().__init__()
        self.setupUI()

        # 입력을 저장할 변수 정의
        self.id = None
        self.password = None

    def setupUI(self):
        self.setGeometry(0, 100, 300, 100)
        self.setWindowTitle("QGridLayout 예제")

        # 위젯 설정 (move()와 resize()를 사용하지 않음.)
        self.label1 = QLabel("아이디: ")
        self.label2 = QLabel("암  호: ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton = QPushButton("로그인")
        self.pushButton.clicked.connect(self.pushButton_Clicked)

        # 레이아웃의 생성, 위젯 연결, 레이아웃 설정
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton, 0, 2)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        self.setLayout(layout)

    def pushButton_Clicked(self):
        self.id = self.lineEdit1.text()         # 입력받은 값을 변수에 저장
        self.password = self.lineEdit2.text()   # 입력받은 값을 변수에 저장
        self.close()

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()