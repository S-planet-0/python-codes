students = {
    "xiaoming": {"id": 101, "age": 18, "gender": "boy"},
    "xiaohuang": {"id": 102, "age": 19, "gender": "girl"},
    "xiaowang": {"id": 103, "age": 17, "gender": "girl"},
}


def get(name):
    if name in students:
        return students[name]
    else:
        return None
