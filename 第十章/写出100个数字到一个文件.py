with open("写出数字列表.txt", "w", encoding='utf8') as fout:
    for number in range(100):
        fout.write(str(number) + "\n")
