"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
"""
print("此处计算s=a+aa+aaa+...+aa...a的值,a的个数取n，\n")
a = int(input("请输入a="))
n = int(input("请输入n="))
i = 1
s = 0
j = 0
while i <= n:
    j = j * 10 + a
    s += j
    i += 1
print(f"s={s}")
