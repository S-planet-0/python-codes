students = {
    "xiaoming": {"id": 101, "age": 18, "gender": "boy"},
    "xiaohuang": {"id": 102, "age": 19, "gender": "girl"},
    "xiaowang": {"id": 103, "age": 17, "gender": "girl"},
}


def get_student(name):
    if name in students:
        return students[name]["age"], students[name]["gender"]
    else:
        return None, None
    # 因为要返回多个值，那么None也要返回多个，和正常数目对应。

# 可以分开变量接收
age, gender = get_student("xiaohuang")
print(age, gender)
# 可以单个变量接收，这时候info是一个元组。
info = get_student("xiaoxiaoxiao")
print(info, type(info))
