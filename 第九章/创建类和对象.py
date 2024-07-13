class Student:
    """ 类注释:这是学生类 """
    def __init__(self, name, age):
        """ 初始化方法 """
        # 普通实例变量，每个实例独有
        self.name = name
        self.age = age

    def introduce(self):
        """ 普通方法 """
        return f"大家好，我叫{self.name}，今年{self.age}岁了。"


xiaoming = Student("小明", 18)
xiaozhang = Student("小张", 17)
xiaozhao = Student("小赵", 19)
# 使用 对象.属性 来访问属性，使用 对象.方法 来访问方法。
print(xiaoming.name, xiaoming.age, xiaoming.introduce())
print(xiaozhang.name, xiaozhang.age, xiaozhao.introduce())
print(xiaozhao.name, xiaozhao.age, xiaozhao.introduce())

#### 函数 与 方法 的区别: ##############################################
#### 如果某个函数属于某个对象，你可以叫它方法，它不属于某个对象，可以叫它函数!! ####
