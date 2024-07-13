import pandas as pd

datas = []
file = "礼金程序结果.xlsx"
while True:
    info = input("请输入姓名,金额(输quit退出):")
    if info == "quit":
        break
    else:
        name, money = info.split("，")
        money = int(money)
        datas.append([name, money])

df = pd.DataFrame(datas, columns=["姓名", "金额"])
df.to_excel(file, index=False)
