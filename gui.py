## GUI module for AI Heatmap Generation
##
## Author: Jack Farmer
import sys
import cv2
from threading import Thread
from PySide6 import QtCore, QtWidgets, QtGui
from stats import getStats

class WindowSystem(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Heatmap Generator")

        self.running = False
        self.alreadyRun = False ## cannot launch thread twice, must block user from re-launching
        self.xvals = []
        self.areaSize = 0
        self.thethread = Thread(target=self.facetrack)

        self.button1 = QtWidgets.QPushButton("Start Capture")
        self.button2 = QtWidgets.QPushButton("Stop Capture")
        self.button3 = QtWidgets.QPushButton("Select File")
        self.button4 = QtWidgets.QPushButton("Exit")
        self.display = QtWidgets.QLabel("Please select an option below",
                                     alignment=QtCore.Qt.AlignCenter)
        self.display.setFont(QtGui.QFont('Helvetica', 25))

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.display)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)

        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)
        self.button3.clicked.connect(self.save)
        self.button4.clicked.connect(self.exit)

        if self.running == True: self.facetrack()

    def facetrack(self):
        width = 0

        capture = cv2.VideoCapture(0)
        if capture.isOpened():
            width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)

        # for frame division/calculation

        while self.running == True:
            self.display.setText("Capturing . . .")
            
            read, frame = capture.read()

            # get width of frame for area calculations
            self.areaSize = width / 5

            if not read: break

            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faceDetect = cv2.CascadeClassifier("facedetect.xml")
            
            detected = faceDetect.detectMultiScale(grayscale, 1.1, 4)

            for (xval,yval,width,height) in detected:
                # store data for later
                self.xvals.append(xval + (width // 2))

        capture.release()
        cv2.destroyAllWindows()


    @QtCore.Slot()
    def start(self):
        if (self.alreadyRun == True):
            msgbox = QtWidgets.QMessageBox()
            msgbox.setWindowTitle("Alert")
            msgbox.setText("Heatmap has already run. Please exit the program and try again")
            x = msgbox.exec_()
            return
        self.resize(500, 500)
        self.display.setText("Initializing...")
        self.thethread.start()
        self.running = True
        self.alreadyRun = True
        print("is thread running:", self.thethread.is_alive())

        
    @QtCore.Slot()
    def stop(self):
        if self.running == False: 
            msgbox = QtWidgets.QMessageBox()
            msgbox.setWindowTitle("Alert")
            msgbox.setText("No capture is currently running!")
            x = msgbox.exec_()
        else:
            self.running = False
            self.thethread.join()
            self.display.setText("Calculating Heatmap . . .")
            print("area size: ", self.areaSize)
            self.display.setText("Capture complete!")
            getStats(self.xvals, 256)
        
    @QtCore.Slot()
    def save(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "/Recent/","Images (*.png *.xpm *.jpg *.bmp);;All Files (*.*)", options=options)
        if fileName:
            image = QtGui.QImage(fileName)
            self.display.setPixmap(QtGui.QPixmap.fromImage(image))
            self.resize(500, 500)

    @QtCore.Slot()
    def exit(self):
        if (self.running == True):
            self.running = False
            self.thethread.join()
        sys.exit()

