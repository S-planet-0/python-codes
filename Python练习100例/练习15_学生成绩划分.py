"""
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，
60分以下的用C表示。

程序分析：程序分析：(a>b) ? a:b 这是条件运算符的基本例子。
"""

grade = ""
score = input("请输入学生成绩:")
if not str(score).isnumeric():
    print("输入有误，请重新输入!")
else:
    score = int(score)
    if score >= 90:
        grade = "A"
    elif 60 <= score <= 89:
        grade = "B"
    elif 0 <= score < 60:
        grade = "C"
    print(f"成绩{score}，属于{grade}等。")
