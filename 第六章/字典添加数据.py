# 创建多个人的信息字典
grades = {"小明": 88, "小花": 99, "小张": 77, "小白": 85, }
print(grades)

# 如下两个，因为Key不存在，会新增键值对：
grades["小李"] = 90
grades["小赵"] = 88
print(grades)

# 如下一个，因为小张之前存在键，所以值会被修改：
grades["小张"] = 79
print(grades)
