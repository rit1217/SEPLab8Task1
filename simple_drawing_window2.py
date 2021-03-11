
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import simple_drawing_window

class Simple_drawing_window2( simple_drawing_window ):
    def __init__( self ):
        super.__init__()

    def paintEvent( self, e ):