import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("QVBoxLayout 예제")
        self.setGeometry(0, 0, 300, 300)

        # 위젯 설정 (move()와 resize()를 사용하지 않음.)
        self.textEdit = QTextEdit()
        self.btnSave = QPushButton("저장")
        self.btnClear = QPushButton("초기화")
        self.btnQuit = QPushButton("닫기")

        # 레이아웃의 생성, 위젯 연결, 레이아웃 설정
        layout = QVBoxLayout()

        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnSave)
        layout.addWidget(self.btnClear)
        layout.addWidget(self.btnQuit)

        # 레이아웃 설정
        self.setLayout(layout)

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()