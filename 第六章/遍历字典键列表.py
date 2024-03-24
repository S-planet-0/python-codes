# 创建多个人的成绩数据
grades = {"小明": 88, "小花": 99, "小张": 77, "小白": 85}

for name in grades.keys():
    # 可以只获得keys，也可以用字典的方式获得value
    print(name, grades[name])

print("#####################################################")

print("【*查看grades.keys()的数据结构，实质是列表】")
print(grades.keys())
print()

print("【*可以将grades.keys()转换成列表】")
print(list(grades.keys()))

print("********************************************")
print("【*查看grades.items()的数据结构，实质是元祖】")
print(grades.items())
print(list(grades.items()))
