def introduce(name, age=6):
    """
    幼儿园自我介绍
    :param name:
    :param age:
    :return:
    """
    print(f"大家好，我叫{name}，我今年{age}岁了。")

# 如下的调用方式都可以
introduce("小明")
introduce(name="小明")
introduce("小白", 5)
introduce(name="小白", age=5)
introduce(age=5, name="小白")
