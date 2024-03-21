grades = [66, 55, 75, 80, 43, 90]
for grade in grades:
    print("***你的成绩是：", grade)
    if grade >= 60:
        print("恭喜你，通过了考试")
        print("请继续保持")
    else:
        print("很遗憾，你的成绩不及格")
        print("请继续努力")
print("**************************************")
# 变量grade可以重复利用
grade = 70
print(grade)
# 判断 70 是不是在grades里面，不在则返回False
print(grade in grades)
# 判断grade是不是大于60
print(grade >= 60)
