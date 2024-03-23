fruits = ["apple", "pear", "orange"]
# 吃掉一个水果，水果的总数就减少一个。
fruits_sum = len(fruits)
print("一共有", fruits_sum, "个水果。")
if fruits_sum:
    for fruit in fruits:
        print("接下来吃这个水果", fruit)
        fruits_sum -= 1
if fruits_sum == 0:
    print("现在水果都吃完了。")
