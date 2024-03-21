numbers = range(1, 101)
new = []
for number in numbers:
    new_number = number * number
    new.append(new_number)
print("1-100的数的平方和：", sum(new))
