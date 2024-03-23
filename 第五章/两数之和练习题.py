numbers = [2, 3, 5, 8, 7, 4, 1, 6]
numbers.sort(reverse=False)
Sum_2num = 8
sum_num = 0
# 查找有哪几对数的和为 8 ？
for curr_num in numbers:
    for number in numbers:
        if curr_num != number and curr_num < number:
            if curr_num + number == Sum_2num:
                print(curr_num, ",", number, "此两数的和为", Sum_2num)
                sum_num += 1
print("总共有", sum_num, "对数字相加为", Sum_2num)
