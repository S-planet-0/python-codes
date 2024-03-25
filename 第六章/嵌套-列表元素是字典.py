# 学生信息字典的列表，表达多个学生信息
students = [
    {"id": 101, "name": "小张", "grade": 88},
    {"id": 102, "name": "小王", "grade": 99},
    {"id": 103, "name": "小李", "grade": 77},
    {"id": 104, "name": "小赵", "grade": 86}
]

for student in students:
    id, name, grade = student["id"], student["name"], student["grade"]
    print(f"学号为{id}的姓名是{name},成绩是{grade}分")
