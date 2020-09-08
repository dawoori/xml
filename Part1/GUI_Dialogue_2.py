import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("QFileDialog 예제")
        self.setGeometry(0, 0, 300, 300)

        # 필요한 모든 위젯 생성
        self.pushButton = QPushButton("File Open")
        self.pushButton.clicked.connect(self.pushButton_Clicked)
        self.label = QLabel()

        # 레이아웃 생성, 위젯 연결, 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def pushButton_Clicked(self):
        fname = QFileDialog.getOpenFileName(self)   # 튜플 타입
        self.label.setText(fname[0])

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()