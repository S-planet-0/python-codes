import time


class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money

total_c = 0
total_m = []
customers = []
i = 1
while True:
    c = Customer(input(f"请输入人名(输quit,0,则退出)，第{i}位:"), int(input("请输入TA的随礼:")))
    customers.append(c)
    total_c += 1
    total_m.append(c.money)
    if c.name == "quit" and c.money == 0:
        customers.pop()
        total_m.pop()
        total_c -= 1
        print("*"*35)
        print(f"访客的总人数是{total_c}人,随礼列表如下:")
        for c_name in customers:
            print(f"访客{c_name.name},随礼{c_name.money}")
        print("*" * 35)
        print(f"随礼总金额:{sum(total_m)}")
        print(f"最大金额:{max(total_m)},最小金额:{min(total_m)}")
        print(f"人均:{(max(total_m) + min(total_m)) / 2}")
        time.sleep(20)
        break
    else:
        i += 1
