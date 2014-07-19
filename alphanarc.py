#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from struct import *
from array import *
import sys, os
import ui_alphanarc

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
        f = open(filename, "rb")
        d = f.read()
        f.close()
        self.narc = NARC(d)
        self.refreshNarc()
    def refreshNarc(self):
        filenames = []
        for i in range(0, self.narc.btaf.getEntryNum()):
            name = "File %i" % i
            filenames.append(name)
        self.selectFile.clear()
        self.selectFile.addItems(filenames)
        #self.selectFile.setCurrentIndex(0)
        self.archivesize.setText(str(self.narc.btaf.getSize()+self.narc.btnf.header[0]+self.narc.gmif.size))
        self.archivefiles.setText(str(self.narc.btaf.getEntryNum()))
        self.archivename.setText(self.name)
    def selectArchiveFile(self):
        cfile = self.selectFile.currentIndex()
        self.fileindex.setText(str(cfile))
        self.filesize.setText(str(len(self.narc.gmif.files[cfile])))
        self.fileheader.setText(unicode(self.narc.gmif.files[cfile][:4]))
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
        newfile.write(self.narc.gmif.files[cfile])
        newfile.close()
    def extractAllFiles(self):
        dirname = QFileDialog.getExistingDirectory(None, "Choose a directory", self.dir)
        if not dirname:
            return
        try:
            os.mkdir(dirname)
        except:
            pass
        for n in range(0,self.narc.btaf.getEntryNum()):
            filename = "%s/%i" % (self.name,n)
            newfile = open(filename, 'wb')
            newfile.write(self.narc.gmif.files[n])
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
        self.narc.replaceFile(cfile,d)
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
        bytes = []
        for e in d:
            bytes.append(ord(e))
        self.narc.addFile(bytes)
        self.refreshNarc()
        self.selectArchiveFile()
        self.save()
    def save(self):
        f = open(self.NARCname, "wb")
        self.narc.ToFile(f)
        f.close()
        self.openNarc(self.NARCname)

class BTAF:
    def __init__(self, rawdata):
        if len(rawdata)>0:
            self.magic = rawdata[:4]
            self.header = unpack("II", rawdata[4:12])
            if self.magic != "BTAF":
                raise NameError, "BTAF tag not found"
        else:
            self.magic = "BTAF"
            self.header = (12, 0)

        self.table = []
        rawdata=rawdata[12:]
        if len(rawdata)>0:
            for i in range(self.getEntryNum()):
                self.table.append(unpack("II", rawdata[i*8:i*8+8]))
    def getSize(self):
        return self.header[0]
    def getEntryNum(self):
        return self.header[1]
    def ToFile(self, f, t):
        f.write(self.magic)
        f.write(pack("II", self.header[0],self.header[1]))

        for pair in t:
            f.write(pack("II", pair[0], pair[1]))
    def addFile(self):
        s, e=self.header
        s += 8
        e += 1
        self.header=s, e
class BTNF:
    def __init__(self, rawdata):
        if len(rawdata)>0:
            self.magic = rawdata[:4]
            self.header = unpack("IIHH", rawdata[4:0x10])
            if self.magic != "BTNF":
                raise NameError, "BTNF tag not found"
        else:
            self.magic = "BTNF"
            self.header = (16, 4, 0, 1)
    def ToFile(self, f):
        f.write(self.magic)
        f.write(pack("IIHH", self.header[0],self.header[1],self.header[2],self.header[3]))
class GMIF:
    def __init__(self, rawdata, t):
        if len(rawdata)>0:
            self.magic = rawdata[:4]
            self.size = unpack("I", rawdata[4:8])[0]
            if self.magic != "GMIF":
                raise NameError, "GMIF tag not found"
        else:
            self.magic = "GMIF"
            self.size = 8

        self.files = []
        for ofs in t:
            self.files.append(rawdata[8+ofs[0]:8+ofs[1]])

    def appendFile(raw):
        data += raw
        self.header.size += len(raw)
    def ToFile(self, f):
        f.write(self.magic)
        f.write(pack("I", self.size))
        stream = ""
        #print self.files
        for d in self.files:
            for e in d:
                stream += e#chr(
        f.write(stream)
    def addFile(self, data, size):
        self.files.append(data)
        self.size += size
    def buildIndex(self):
        index = []
        c = 0
        for f in self.files:
            l = len(f)
            index.append((c, c+l))
            c=c+l
        return index
class NARC:
    def __init__(self, rawdata):

        if len(rawdata)>0:
            self.magic = rawdata[:4]
            if self.magic != "NARC":
                raise NameError, "NARC tag not found"
            self.header = unpack("IIHH", rawdata[4:16])
        else:
            self.magic = "NARC"
            self.header = (0x0100FFFE, 0x10+12+8 + 0x10, 0x10, 3)


        rawdata= rawdata[16:]
        self.btaf = BTAF(rawdata)
        rawdata= rawdata[self.btaf.getSize():]
        self.btnf = BTNF(rawdata)
        rawdata= rawdata[self.btnf.header[0]:]
        self.gmif = GMIF(rawdata, self.btaf.table)

    def ToFile(self, f):
        f.write(self.magic)
        f.write(pack("IIHH", self.header[0],self.header[1],self.header[2],self.header[3]))
        self.btaf.ToFile(f, self.gmif.buildIndex())
        self.btnf.ToFile(f)
        self.gmif.ToFile(f)
    def addFile(self, s):
        size = len(s)
        mark, narcsz, hdrsize, sect = self.header
        narcsz += (size + 8)
        self.header = (mark, narcsz, hdrsize, sect)
        self.btaf.addFile()
        self.gmif.addFile(s, size)
    def replaceFile(self, index, s):
        newmold = len(s) - len(self.gmif.files[index])
        mark, narcsz, hdrsize, sect = self.header
        narcsz += (newmold)
        self.header = (mark, narcsz, hdrsize, sect)
        self.gmif.size += (newmold)
        self.gmif.files[index] = s



app = QApplication(sys.argv)
mw = MainWindow()
mw.show()
app.exec_()
