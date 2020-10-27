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

        buttonNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        positions = [(row, col) for row in range(3) for col in range(3)]

        for name, position in zip(buttonNames, positions):          # zip function
            button = QPushButton(name)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(button, *position)                     # * operator, 즉 layout.addWidget(button, row, col)

#########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()