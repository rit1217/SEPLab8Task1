import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtPrintSupport import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("A simple paint program")
        self.resize(600, 500)

        self.label = QLabel(self)
        self.label.setText("Drag the mouse to draw")
        self.label.move(240, 400)

        self.points = []
        self.button = QPushButton(self)
        self.button.setText("Clear")
        self.button.clicked.connect(self.clear)
        self.button.move(260, 450)
 #oioib
    
    def clear( self ):
        self.points.clear()
    
<<<<<<< HEAD
    def mouseMoveEvent(self,event):
        self.points.append(event.pos())
    
    def paint(self, e):
=======
    def mouseMoveEvent(self):
        pass

    def paintEvent(self, e):
>>>>>>> 765cbb1575995cda932411bbf7b5c5f93abd752a
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 255))
        p.setBrush(QColor(0, 0, 255))
        for point in self.points:
            p.drawPie(point.x(), point.y(), 10, 10, 0, 180 * 32)
        p.end()

        self.update()

        
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())