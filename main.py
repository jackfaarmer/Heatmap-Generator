## Main module for AI Heatmap Generation
##
## Author: Jack Farmer


from gui import WindowSystem
from PySide6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = WindowSystem()
    widget.resize(500, 500)
    widget.show()
    if widget.running == True:
        widget.facetrack()
    
    sys.exit(app.exec())
