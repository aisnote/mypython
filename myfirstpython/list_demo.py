#/usr/local/Cellar/python3/3.6.2

def printMsg(msg):
    print(msg)

if __name__ == '__main__':
    # print("this is my project")

    printMsg("hello world")

    lizzard_list = ['spider legs', 'toes of frog', 'eyes of newt',
                    '3-bat wing', '4-slug butter', '5-snake dandruff']

    printMsg(lizzard_list)

    printMsg('this is first item: index is 0\n')
    printMsg(lizzard_list[0])

    printMsg(lizzard_list[1])

    # len 是内置函数
    count = len(lizzard_list)

    printMsg('count =' + str(count))

    # remove one item from the list
    del lizzard_list[3]

    printMsg(lizzard_list)

    # add one new item to the list
    lizzard_list.append('this is the new item')

    printMsg(lizzard_list)

    # list 加法
    list1 = [1, 2, 3, 4]
    list2 = ['this', 'is', 'my', 'second', 'list']

    list_added = list1 + list2

    printMsg(list_added)

    # list multiply
    list3 = [1, 2]
    list_multiply = list3 * 5
    printMsg(list_multiply)

    list4 = ['my', 'son']
    list_multiply2 = list4 * 3
    printMsg(list_multiply2) # result: ['my', 'son', 'my', 'son', 'my', 'son']

    list5 = ['my', 'son', 'is', 'great']
    # loop,  循环语句
    for item in list5:
        print(item)

