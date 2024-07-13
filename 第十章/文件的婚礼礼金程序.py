lines = {}
money_list = []
with open("婚礼礼金.txt", "w", encoding='utf8') as fout:
    while True:
        line = input("请输入'姓名 礼金':")
        if line == "quit":
            break
        fields = line.split(" ", 1)
        if len(fields) != 2:
            continue
        name, money = fields
        lines[name] = money
        fout.write(name + " " + money + "\n")


with open("婚礼礼金.txt", "r", encoding='utf8') as fin:
    for l in lines:
        money_list.append(int(lines[l]))
    print("*"*30)
    print("统计礼金数据:")
    print(f"礼金总计:{sum(money_list)}元")
    print(f"最高:{max(money_list)}，最低:{min(money_list)}，平均:{sum(money_list)/len(money_list)}")


