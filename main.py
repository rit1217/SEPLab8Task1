from simple_drawing_window2 import *

def main():
	app = QApplication(sys.argv)

	w = simple_drawing_window2()
    
	w.show()

	return app.exec_()
	#rabbit

if __name__ == "__main__":
	sys.exit(main())