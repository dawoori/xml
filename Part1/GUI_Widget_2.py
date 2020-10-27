import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):          # QWidget > QMainWindow 클래스의 서브클래스
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("LineEdit과 Button 예제")
        self.setGeometry(0, 0, 400, 120)

        # 스테이터스바 설정 (QMainWindow 객체)
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # 레이블과 라인에디트 설정
        self.label = QLabel("이름: ", self)
        self.label.move(50, 20)
        self.label.resize(50, 20)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(100, 20)
        self.lineEdit.resize(200, 20)
        self.lineEdit.textChanged.connect(self.lineEdit_TextChanged)
        self.lineEdit.returnPressed.connect(self.lineEdit_ReturnPressed)

        # 푸시버튼 설정
        self.btnSave = QPushButton("저장", self)
        self.btnSave.move(50, 50)
        self.btnSave.resize(self.btnSave.sizeHint())
        self.btnSave.setToolTip("Save")
        self.btnSave.clicked.connect(self.btnSave_Clicked)

        self.btnClear = QPushButton("초기화", self)
        self.btnClear.move(150, 50)
        self.btnClear.resize(self.btnClear.sizeHint())
        self.btnClear.setToolTip("Clear")
        self.btnClear.clicked.connect(self.btnClear_Clicked)

        self.btnQuit = QPushButton("닫기", self)
        self.btnQuit.move(250, 50)
        self.btnQuit.resize(self.btnQuit.sizeHint())
        self.btnQuit.setToolTip("Quit")
        self.btnQuit.clicked.connect(self.btnQuit_Clicked)

    def lineEdit_TextChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

    def lineEdit_ReturnPressed(self):
        self.statusBar.showMessage("이름을 입력하세요.")

    def btnSave_Clicked(self):
        msg = "저장하시겠습니까?"
        msg += "\n이름 : " + self.lineEdit.text()
        buttonReply = QMessageBox.question(self, "저장 확인", msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                                                                        # "YES", "NO" push button 제공

        if buttonReply == QMessageBox.Yes:
            QMessageBox.about(self, "저장", "저장되었습니다.")             # "OK" push button 제공
            self.statusBar.showMessage("저장되었습니다.")
        if buttonReply == QMessageBox.No:
            QMessageBox.about(self, "저장 취소", "저장되지 않았습니다.")
            self.statusBar.showMessage("저장되지 않았습니다.")

    def btnClear_Clicked(self):
        self.lineEdit.clear()
        self.statusBar.showMessage("초기화되었습니다.")

    def btnQuit_Clicked(self):
        sys.exit()                  # 윈도우를 종료함.

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()                     # 윈도우의 event loop에 들어감.