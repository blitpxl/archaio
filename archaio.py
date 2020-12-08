"""Archaio v2.6a by Negated (Kevin Putra)"""

from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
import sys
import os
import time
from tkinter import Tk, filedialog, messagebox

if not os.path.isfile('unit/unit.txt'):
    root = Tk()
    root.withdraw()
    messagebox.showerror("Error: Missing file", "Couldn't open Archaio, The file (unit/unit.txt) is missing ")
    sys.exit()
else:
    pass


class CustomSize(QWidget):
    def __init__(self):
        super(CustomSize, self).__init__()
        self.initCustomSizeWindow()
        self.setFixedWidth(250)
        self.setFixedHeight(150)
        self.setWindowTitle("Custom Size")
        self.setWindowIcon(QIcon('Icon/aioicon.png'))

    def initCustomSizeWindow(self):
        self.customSizelbl = QtWidgets.QLabel(self)
        self.customSizelbl.setText("Enter Custom value (in Kb)")
        self.customSizelbl.move(25, 10)

        self.customSize = QtWidgets.QLineEdit(self)
        self.customSize.setGeometry(25, 25, 200, 25)

        self.exampleSize = QtWidgets.QLabel(self)
        self.exampleSize.setText("Examples:"
                                 "\n10MB = 102400kb"
                                 "\n1GB = 1024000kb"
                                 "\n5GB = 5120000kb"
                                 "\n10GB = 10240000kb")
        self.exampleSize.move(25, 50)

        self.okbutton = QtWidgets.QPushButton(self)
        self.okbutton.setText("OK")
        self.okbutton.move(85, 120)
        self.okbutton.clicked.connect(self.ok)

    def ok(self):
        if self.customSize.text() == "":
            warn = QMessageBox(self)
            warn.setText("Custom size field empty, please fill to continue")
            warn.setIcon(QMessageBox.Warning)
            warn.setWindowTitle("Error")
            warn.setWindowIcon(QIcon('Icon/aioicon.png'))
            warn.exec_()
        else:
            self.close()


class MainWindow(QMainWindow):  # Main Window Class
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.setFixedHeight(300)
        self.setFixedWidth(400)
        self.setWindowTitle("Archaio v2.6a")
        self.setWindowIcon(QIcon('Icon/aioicon.png'))
        self.customsizewindow = CustomSize()

    def initUI(self):
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(25, 25, 350, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.directoryLabel = QtWidgets.QLabel(self)
        self.directoryLabel.setText("Select the file output directory:")
        self.directoryLabel.setGeometry(100, 55, 200, 25)

        self.selectedDirectory = QtWidgets.QLineEdit(self)
        self.selectedDirectory.setGeometry(100, 80, 175, 25)

        self.selectDirectory = QtWidgets.QPushButton(self)
        self.selectDirectory.setGeometry(275, 80, 25, 25)
        self.selectDirectory.setText("...")
        self.selectDirectory.setToolTip("Browse Directories")
        self.selectDirectory.clicked.connect(self.getDirectory)

        self.sizeLabel = QtWidgets.QLabel(self)
        self.sizeLabel.setText("File Size:")
        self.sizeLabel.setGeometry(100, 145, 200, 25)

        self.sizeList = ['10MB', '50MB', '100MB', '500MB', '1GB', '5GB', '10GB', '20GB', 'Custom Size']
        self.selectSize = QtWidgets.QComboBox(self)
        self.selectSize.setGeometry(100, 170, 200, 30)
        self.selectSize.setToolTip("Select output file size")
        self.selectSize.currentTextChanged.connect(self.checkCustomSize)
        self.selectSize.addItems(self.sizeList)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Generate File")
        self.btn.move(150, 260)
        self.btn.clicked.connect(self.createFile)

    def checkCustomSize(self):
        if self.selectSize.currentText() == "Custom Size":
            self.customsizewindow.show()
        else:
            pass

    def getDirectory(self):  # function to get the file output directory
        root = Tk()
        root.withdraw()
        self.directory = filedialog.askdirectory()
        self.selectedDirectory.setText(self.directory)

    def createFile(self):  # function to create/process the file
        if self.selectedDirectory.text() == "":  # if no directory selected, show warning
            self.warning_no_dir = QMessageBox(self)
            self.warning_no_dir.setText("Select directory to proceed")
            self.warning_no_dir.setIcon(QMessageBox.Warning)
            self.warning_no_dir.setWindowTitle("No directory selected")
            self.warning_no_dir.setWindowIcon(QIcon('Icon/aioicon.png'))
            self.warning_no_dir.exec_()
        elif not os.path.isdir(self.selectedDirectory.text()):  # if the selected directory does not exist, show warning
            self.warning_invalid_dir = QMessageBox(self)
            self.warning_invalid_dir.setText(
                "Invalid directory, no such directory as: " + self.selectedDirectory.text())
            self.warning_invalid_dir.setIcon(QMessageBox.Warning)
            self.warning_invalid_dir.setWindowTitle("Invalid Directory")
            self.warning_invalid_dir.setWindowIcon(QIcon('Icon/aioicon.png'))
            self.warning_invalid_dir.exec_()
        else:
            self.info = QMessageBox(self)
            self.info.setText("Be aware that the application might freeze"
                              "\nwhen creating the file, this is normal, do not close the app.")
            self.info.setIcon(QMessageBox.Information)
            self.info.setWindowTitle("Archaio")
            self.info.exec_()

            self.setWindowTitle("Archaio - Generating File (Do not close)")

            unit_text = open('unit/unit.txt', 'r')
            unit = unit_text.read()
            y = 0

            if self.selectSize.currentText() == "10MB":  # changing the value of the variable-
                threshold = int(10240)  # -"threshold" to match the selected size
                size = "10MB"
            elif self.selectSize.currentText() == "50MB":
                threshold = int(51200)
                size = "50MB"
            elif self.selectSize.currentText() == "100MB":
                threshold = int(102400)
                size = "100MB"
            elif self.selectSize.currentText() == "500MB":
                threshold = 512000
                size = "500MB"
            elif self.selectSize.currentText() == "1GB":
                threshold = int(1024000)
                size = "1GB"
            elif self.selectSize.currentText() == "5GB":
                threshold = int(5120000)
                size = "5GB"
            elif self.selectSize.currentText() == "10GB":
                threshold = int(10240000)
                size = "10GB"
            elif self.selectSize.currentText() == "Custom Size":
                threshold = int(self.customsizewindow.customSize.text())
                size = self.customsizewindow.customSize.text() + "KB"
            else:
                threshold = int(20480000)
                size = "20GB"

            sys.stdout = open(self.selectedDirectory.text() + '/Archaio' + size + 'File.aio', 'w+')
            tl_start = time.perf_counter()
            while y < int(threshold):
                print(unit, end='')
                y += 1
            tl_stop = time.perf_counter()
            self.finished_message = QMessageBox()
            self.finished_message.setText("File Successfully Generated, time taken: " + str(tl_stop - tl_start))
            self.finished_message.setIcon(QMessageBox.Information)
            self.finished_message.setWindowTitle("Archaio")
            self.finished_message.setWindowIcon(QIcon('Icon/aioicon.png'))
            self.finished_message.exec_()

            self.setWindowTitle("Archaio v2.6a")


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())


window()
sys.stdout.close()
