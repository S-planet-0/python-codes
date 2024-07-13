def compute(x, y, method):
    if method == "add":
        return x + y
    elif method == "sub":
        return x - y
    elif method == "mul":
        return x * y
    elif method == "div":
        return x / y
    else:
        return None


def add(x, y):
    return compute(x, y, "add")


def sub(x, y):
    return compute(x, y, "sub")


# 调用函数：
print(add(1, 1))
print(sub(1, 2))
