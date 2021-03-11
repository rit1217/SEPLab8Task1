
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import simple_drawing_window

class simple_drawing_window2( simple_drawing_window ):
    def __init__( self ):
        super.__init__()

    def paintEvent( self, e ):
        p = QPainter()
		p.begin(self)
		
		p.setPen(QColor(255,0,0))
		p.setBrush(QColor(255,0,0))

		p.drawPolygon(
			[QPoint(50,400), QPoint(150,400), QPoint(100,200),]
		)
		
		p.drawPixmap(QRect(400,150,200,200), self.rabbit)
        
		p.end()