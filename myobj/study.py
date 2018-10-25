'''判断某数的数据类型（python中同一个变量可以进行不同类型的赋值）'''


def actionGetVarType():
    a = 1
    print(type(a))
    a = "你好"
    print(type(a))
    a = 1 / 5.0
    print(type(a))
    a = 2j + 4
    print(type(a))


'''结束判断某数的数据类型'''

'''此处为输出9*9乘法表'''


def action9X9():
    have = input("please input a number")
    if (have.isdigit()):
        inputI = int(have)
    else:
        exit("input is not digit")

    for i in range(1, inputI + 1):
        for j in range(1, i + 1):
            con = "%d*%d=%d" % (i, j, i * j)
            print(con, end="\t")
        print()


'''此处结束9*9乘法表'''

'''判断是否为闰年   START'''


def isRunYear(year, month, day):
    if (year % 4 == 0 and year % 400 == 0) or year % 400 == 0:
        return "%d-%d-%d 是闰年" % (year, month, day)
    else:
        return "%d-%d-%d 不是闰年" % (year, month, day)


'''判断是否为闰年   END'''


'''写入文件 并读取文件'''
def writeAndReadTxt(msg) :
    file = open("test.txt","w")
    file.write(msg)
    file.close()
    file = open("test.txt", "r")
    msg = file.readline();
    file.close()
    return msg
'''写入文件 并读取文件  END'''

