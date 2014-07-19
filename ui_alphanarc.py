# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alphanarc.ui'
#
# Created: Sun Dec  6 21:02:48 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 234)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open = QtGui.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(10, 10, 92, 28))
        self.open.setObjectName("open")
        self.selectFile = QtGui.QComboBox(self.centralwidget)
        self.selectFile.setGeometry(QtCore.QRect(160, 10, 171, 27))
        self.selectFile.setObjectName("selectFile")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(200, 40, 261, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 62, 18))
        self.label.setObjectName("label")
        self.filesize = QtGui.QLabel(self.groupBox)
        self.filesize.setGeometry(QtCore.QRect(100, 50, 71, 18))
        self.filesize.setObjectName("filesize")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 91, 18))
        self.label_2.setObjectName("label_2")
        self.fileheader = QtGui.QLabel(self.groupBox)
        self.fileheader.setGeometry(QtCore.QRect(100, 30, 71, 18))
        self.fileheader.setObjectName("fileheader")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 18))
        self.label_3.setObjectName("label_3")
        self.fileindex = QtGui.QLabel(self.groupBox)
        self.fileindex.setGeometry(QtCore.QRect(100, 70, 71, 18))
        self.fileindex.setObjectName("fileindex")
        self.replace = QtGui.QPushButton(self.groupBox)
        self.replace.setGeometry(QtCore.QRect(170, 30, 92, 28))
        self.replace.setObjectName("replace")
        self.deleteFile = QtGui.QPushButton(self.groupBox)
        self.deleteFile.setGeometry(QtCore.QRect(170, 60, 92, 28))
        self.deleteFile.setObjectName("deleteFile")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 40, 191, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 101, 18))
        self.label_4.setObjectName("label_4")
        self.archivesize = QtGui.QLabel(self.groupBox_2)
        self.archivesize.setGeometry(QtCore.QRect(110, 50, 71, 18))
        self.archivesize.setObjectName("archivesize")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 101, 18))
        self.label_6.setObjectName("label_6")
        self.archivename = QtGui.QLabel(self.groupBox_2)
        self.archivename.setGeometry(QtCore.QRect(110, 30, 71, 18))
        self.archivename.setObjectName("archivename")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 101, 18))
        self.label_5.setObjectName("label_5")
        self.archivefiles = QtGui.QLabel(self.groupBox_2)
        self.archivefiles.setGeometry(QtCore.QRect(110, 70, 81, 18))
        self.archivefiles.setObjectName("archivefiles")
        self.addFile = QtGui.QPushButton(self.centralwidget)
        self.addFile.setGeometry(QtCore.QRect(200, 150, 111, 28))
        self.addFile.setObjectName("addFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionReplace = QtGui.QAction(MainWindow)
        self.actionReplace.setObjectName("actionReplace")
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionSelectFile = QtGui.QAction(MainWindow)
        self.actionSelectFile.setObjectName("actionSelectFile")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.open, QtCore.SIGNAL("clicked()"), MainWindow.openArchive)
        QtCore.QObject.connect(self.replace, QtCore.SIGNAL("clicked()"), MainWindow.replaceFile)
        QtCore.QObject.connect(self.deleteFile, QtCore.SIGNAL("clicked()"), MainWindow.extractFile)
        QtCore.QObject.connect(self.addFile, QtCore.SIGNAL("clicked()"), MainWindow.appendFile)
        QtCore.QObject.connect(self.selectFile, QtCore.SIGNAL("currentIndexChanged(int)"), MainWindow.selectArchiveFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("MainWindow", "Open NARC", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "File Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "File Size", None, QtGui.QApplication.UnicodeUTF8))
        self.filesize.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "File Header", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "File Index", None, QtGui.QApplication.UnicodeUTF8))
        self.fileindex.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.replace.setText(QtGui.QApplication.translate("MainWindow", "Replace File", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFile.setText(QtGui.QApplication.translate("MainWindow", "Extract File", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Archive Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Archive Size", None, QtGui.QApplication.UnicodeUTF8))
        self.archivesize.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Archive Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Total Files", None, QtGui.QApplication.UnicodeUTF8))
        self.archivefiles.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.addFile.setText(QtGui.QApplication.translate("MainWindow", "Add File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReplace.setText(QtGui.QApplication.translate("MainWindow", "replace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setText(QtGui.QApplication.translate("MainWindow", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectFile.setText(QtGui.QApplication.translate("MainWindow", "selectFile", None, QtGui.QApplication.UnicodeUTF8))

