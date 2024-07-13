"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
"""

message = input("请输入一行字符(以回车结束):")
letter = 0
space = 0
digit = 0
others = 0
index = 0
while index < len(message):
    c = message[index]
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
    index += 1

print(f"你输入了{letter}个字母，{space}个空格，{digit}个数字，以及{others}个其他字符。")
