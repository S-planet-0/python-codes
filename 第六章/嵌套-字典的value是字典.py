# 学生信息字典的列表，表达多个学生信息
students = {
    "小张": {"id": 101, "grade": 88},
    "小王": {"id": 102, "grade": 99},
    "小李": {"id": 103, "grade": 77},
    "小赵": {"id": 104, "grade": 86},
}

for name, info in students.items():
    id, grade = info["id"], info["grade"]
    print(f"姓名为{name},学号为{id},成绩是{grade}分")
