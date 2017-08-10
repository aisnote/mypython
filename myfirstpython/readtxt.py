#/usr/local/Cellar/python3/3.6.2

def printMsg(msg):
    print(msg)

def readTextFileAndPrint():
    path = '/Users/liuliu/input.txt'
    inputFile = open(path, 'r')
    lines = inputFile.readlines()

    for line in lines:
        printMsg(line)

    inputFile.close()

if __name__ == '__main__':
    # print("this is my project")
    readTextFileAndPrint()