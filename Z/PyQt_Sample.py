import sys

from PyQt6 import  QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("PyQt Sample")
        self.setGeometry(300, 300, 400, 400)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
