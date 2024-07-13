def introduce(name, gender):
    """
    幼儿园自我介绍
    :param name:
    :param gender:
    :return:
    """
    print(f"大家好，我的名字是{name}，是个小{gender}。")
# 可以用 形参名 = 值 的方式提供实参。
introduce(name="小明", gender="男生")
introduce(gender="男生", name="小明")
# 也可以用 位置参数，和 关键字参数 配合。
introduce("小明", gender="男生")
