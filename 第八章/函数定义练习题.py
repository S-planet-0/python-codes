def sum_numbers(number):
    """
    此函数实现：数字 1 到数字 number 之间，
    所有整数的加和。
    :param number:
    :return:
    """
    if not str(number).isdigit():
        print("你输入的不是整数，请重新输入!")
    else:
        print("**************方法一(while)**************")
        number = int(number)
        temp = number
        sum_number_1 = 0
        while temp >= 1:
            sum_number_1 += temp
            temp -= 1
        print(f"从 1 到数字{number}之间的所有整数之和是{sum_number_1}")
        print("**************方法二(for)**************")
        sum_number_2 = 0
        for i in range(1, number + 1):
            sum_number_2 += i
        print(f"从 1 到数字{number}之间的所有整数之和是{sum_number_2}")


# 调用此函数
sum_numbers(100)
sum_numbers(number=input("请输入一个整数："))
