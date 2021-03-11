import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from simple_drawing_window import *
class simple_drawing_window3( simple_drawing_window ):
	def __init__(self):
		super().__init__()

	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		
	
		p.setPen(QColor(255,222,0))
		p.setBrush(QColor(255,222,0))
		p.drawEllipse(50,150, 200,200)

		
		
		p.drawPixmap(QRect(400,150,200,200), self.rabbit)
        
		p.end()
