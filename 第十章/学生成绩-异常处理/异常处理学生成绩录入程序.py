file_name = "学生成绩带异常处理.txt"
import json
import os
stu_grade = {}
if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        print("*"*10, "读取文件:", "*"*10)
        try:
            stu_grade = json.loads(f.read())
            for name, grade in stu_grade.items():
                print(name, grade)
        except Exception as e:
            print("文件读取出错!", e)

with open(file_name, "w", encoding='utf8') as f:
    while True:
        print("*"*30)
        info = input("请输入学生姓名和成绩(quit退出):")
        try:
            if info == "quit":
                break
            name, grade = info.split()
            grade = int(grade)
            stu_grade[name] = grade
        except Exception as e:
            print("出问题了:", e, "你输入的是:", info)
            continue
    f.write(json.dumps(stu_grade))

print("success!")

