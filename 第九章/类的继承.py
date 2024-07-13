class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def info(self):
        print(f"车型是{self.model}，价格是{self.price}万元。")


class OilCar(Car):
    def __init__(self, model, price, box_size):
        super().__init__(model, price)
        self.box_size = box_size

    def add_oil(self, money):
        print(f"老板，加{money}元的汽油。")

    def info(self):
        super().info()
        print("我是油车，跑起来比电动车动力更足。")


class ElectricCar(Car):
    def __init__(self, model, price, battery_size):
        super().__init__(model, price)
        self.battery_size = battery_size

    def add_electric(self, money):
        print(f"车值{self.price}万元，充电花了{money}元。")


# 测试调用:
OCar_1 = OilCar("路虎", 60, 50)
print(OCar_1.model, OCar_1.price, OCar_1.box_size)
OCar_1.info()
OCar_1.add_oil(200)

eCar_1 = ElectricCar("特斯拉", 100, 200)
print(eCar_1.model, eCar_1.price, eCar_1.battery_size)
eCar_1.info()
eCar_1.add_electric(300)

