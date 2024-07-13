class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def welcome(self):
        print(f"你好{self.name},欢迎到来！")


class Admin(User):
    def ctr_sys(self):
        print("我在管理系统！")

    def welcome(self):
        print(f"你好，尊贵的Admin管理员{self.name},欢迎归来！")


class Vip(User):
    def __init__(self, name, password, money):
        super().__init__(name, password)
        self.money = money

    def vip_service(self):
        print("您好，给您提供贵宾服务！")

    def welcome(self):
        print(f"你好，尊贵的Vip用户{self.name},欢迎归来！")


# 测试调用:
print("*"*25,"测试调用:","*"*25)
xiaoming = Admin("小明", 111)
xiaobai = Vip("小白", 110, 700)
xiaohuang = Vip("小黄", 112, 8000)
xiaoli, xiaozhang = User("小李", 113), User("小张", 114)
print("管理员用户:小明")
Admin.welcome(xiaoming)
Admin.ctr_sys(xiaoming)
print("*"*30)
print("VIP用户:小白、小黄")
Vip.welcome(xiaobai)
Vip.vip_service(xiaobai)
print(f"VIP用户{xiaobai.name}花了{xiaobai.money}元买了VIP服务。")
print("*"*25)
Vip.welcome(xiaohuang)
Vip.vip_service(xiaohuang)
print("*"*30)
print("普通用户:小李、小张")
User.welcome(xiaoli)
User.welcome(xiaozhang)
####################################################################
print("*"*45)
PassWd = {
    xiaoming.name : xiaoming.password,
    xiaobai.name : xiaobai.password,
    xiaohuang.name : xiaohuang.password,
    xiaoli.name : xiaoli.password,
    xiaozhang.name : xiaozhang.password,
}
print("以下是所有的用户名，密码表:")
for key in PassWd.keys():
    print(key, PassWd[key])

