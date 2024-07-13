def compute(x, y, method="add"):
    """
    如果 method == "add"，打印 x + y 的值；
    如果 method == "sub"，打印 x - y 的值；
    如果 method == "mul"，打印 x * y 的值；
    如果 method == "div"，打印 x / y 的值；
    method 默认是加法。
    :param x:数字 x
    :param y:数字 y
    :param method:字符串 method
    :return:无（用print函数值表达）
    分别用如下方式调用函数：
    ① 位置参数
    ② 关键字参数，可以换顺序
    ③ 带默认值参数调用
    ④不带默认值参数调用
    """
    # if not str(x).isnumeric() or str(y).isnumeric():
    #     print("你输入的不是数字，请重新输入：")

    value = x + y

    if method == "sub":
        value = x - y

    elif method == "mul":
        value = x * y

    elif method == "div":
        value = x / y

    print(f"x {method} y = {value}")


# 测试用例：x=10,y=2,计算x与y的加减乘除。

# 调用函数compute,① 位置参数:
compute(x=10, y=2)
# 调用函数compute,② 关键字参数，可以换顺序:
compute(y=2, method="sub", x=10)
# 调用函数compute,③ 带默认值参数调用:
compute(10, 2)
# 调用函数compute,④ 不带默认值参数调用:
compute(x=10, y=2, method="mul")
compute(x=10, y=2, method="div")
