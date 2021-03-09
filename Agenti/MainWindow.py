from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QMainWindow
from PySide6.QtGui import QPainter, QPen, QBrush
from PySide6.QtCore import Qt
import sys
 
 
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Gara fra agenti")
        self.setGeometry(350, 200, 700, 700)
        self.show()
 
    def paintEvent(self, e):
        width = self.width()
        height = self.height()
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.lightGray))
 
        painter.drawRect(0.05*width, 0.05*height, 0.9*width, 0.9*height)
 

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())