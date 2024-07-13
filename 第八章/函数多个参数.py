def introduce(name, gender):
    """
    幼儿园自我介绍
    :param name:
    :param gender:
    :return:
    """
    print(f"大家好，我的名字是{name}，是个小{gender}。")
# 需要按顺序提供参数，顺序不能乱。
# 这叫做位置实参，按位置提供。
introduce("小明", "男生")
introduce("小白", "女生")
