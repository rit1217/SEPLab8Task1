from turtle import *
class Disk():
    def __init__(self, x, y, h, w, c):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.c = c

#test
    def newpos(self, x, y):
        self.cleardisk()
        self.posx = x
        self.posy = y
        self.showdisk()

    def cleardisk(self):
        penup()
        goto(self.posx, self.y)
        pendown()
        pencolor("white")
        fillcolor("white")
        begin_fill()
        forward(self.w / 2)
        left(90)
        forward(self.h)
        left(90)
        forward(self.w)
        left(90)
        forward(self.h)
        left(90)
        forward(self.w / 2)
        end_fill()

    def showdisk(self):
        penup()
        goto(self.posx, self.posy)
        pendown()
        fillcolor("blue")

        begin_fill()
        forwardd(self.width / 2)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width / 2)
        end_fill()