class car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def info(self):
        print(f"车型是{self.model},价格是{self.price}")

