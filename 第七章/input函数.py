number = input("请输入一个数字：")
print(number, type(number))
# input函数本身使用的是字符串类型，想使用其他类型，需进行转换。
number = input("请输入一个数字：")
number = int(number)
print("信息结果：", number, type(number), number * number)
