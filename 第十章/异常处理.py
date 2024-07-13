try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError as e:
    print("出现问题了:", e)
print("hahaha...")

try:
    with open("xxx.txt") as f:
        print(f.read())
except Exception as g:
    print("读取文件错误:", g)
print("hahaha...2")

