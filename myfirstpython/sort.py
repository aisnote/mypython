#/usr/local/Cellar/python3/3.6.2

def insert(key, sortedList):
    if len(sortedList) == 0:
        sortedList[0] = key
        return

    index= 0
    firstOne = sortedList[0]
    nextIndex = 0
    nextOne = 0

    for nextIndex in range(1, len(sortedList)):
        nextOne = sortedList[nextIndex]
        if key <= nextOne and key >= nextOne:
            

    for outputKey in sortedList:
        if key >= outputKey and key

def sort(input):
    if not isinstance(input, list):
        return []

    output = []
    for key in input:
        for outPutKey in output:




    return input;

if __name__ == '__main__':
    # print("this is my project")
    input = [0, 11, 2, 13, 15, 9, 8, 1, 6, 5]
    output = sort(input)
    print(output)