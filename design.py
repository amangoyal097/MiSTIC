# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Mon Nov 11 22:33:36 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(755, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame1)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName(_fromUtf8("page1"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.le_AreaOfInt = QtWidgets.QLineEdit(self.page1)
        self.le_AreaOfInt.setObjectName(_fromUtf8("le_AreaOfInt"))
        self.horizontalLayout_4.addWidget(self.le_AreaOfInt)
        self.p1blank1 = QtWidgets.QLabel(self.page1)
        self.p1blank1.setObjectName(_fromUtf8("p1blank1"))
        self.horizontalLayout_4.addWidget(self.p1blank1)
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_4
        )
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtWidgets.QLabel(self.page1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.le_SpUnits = QtWidgets.QLineEdit(self.page1)
        self.le_SpUnits.setObjectName(_fromUtf8("le_SpUnits"))
        self.horizontalLayout_5.addWidget(self.le_SpUnits)
        self.p1blank2 = QtWidgets.QLabel(self.page1)
        self.p1blank2.setObjectName(_fromUtf8("p1blank2"))
        self.horizontalLayout_5.addWidget(self.p1blank2)
        self.formLayout.setLayout(
            1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_5
        )
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtWidgets.QLabel(self.page1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.le_TimeUnits = QtWidgets.QLineEdit(self.page1)
        self.le_TimeUnits.setObjectName(_fromUtf8("le_TimeUnits"))
        self.horizontalLayout_6.addWidget(self.le_TimeUnits)
        self.p1blank3 = QtWidgets.QLabel(self.page1)
        self.p1blank3.setObjectName(_fromUtf8("p1blank3"))
        self.horizontalLayout_6.addWidget(self.p1blank3)
        self.formLayout.setLayout(
            2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_6
        )
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtWidgets.QLabel(self.page1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        self.le_StartYear = QtWidgets.QLineEdit(self.page1)
        self.le_StartYear.setObjectName(_fromUtf8("le_StartYear"))
        self.horizontalLayout_7.addWidget(self.le_StartYear)
        self.p1blank4 = QtWidgets.QLabel(self.page1)
        self.p1blank4.setObjectName(_fromUtf8("p1blank4"))
        self.horizontalLayout_7.addWidget(self.p1blank4)
        self.formLayout.setLayout(
            3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_7
        )
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_11 = QtWidgets.QLabel(self.page1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_8.addWidget(self.label_11)
        self.le_EndYear = QtWidgets.QLineEdit(self.page1)
        self.le_EndYear.setObjectName(_fromUtf8("le_EndYear"))
        self.horizontalLayout_8.addWidget(self.le_EndYear)
        self.p1blank5 = QtWidgets.QLabel(self.page1)
        self.p1blank5.setObjectName(_fromUtf8("p1blank5"))
        self.horizontalLayout_8.addWidget(self.p1blank5)
        self.formLayout.setLayout(
            4, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_8
        )
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.btn_Next1 = QtWidgets.QPushButton(self.page1)
        self.btn_Next1.setObjectName(_fromUtf8("btn_Next1"))
        self.gridLayout_3.addWidget(self.btn_Next1, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page1)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName(_fromUtf8("page3"))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox = QtWidgets.QGroupBox(self.page3)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 531, 33))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0,0,0,0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.le_InputFile = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_InputFile.setObjectName(_fromUtf8("le_InputFile"))
        self.horizontalLayout.addWidget(self.le_InputFile)
        self.btn_BrowseIn = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_BrowseIn.setObjectName(_fromUtf8("btn_BrowseIn"))
        self.horizontalLayout.addWidget(self.btn_BrowseIn)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page3)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(30, 40, 531, 33))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_2.setContentsMargins(0,0,0,0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.le_OutputFile = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.le_OutputFile.setObjectName(_fromUtf8("le_OutputFile"))
        self.horizontalLayout_2.addWidget(self.le_OutputFile)
        self.btn_BrowseOut = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_BrowseOut.setObjectName(_fromUtf8("btn_BrowseOut"))
        self.horizontalLayout_2.addWidget(self.btn_BrowseOut)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.btn_Back1 = QtWidgets.QPushButton(self.page3)
        self.btn_Back1.setObjectName(_fromUtf8("btn_Back1"))
        self.gridLayout_4.addWidget(self.btn_Back1, 2, 0, 1, 1)
        self.btn_Next2 = QtWidgets.QPushButton(self.page3)
        self.btn_Next2.setObjectName(_fromUtf8("btn_Next2"))
        self.gridLayout_4.addWidget(self.btn_Next2, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page3)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName(_fromUtf8("page2"))
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_3 = QtWidgets.QGroupBox(self.page2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.radio_Shapefile = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_Shapefile.setGeometry(QtCore.QRect(20, 40, 97, 18))
        self.radio_Shapefile.setObjectName(_fromUtf8("radio_Shapefile"))
        self.radio_Point = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_Point.setGeometry(QtCore.QRect(20, 70, 97, 18))
        self.radio_Point.setObjectName(_fromUtf8("radio_Point"))
        self.radio_Manual = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_Manual.setGeometry(QtCore.QRect(20, 100, 97, 18))
        self.radio_Manual.setObjectName(_fromUtf8("radio_Manual"))
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 140, 551, 56))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0,0,0,0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_3.addWidget(self.label_12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.le_SpNeighbor = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_SpNeighbor.setObjectName(_fromUtf8("le_SpNeighbor"))
        self.horizontalLayout_3.addWidget(self.le_SpNeighbor)
        self.btn_BrowseNbh = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_BrowseNbh.setObjectName(_fromUtf8("btn_BrowseNbh"))
        self.horizontalLayout_3.addWidget(self.btn_BrowseNbh)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 2)
        self.btn_Back2 = QtWidgets.QPushButton(self.page2)
        self.btn_Back2.setObjectName(_fromUtf8("btn_Back2"))
        self.gridLayout_5.addWidget(self.btn_Back2, 1, 0, 1, 1)
        self.btn_Start = QtWidgets.QPushButton(self.page2)
        self.btn_Start.setAutoDefault(False)
        self.btn_Start.setDefault(True)
        self.btn_Start.setFlat(False)
        self.btn_Start.setObjectName(_fromUtf8("btn_Start"))
        self.gridLayout_5.addWidget(self.btn_Start, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page2)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName(_fromUtf8("page4"))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_6 = QtWidgets.QLabel(self.page4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_13.addWidget(self.label_6)
        self.le_itf = QtWidgets.QLineEdit(self.page4)
        self.le_itf.setObjectName(_fromUtf8("le_itf"))
        self.horizontalLayout_13.addWidget(self.le_itf)
        self.p4blank5 = QtWidgets.QLabel(self.page4)
        self.p4blank5.setObjectName(_fromUtf8("p4blank5"))
        self.horizontalLayout_13.addWidget(self.p4blank5)
        self.gridLayout_6.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.radio_Cc = QtWidgets.QRadioButton(self.page4)
        self.radio_Cc.setObjectName(_fromUtf8("radio_Cc"))
        self.gridLayout_6.addWidget(self.radio_Cc, 1, 0, 1, 1)
        self.radio_Cr = QtWidgets.QRadioButton(self.page4)
        self.radio_Cr.setObjectName(_fromUtf8("radio_Cr"))
        self.gridLayout_6.addWidget(self.radio_Cr, 2, 0, 1, 1)
        self.radio_Both = QtWidgets.QRadioButton(self.page4)
        self.radio_Both.setObjectName(_fromUtf8("radio_Both"))
        self.gridLayout_6.addWidget(self.radio_Both, 3, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_2 = QtWidgets.QLabel(self.page4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_9.addWidget(self.label_2)
        self.le_MinSup = QtWidgets.QLineEdit(self.page4)
        self.le_MinSup.setObjectName(_fromUtf8("le_MinSup"))
        self.horizontalLayout_9.addWidget(self.le_MinSup)
        self.p4blank1 = QtWidgets.QLabel(self.page4)
        self.p4blank1.setObjectName(_fromUtf8("p4blank1"))
        self.horizontalLayout_9.addWidget(self.p4blank1)
        self.gridLayout_6.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_3 = QtWidgets.QLabel(self.page4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_10.addWidget(self.label_3)
        self.le_CrRadius = QtWidgets.QLineEdit(self.page4)
        self.le_CrRadius.setObjectName(_fromUtf8("le_CrRadius"))
        self.horizontalLayout_10.addWidget(self.le_CrRadius)
        self.p4blank4 = QtWidgets.QLabel(self.page4)
        self.p4blank4.setObjectName(_fromUtf8("p4blank4"))
        self.horizontalLayout_10.addWidget(self.p4blank4)
        self.gridLayout_6.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_4 = QtWidgets.QLabel(self.page4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_11.addWidget(self.label_4)
        self.le_MaxPrune = QtWidgets.QLineEdit(self.page4)
        self.le_MaxPrune.setObjectName(_fromUtf8("le_MaxPrune"))
        self.horizontalLayout_11.addWidget(self.le_MaxPrune)
        self.p4blank2 = QtWidgets.QLabel(self.page4)
        self.p4blank2.setObjectName(_fromUtf8("p4blank2"))
        self.horizontalLayout_11.addWidget(self.p4blank2)
        self.gridLayout_6.addLayout(self.horizontalLayout_11, 6, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_5 = QtWidgets.QLabel(self.page4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_12.addWidget(self.label_5)
        self.le_MinFreq = QtWidgets.QLineEdit(self.page4)
        self.le_MinFreq.setObjectName(_fromUtf8("le_MinFreq"))
        self.horizontalLayout_12.addWidget(self.le_MinFreq)
        self.p4blank3 = QtWidgets.QLabel(self.page4)
        self.p4blank3.setObjectName(_fromUtf8("p4blank3"))
        self.horizontalLayout_12.addWidget(self.p4blank3)
        self.gridLayout_6.addLayout(self.horizontalLayout_12, 7, 0, 1, 1)
        self.btn_Back3 = QtWidgets.QPushButton(self.page4)
        self.btn_Back3.setObjectName(_fromUtf8("btn_Back3"))
        self.gridLayout_6.addWidget(self.btn_Back3, 8, 1, 1, 1)
        self.btn_Next3 = QtWidgets.QPushButton(self.page4)
        self.btn_Next3.setObjectName(_fromUtf8("btn_Next3"))
        self.gridLayout_6.addWidget(self.btn_Next3, 8, 2, 1, 1)
        self.stackedWidget.addWidget(self.page4)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.le_AreaOfInt, self.le_SpUnits)
        MainWindow.setTabOrder(self.le_SpUnits, self.le_TimeUnits)
        MainWindow.setTabOrder(self.le_TimeUnits, self.le_StartYear)
        MainWindow.setTabOrder(self.le_StartYear, self.le_EndYear)
        MainWindow.setTabOrder(self.le_EndYear, self.btn_Next1)
        MainWindow.setTabOrder(self.btn_Next1, self.radio_Shapefile)
        MainWindow.setTabOrder(self.radio_Shapefile, self.radio_Point)
        MainWindow.setTabOrder(self.radio_Point, self.radio_Manual)
        MainWindow.setTabOrder(self.radio_Manual, self.le_SpNeighbor)
        MainWindow.setTabOrder(self.le_SpNeighbor, self.btn_BrowseNbh)
        MainWindow.setTabOrder(self.btn_BrowseNbh, self.btn_Back2)
        MainWindow.setTabOrder(self.btn_Back2, self.le_InputFile)
        MainWindow.setTabOrder(self.le_InputFile, self.btn_BrowseIn)
        MainWindow.setTabOrder(self.btn_BrowseIn, self.le_OutputFile)
        MainWindow.setTabOrder(self.le_OutputFile, self.btn_BrowseOut)
        MainWindow.setTabOrder(self.btn_BrowseOut, self.btn_Back1)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Area of Interest", None))
        self.p1blank1.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.label_8.setText(_translate("MainWindow", "No of Spatial Units", None))
        self.p1blank2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.label_9.setText(_translate("MainWindow", "No of Time Units", None))
        self.p1blank3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.label_10.setText(_translate("MainWindow", "Start Year", None))
        self.p1blank4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.label_11.setText(_translate("MainWindow", "End Year", None))
        self.p1blank5.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.btn_Next1.setText(_translate("MainWindow", "Next", None))
        self.groupBox.setTitle(_translate("MainWindow", "Path to input files", None))
        self.btn_BrowseIn.setText(_translate("MainWindow", "Browse", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Path to output files", None))
        self.btn_BrowseOut.setText(_translate("MainWindow", "Browse", None))
        self.btn_Back1.setText(_translate("MainWindow", "Back", None))
        self.btn_Next2.setText(_translate("MainWindow", "Next", None))
        self.groupBox_3.setTitle(
            _translate(
                "MainWindow", "Preferred mode of Input for Spatial Neighbours", None
            )
        )
        self.radio_Shapefile.setText(_translate("MainWindow", "Shapefile", None))
        self.radio_Point.setText(_translate("MainWindow", "Point Data", None))
        self.radio_Manual.setText(_translate("MainWindow", "Manual", None))
        self.label_12.setText(
            _translate("MainWindow", "Path to corresponding file", None)
        )
        self.btn_BrowseNbh.setText(_translate("MainWindow", "Browse", None))
        self.btn_Back2.setText(_translate("MainWindow", "Back", None))
        self.btn_Start.setText(_translate("MainWindow", "Start MiSTIC", None))
        self.label_6.setText(
            _translate("MainWindow", "Initial threshold frequency", None)
        )
        self.p4blank5.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p>( Default is 0 )</p></body></html>",
                None,
            )
        )
        self.radio_Cc.setText(_translate("MainWindow", "CC Only", None))
        self.radio_Cr.setText(_translate("MainWindow", "CR Only", None))
        self.radio_Both.setText(_translate("MainWindow", "Both CC && CR", None))
        self.label_2.setText(_translate("MainWindow", "Minimum Support", None))
        self.p4blank1.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.label_3.setText(_translate("MainWindow", "CR Radius", None))
        self.p4blank4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.label_4.setText(_translate("MainWindow", "Max Prune", None))
        self.p4blank2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.label_5.setText(_translate("MainWindow", "Min Frequency", None))
        self.p4blank3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ff0000;">Field cannot be left blank</span></p></body></html>',
                None,
            )
        )
        self.btn_Back3.setText(_translate("MainWindow", "Back", None))
        self.btn_Next3.setText(_translate("MainWindow", "Next", None))
