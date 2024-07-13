import sheep as s
import tiger as t

sheep01 = s.Sheep("羊", "奔跑")
tiger01 = t.Tiger("老虎", "追赶")

sheep01.eat_grass()
print(f"我还会{sheep01.run}")
tiger01.eat_meat(sheep01.name)
print(f"我还会{tiger01.run}")
