class StudentGrade:
    """ 学生成绩 """
    def __init__(self, name, yuwen, shuxue):
        self.name = name
        self.yuwen = yuwen
        self.shuxue = shuxue

    def update(self, course, grade):
        if course == "语文":
            self.yuwen = grade
        elif course == "数学":
            self.shuxue = grade

# 赋值操作:
xiaoming = StudentGrade("小明", 88, 99)
print(f"{xiaoming.name}的语文成绩：{xiaoming.yuwen}")
print(f"{xiaoming.name}的数学成绩：{xiaoming.shuxue}")
print("********************************************************")


# 更新操作,方法 1:
xiaoming.yuwen = 89
xiaoming.shuxue = 96
print(f"{xiaoming.name}的语文成绩：{xiaoming.yuwen}")
print(f"{xiaoming.name}的数学成绩：{xiaoming.shuxue}")
print("********************************************************")

# 更新操作,方法 2:
xiaoming.update("语文", 86)
xiaoming.update("数学", 99)
print(f"{xiaoming.name}的语文成绩：{xiaoming.yuwen}")
print(f"{xiaoming.name}的数学成绩：{xiaoming.shuxue}")
print("********************************************************")
