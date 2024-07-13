class Phone:
    """ 这是一个手机类 """
    def __init__(self, model, price):
        self.model = model
        self.price = price
    ######## 构造函数↑ ########

    ######### 普通函数↓ #########
    def describe(self):
        info = f"这是{self.model}手机，价格是{self.price}元。"
        return info

    def call_friend(self, friend_name):
        message = f"我在用{self.model}手机，打电话给{friend_name}。"
        return message


# 初始化2个对象(此时才真正在内存中开辟了空间):
HuaWei = Phone("HuaWei P50", 4000)
iPhone = Phone("iPhone 13", 6000)

# 调用方法:
print(f"{HuaWei.describe()}{HuaWei.call_friend("小明")}")
print(f"{iPhone.describe()}{iPhone.call_friend("小白")}")
