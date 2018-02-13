#/usr/local/Cellar/python3/3.6.2

def printMsg(msg):
    print(msg)

if __name__ == '__main__':
    # print("this is my project")

    fibs = (1, 2, 3, 4) # can not be changed
    printMsg(fibs)

    printMsg(fibs[3])
    # tuple can not be changed as below
    # fibs[3] = 10v

    array = [1, 2, 3, 4]
    array[3] = 10
    printMsg(array)

    # dictionary

    testDict = {'hanson': 'boy',
                'hedy': 'girl',
                'key': 'value'}

    printMsg(testDict)

    # printMsg(testDict[0])

    printMsg(testDict['hanson'])

    printMsg(testDict['hedy'])

    testDict = {'hanson1': {'sex':'boy',
                           'grade': '5th',
                           'age': '10'},
                'hedy1': [1,2,3,4],
                'key': 'value'}

    printMsg(testDict['hanson1'])
    printMsg(testDict['hedy1'])
    printMsg(testDict['key'])