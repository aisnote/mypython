#/usr/local/Cellar/python3/3.6.2
# -*- coding: utf-8 -*-


def printMsg(msg):
    print(msg)

def readTextFileAndPrint():
    path = '/Users/liuliu/input.txt'
    inputFile = open(path, 'r')
    lines = inputFile.readlines()

    for line in lines:
        printMsg(line)

    inputFile.close()

def saveMsgToFile():
    printMsg("save Msg To file中文")

    myMsg = '中文sedgwick'
    a = myMsg.encode('utf-8')
    d = a.decode('utf-8')
    fileName = '/Users/liuliu/myfile.txt'

    # with open(fileName, 'wt', encoding='utf-8') as f:
    #     f.write(myMsg)

    outPutFile = open(fileName, 'wt', encoding='utf-8')
    outPutFile.write(d)
    outPutFile.close()


if __name__ == '__main__':
    # print("this is my project")
    readTextFileAndPrint()
    s = 'Python-中文'
    print(s)
    b = s.encode('utf-8')
    print(b)
    print(b.decode('utf-8'))


    saveMsgToFile()

