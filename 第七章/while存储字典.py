student_grade = {}
while True:
    info = input("请输入学生姓名和成绩，用空格分割(输quit退出)：\n")
    if info == "quit":
        break
    # str.split函数，可以用空白符号拆分大字符串。
    name, grade = info.split()
    grade = int(grade)
    student_grade[name] = grade

print("学生信息如下：\n")
for name, grade in student_grade.items():
    print(name, grade)

print("最高分：", max(student_grade.values()))
print("最低分：", min(student_grade.values()))
print("平均分：", sum(student_grade.values()) / len(student_grade))

