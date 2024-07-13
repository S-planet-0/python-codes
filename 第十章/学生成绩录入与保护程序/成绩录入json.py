import os
import json

file = "成绩录入json.txt"
grade_dict = {}

if os.path.exists(file):
    with open(file, encoding='utf8') as fin:
        lines = fin.read()
        grade_dict = json.loads(lines)
        print("*"*15, "读取后的文件内容:", "*"*15)
        for key, value in grade_dict.items():
            print(key, value)
        print("*"*46)

while True:
    line_i = input("请输入学生姓名和成绩(输quit结束!):")
    if line_i == "quit":
        break
    field = line_i.split()
    if len(field) != 2:
        continue
    name, grade = field
    if not str(grade).isdigit():
        print("你输入的成绩不是数字,请重新输入!")
        continue
    grade_dict[name] = grade


with open(file, "w", encoding='utf8') as fout:
    line_o = fout.write(json.dumps(grade_dict))

