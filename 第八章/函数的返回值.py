def add(x, y):
    """
    加法函数，可以自动处理字符串类型
    """
    x = int(x)
    y = int(y)
# return的后面加上返回值即可。
    return x + y

# 调用：
result = add(3, 5)
print(result)

print(add("4", 6))
print(add("4", "7"))
