while True:
    info = input("请输入物品的重量（输入quit结束）：\n")
    if info == "quit":
        break
    weight = float(info)
    freight = 0
    if 0 < weight <= 1:
        freight = 7
    elif 1 < weight < 3:
        freight = 7 + 2 * weight
    elif weight >= 3:
        freight = 7 + 3 * weight

    else:
        print(f"您输入了错误数据:{weight}")
        continue
    print(f"该物品的运费是：{freight}")

