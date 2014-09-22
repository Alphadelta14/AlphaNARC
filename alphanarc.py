#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from struct import *
from array import *
import sys, os
import ui_alphanarc

sys.path.append('../')
from rawdb.ntr.narc import NARC
from rawdb.util.io import BinaryIO


class MainWindow(QMainWindow, ui_alphanarc.Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        if len(sys.argv)>1:
            fileName = sys.argv[1]
            self.openNarc(fileName)
    def openArchive(self):
        fileName = QFileDialog.getOpenFileName(None, "Open NARC", "~/Desktop", "NARC Files (*.narc *.NARC *.bin);;All Files (*.*)");
        if not fileName:
            return
        self.openNarc(str(fileName))
    def openNarc(self, filename):
        self.NARCname = filename
        ndir, nfile = os.path.split(str(filename))
        self.name = nfile
        with open(filename, "rb") as handle:
            self.narc = NARC(BinaryIO.adapter(handle))
        self.refreshNarc()
    def refreshNarc(self):
        filenames = []
        for i in xrange(self.narc.fatb.num):
            name = "File %i" % i
            filenames.append(name)
        self.selectFile.clear()
        self.selectFile.addItems(filenames)
        #self.selectFile.setCurrentIndex(0)
        self.archivesize.setText('--')
        self.archivefiles.setText(str(self.narc.fatb.num))
        self.archivename.setText(self.name)
    def selectArchiveFile(self):
        cfile = self.selectFile.currentIndex()
        self.fileindex.setText(str(cfile))
        self.filesize.setText(str(len(self.narc.fimg.files[cfile])))
        self.fileheader.setText(unicode(self.narc.fimg.files[cfile][:4]))
    def deleteFile(self):
        print "can't delete"
        return
    def extractFile(self):
        cfile = self.selectFile.currentIndex()
        propfilename = "%s/%s_%i" % (".", os.path.splitext(self.name)[0], cfile)
        filename = QFileDialog.getSaveFileName(None, "Save File", propfilename, "All Files (*.*)")
        if not filename:
            return
        newfile = open(filename, 'w')
        newfile.write(self.narc.fimg.files[cfile])
        newfile.close()
    def extractAllFiles(self):
        dirname = QFileDialog.getExistingDirectory(None, "Choose a directory", self.dir)
        if not dirname:
            return
        try:
            os.mkdir(dirname)
        except:
            pass
        for n in range(0,self.narc.fatb.num):
            filename = "%s/%i" % (self.name,n)
            newfile = open(filename, 'wb')
            newfile.write(self.narc.fimg.files[n])
            newfile.close()
    def replaceFile(self):
        cfile = self.selectFile.currentIndex()
        fileName = QFileDialog.getOpenFileName(None, "Open File", "~/Desktop", "All Files (*.*)");
        if not fileName:
            return
        f = open(fileName, "rb")
        d = f.read()
        f.close()
        #bytes = ""
        #print d
        #for e in d:
        #    print ord(e),
        #    #bytes+= (chr(int(e)))
        #return
        self.narc.files[cfile] = d
        self.refreshNarc()
        self.selectArchiveFile()
        self.save()
    def appendFile(self):
        fileName = QFileDialog.getOpenFileName(None, "Open File", "~/Desktop", "All Files (*.*)");
        if not fileName:
            return
        f = open(fileName, "rb")
        d = f.read()
        f.close()
        self.narc.files.append(d)
        self.refreshNarc()
        self.selectArchiveFile()
        self.save()
    def save(self):
        f = open(self.NARCname, "wb")
        f.write(str(self.narc))
        f.close()
        self.openNarc(self.NARCname)


app = QApplication(sys.argv)
mw = MainWindow()
mw.show()
app.exec_()
