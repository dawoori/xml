import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):          # QWidget > QMainWindow 클래스의 서브클래스
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("RadioButton 예제")
        self.setGeometry(0, 0, 400, 150)

        # 스테이터스바 설정
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # 그룹박스 설정
        self.GroupBox = QGroupBox(self)
        self.GroupBox.move(50, 20)
        self.GroupBox.resize(230, 50)

        # 라디오 버튼 설정
        self.radioBtn1 = QRadioButton("사용안함", self)
        self.radioBtn1.move(60, 40)
        self.radioBtn1.setChecked(True)
        self.radioBtn1.clicked.connect(self.radioBtn_Clicked)

        self.radioBtn2 = QRadioButton("이상", self)
        self.radioBtn2.move(150, 40)
        self.radioBtn2.clicked.connect(self.radioBtn_Clicked)

        self.radioBtn3 = QRadioButton("미만", self)
        self.radioBtn3.move(210, 40)
        self.radioBtn3.clicked.connect(self.radioBtn_Clicked)

    def radioBtn_Clicked(self):
        msg = ""

        if self.radioBtn1.isChecked():
            msg = "사과"
        elif self.radioBtn2.isChecked():
            msg = "딸기"
        else:
            msg = "곰"

        QMessageBox.about(self, "선택된 항목", msg + " 선택됨")
        self.statusBar.showMessage(msg + " 선택됨")

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()