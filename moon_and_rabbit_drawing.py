import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class simple_drawing_window(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.setWindowTitle("Simple Drawing")
        
		self.rabbit = QPixmap("image/rabbit.png")
        
	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		

		p.setPen(QColor((255,255,0)))
		p.setBrush(QColor((255,255,0)))
		p.drawArc(50,200,150,50,0,16*360)
		
		p.drawPixmap(QRect(400,150,200,200), self.rabbit)
        
		p.end()

def main():
	app = QApplication(sys.argv)

	w = simple_drawing_window()
    
	w.show()

	return app.exec_()

if __name__ == "__main__":
	sys.exit(main())