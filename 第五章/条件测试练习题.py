grade = 70
print(grade, "分")
# 进行下列各项条件测试:
if grade >= 60:
    print("及格")
if grade < 60:
    print("不及格")
if grade == 100:
    print("满分")
if grade != 100:
    print("不是满分")
if grade >= 90:
    print("优秀")
if 70 <= grade < 90:
    print("良好")
if grade < 70:
    print("一般")
if grade == 66 in [66, 88, 99]:
    print("成绩顺口")
else:
    print("成绩不顺口")
if grade >= 60 and grade in [60, 70, 80, 90, 100]:
    print("成绩及格，并且以0结尾")
