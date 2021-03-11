from turtle import *

class Pole:
    def __init__(self, name, posx, posy):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.stack = []
        self.top_position = 0
        self.thickness = 30
        self.length = 210

    def showpole(self):
        pass

    def pushdisk(self, disk):
        self.stack.append(disk)
        disk.newpos(self.posx, self.posy + disk.height * len(self.stack))

    def popdisk(self):
        disk = self.stack.pop(len(self.stack) - 1)
        disk.newpos(self.posx, self.length + 50)
        self.showpole()
        return disk