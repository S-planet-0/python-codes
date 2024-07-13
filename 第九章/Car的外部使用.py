# 方法 1
# 引入文件 Car.py
import Car

# 新建 对象=文件名.方法
my_car = Car.car("路虎", 80)
# 应用 对象.方法
my_car.info()

#################################################
# 方法 2
# 从文件 Car 中，引入方法 car
from Car import car

my_car = car("路虎", 80)
my_car.info()

#################################################
# 方法 3
import Car as C

my_car = C.car("路虎", 80)
my_car.info()

