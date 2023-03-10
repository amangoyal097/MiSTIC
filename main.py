from PyQt5 import QtGui, QtWidgets
from driver import mistic
from find_neighbors import shp_neighbors
from coreRegion import core_analysis

import sys
import design
import os


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    InputFile = ""
    OutputFile = ""
    NeighborFile = ""

    areaOfInt = ""
    spUnits = ""
    timeUnits = ""
    startYear = ""
    endYear = ""

    itf = ""
    minSupport = ""
    crRadius = ""
    maxPrune = ""
    minFreq = ""

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        self.btn_BrowseIn.clicked.connect(self.browse_In)
        self.btn_BrowseOut.clicked.connect(self.browse_Out)
        self.btn_BrowseNbh.clicked.connect(self.browse_Nbh)
        self.btn_Next1.clicked.connect(self.next1)
        self.btn_Next2.clicked.connect(self.next2)
        self.btn_Next3.clicked.connect(self.next3)
        self.btn_Back1.clicked.connect(self.back1)
        self.btn_Back2.clicked.connect(self.back2)
        self.btn_Back3.clicked.connect(self.back3)
        self.btn_Start.clicked.connect(self.start_mistic)

        self.p1blank1.hide()
        self.p1blank2.hide()
        self.p1blank3.hide()
        self.p1blank4.hide()
        self.p1blank5.hide()

        self.p4blank1.hide()
        self.p4blank2.hide()
        self.p4blank3.hide()
        self.p4blank4.hide()

        self.radio_Manual.setChecked(True)
        self.radio_Cc.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)

        # self.btnExit.clicked.connect(self.exit)

    def btn_State(self, b):
        if b.text() == "Shapefile" and b.isChecked():
            print("Shapefile")
        if b.text() == "Point Data" and b.isChecked():
            print("Point Data")
        if b.text() == "Manual" and b.isChecked():
            print("Manual")

    def browse_In(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a folder")
        # print directory
        if directory:
            self.le_InputFile.setText(directory)
            self.InputFile = str(directory)

    def browse_Out(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a folder")
        # print directory
        if directory:
            self.le_OutputFile.setText(directory)
            self.OutputFile = str(directory)

    def browse_Nbh(self):
        # Change to File Chooser
        # directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a folder")

        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Pick a file")[0]
        print(filename)
        if filename:
            self.le_SpNeighbor.setText(filename)
            self.NeighborFile = str(filename)

    def next1(self):
        self.grab_parameters()

    def next2(self):
        self.stackedWidget.setCurrentIndex(2)

    def next3(self):
        """Run the advanced analysis part"""

        self.itf = self.le_itf.text()
        self.minSupport = self.le_MinSup.text()
        self.crRadius = self.le_CrRadius.text()
        self.maxPrune = self.le_MaxPrune.text()
        self.minFreq = self.le_MinFreq.text()

        show = 1
        if not self.minSupport:
            self.p4blank1.show()
            show = 0
        else:
            self.p4blank1.hide()
        if not self.maxPrune:
            self.p4blank2.show()
            show = 0
        else:
            self.p4blank2.hide()
        if not self.minFreq:
            self.p4blank3.show()
            show = 0
        else:
            self.p4blank3.hide()

        if self.radio_Cr.isChecked() or self.radio_Both.isChecked():
            if not self.crRadius:
                self.p4blank4.show()
                show = 0
            else:
                self.p4blank4.hide()

        if not self.itf:
            self.itf = 0

        # If initial threshold frequency is 0, minimum support can be anything.
        # But if initial threshold frequency is a non-zero percentage, minimum support
        # cannot be > itf.
        if int(self.itf) > 0:
            # Check if minimum support <= itf

            if int(self.minSupport) > int(self.itf):
                show = 0
                print(
                    "Minimum support cannot be more than Initial threshold frequency: {} ; {}".format(
                        self.minSupport, self.itf
                    )
                )
                # show a message
            # else:
            # hide the message

        if show == 1:
            # Call the analysis fn
            if self.radio_Cc.isChecked():
                # Call fn for CC Analysis
                print("CC Analysis")
                core_analysis(
                    self.OutputFile,
                    self.startYear,
                    self.endYear,
                    self.itf,
                    self.minSupport,
                    self.maxPrune,
                    self.minFreq,
                    self.crRadius,
                    0,
                )
            if self.radio_Cr.isChecked():
                # Call fn for CR Analysis
                print("CR Analysis")
                core_analysis(
                    self.OutputFile,
                    self.startYear,
                    self.endYear,
                    self.itf,
                    self.minSupport,
                    self.maxPrune,
                    self.minFreq,
                    self.crRadius,
                    1,
                )
            if self.radio_Both.isChecked():
                # Call both fns for CC & CR
                core_analysis(
                    self.OutputFile,
                    self.startYear,
                    self.endYear,
                    self.itf,
                    self.minSupport,
                    self.maxPrune,
                    self.minFreq,
                    self.crRadius,
                    2,
                )
                print("Both")

    def grab_parameters(self):

        self.areaOfInt = self.le_AreaOfInt.text()
        self.spUnits = self.le_SpUnits.text()
        self.timeUnits = self.le_TimeUnits.text()
        self.startYear = self.le_StartYear.text()
        self.endYear = self.le_EndYear.text()

        show = 1
        if not self.areaOfInt:
            self.p1blank1.show()
            show = 0
        else:
            self.p1blank1.hide()
        if not self.spUnits:
            self.p1blank2.show()
            show = 0
        else:
            self.p1blank2.hide()
        if not self.timeUnits:
            self.p1blank3.show()
            show = 0
        else:
            self.p1blank3.hide()
        if not self.startYear:
            self.p1blank4.show()
            show = 0
        else:
            self.p1blank4.hide()
        if not self.endYear:
            self.p1blank5.show()
            show = 0
        else:
            self.p1blank5.hide()

        if show == 1:
            self.stackedWidget.setCurrentIndex(1)

    def process_Shapefile(self, filename):
        """Process shapefile to generate neighbors (separate fn not needed)"""
        # selected filename should be a .shp file
        # Call find_neighbors.py and generate neighbors.csv in 'In' path
        shp_neighbors(filename, self.InputFile)

    def process_Point(self, filename):
        """Process Point Data to Voronoi Polygons"""
        pass

    def back1(self):
        self.stackedWidget.setCurrentIndex(0)

    def back2(self):
        self.stackedWidget.setCurrentIndex(1)

    def back3(self):
        self.stackedWidget.setCurrentIndex(2)

    def start_mistic(self):
        """Calls mistic funtion in driver.py"""

        if self.radio_Shapefile.isChecked():
            self.process_Shapefile(self.NeighborFile)
            # Value of NeighborFile changed for further use
            self.NeighborFile = self.InputFile + "/neighbors.csv"
        if self.radio_Point.isChecked():
            self.process_Point(self.NeighborFile)
            # read_Locations is the same file in this case
            # self.NeighborFile = self.InputFile + '/neighbors.csv'
        if self.radio_Manual.isChecked():
            # Manually provided neighbors.csv in Input path
            print("Checked")
            pass
        # call read_Neighbor fn from
        mistic(
            self.InputFile,
            self.OutputFile,
            self.NeighborFile,
            self.spUnits,
            self.timeUnits,
            self.startYear,
            self.endYear,
        )
        # if(Shapefile given)
        #   Show foci for each year in new window
        self.stackedWidget.setCurrentIndex(3)

    def exit(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
