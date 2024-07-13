import random
import time
target = random.randint(1, 100)
# print("target:", target)
count = 1
success = False
while count <= 10:
    number = input(f"1到100之间，请你猜一个数字(第{count}次)：")
    if not str(number).isnumeric():
        print("你输入的不是数字，请继续输入数字：")
        continue
    number = int(number)
    if number > target:
        print("你猜得大了，再猜：")
    elif number < target:
        print("你猜得小了，再猜：")
    else:
        print("恭喜你，猜对了！")
        success = True
        break
    count += 1
if not success:
    print(f"很抱歉，你没有猜出来，正确数字是{target}。")
time.sleep(20)
