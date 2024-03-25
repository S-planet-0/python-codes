# 字典的value是列表，表达每个人列表类型信息
students = {
    "小张": ["足球", "篮球"],
    "小王": ["篮球", "乒乓球"],
    "小李": ["篮球", "棒球", "台球"],
    "小赵": ["乒乓球", "羽毛球"],
}

for student, likes in students.items():
    print(f"学生{student},爱好有这些{likes}")
