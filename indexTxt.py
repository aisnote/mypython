# -*- coding: utf-8 -*-
import sys
import os
import os.path

g_output_log = True

def mylog(msg):
    if g_output_log:
        print msg
    else:
        pass

class IndexFile(object):
    """header format for the index file. index.tmp

        datFileName: 256byte
        datFileSize: int64
        keyWordStructure:
                        {key:128byte,
                         offset: int64 //from 0 on datFile
                         length: int64
                         }
    """
    datFileName = ""
    datFileSize = 0


    __keyWords = []                         # like ['this', 'bank', 'shopping', 'www.sohu.com']
    __keyLink = (0, 100)                    # tuple, 1st is offset, 2nd is length
    __keyLinks = []                         # [keyLink, keyLink]
    __keyWordIndexLinks = []                # [{0,}]
    def __init__(self, datFileName):
        """datFileName need absolute path"""
        self.datFileName = datFileName
        self.datFileSize = 0

    def appendKeyLink(self, keyLink):
        self.__keyLinks.append(keyLink)

    def appendKeyWord(self, keyWord):
        self.__keyWords.append(keyWord)

    def lookupKeyWordAnd(self, keyWord):
        """judge the key word is existed or not"""
        keyWordIndex = 0
        for key in self.__keyWords:
            if key == keyWord:
                mylog("Found the key" + key)
            else:
                continue


class DatFile(object):
    """data file structure, just save the sentences
       and make sure the sentence only have one copy

        sentence1 CRLF or LF
        sentence2 CRLF or LF

    """
    fileName = ""        # need to save back
    sentences = []       # cache the sentences from data file
    def __init__(self, fileName):
        self.fileName = fileName

    def read(self, fileName):
        self.fileName = fileName
        file = open(fileName)
        while 1:
            line = file.readline()
            if line:
                self.sentences.append(line)
            else:
                break
        #end of while
        file.close()

    def save(self, fileName):
        tempFileName = fileName
        if not tempFileName:
            tempFileName = self.fileName

        if not tempFileName:
            print "please passed in the real file name you want to save"
            return

        if len(self.sentences) <= 0:
            print "data not ready for save"
            return

        file = open(tempFileName, 'w')
        if file:
            file.writelines(self.sentences)
        else:
            print ("open file to save failed")
            return

        file.close()

# class IndexText(object):
#     """Index one text file.

#     create index for lots of text, support unicode
#     """
#     def indexTextFile(self, fileName):
#         """indexing one textfile passed by fileName"""
class IndexTextFileMgr(object):
    filePath = ''
    def __init__(self, path):
        self.filePath = path

    def startIndexing(self):
        """indexing"""
        datFile = DatFile("")
        for root, dirs, files in os.walk(r"e:\\mytools\\aisnote\\Release2011-05-14\\elliot\\data"):
            for name in files:
                filePathName = root + '\\' + name
                print filePathName
                
                datFile.read(filePathName)
        
        datFile.save("d:\\testDatFile.txt")


#if __name__ == 'main':
#a = 1
test = IndexTextFileMgr(r"e:\\mytools\\aisnote\\Release2011-05-14\\elliot\\data")
test.startIndexing()
#print a
###print "start indexing..."
