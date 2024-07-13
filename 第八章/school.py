from student_query import get

while True:
    name = input("请输入学生名字（输入quit退出）：")
    if name == "quit":
        break
    else:
        info = get(name)
        if not info:
            print("没有这个学生信息！")
        else:
            print("你要查询的学生信息如下：\n", info)
