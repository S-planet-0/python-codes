student = (1001, "小明", 20, 176)
print(student, type(student))

print("for循环遍历元组：")
for x in student:
    print(x)

print("拆包得到多个变量：")
# noinspection NonAsciiCharacters
学号, 姓名, 年龄, 身高 = student
print("学号：", 学号)
print("姓名：", 姓名)
print("年龄：", 年龄)
print("身高：", 身高)

# student[1] = "大明" (会报错！不能单个修改元组的值)
student = (1002, "小白", 21, 173)
print("修改后:", student, type(student))
