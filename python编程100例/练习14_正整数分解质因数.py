"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""


def factoriNum(num):
    if not str(num).isnumeric() or int(num) <= 0:
        print("请输入一个正整数!")
        ####### 退出当前函数 #######
        exit(0)

    ################# 正常情况: #################
    elif num == 1:
        print(f"{num}=", end="1\n")
    else:
        index = 2
        print(f"{num}=", end="")
        while index <= num + 1:
            if num % index == 0:
                num //= index
                if num == 1:
                    print(index)
                    break
                else:
                    print(f"{index}", end="*")
            else:
                index += 1
                continue


# 测试调用:
factoriNum(90)
factoriNum(100)

factoriNum(1)
factoriNum(2)
factoriNum(3)
factoriNum(4)
