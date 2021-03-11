from simple_drawing_window2 import *
from Simple_drawing_window1 import *

def main():
    app = QApplication(sys.argv)

    w1 = simple_drawing_window1()
    w2 = simple_drawing_window2()
    
    w1.show()
    w2.show()

    return app.exec_()
    #rabbit

if __name__ == "__main__":
    sys.exit(main())