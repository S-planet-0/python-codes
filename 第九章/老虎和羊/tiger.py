from animal import Animal


class Tiger(Animal):
    def eat_meat(self, meat):
        self.meat = meat
        print(f"我是老虎，在吃{self.meat}")

