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

        layout = QGridLayout()
        self.setLayout(layout)

        buttonNames = ['1', '2', '3','4', '5', '6', '7', '8', '9']

        positions = [(r, c) for r in range(3) for c in range(3)]

        for name, position in zip(buttonNames, positions):
            button = QPushButton(name)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(button, *position)

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()