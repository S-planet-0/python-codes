def introduce(name, gender, age=6):
    """
    幼儿园自我介绍
    :param name:
    :param gender:
    :param age:
    :return:
    """
    print(f"大家好，我的名字是{name}，是个小{gender}，今年{age}岁了。")
# 默认参数age，必须放在其他所有参数的最后位置。
# 调用函数时，默认参数可以不写值。

# 如果不设置age，那么就是6岁。
introduce("小明", "男生")

# 也可以传递一个新值，覆盖默认值。
introduce("小白", "女生", 5)
