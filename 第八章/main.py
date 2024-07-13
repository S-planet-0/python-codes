# 引用外部函数，方法 1 ：
# import compute
#
# print(compute.add(3, 5))
# print(compute.sub(3, 5))
# print(compute.mul(3, 5))
# print(compute.div(3, 5))

###################################

# 引用外部函数，方法 2 ：
# import compute as cp
#
# print(cp.add(3, 5))
# print(cp.sub(3, 5))
# print(cp.mul(3, 5))
# print(cp.div(3, 5))

###################################

# 引用外部函数，方法 3 ：
# from compute import add, sub, mul, div
#
# print(add(3, 5))
# print(sub(3, 5))
# print(mul(3, 5))
# print(div(3, 5))

###################################

# 引用外部函数，方法 4 ：
# from compute import *
#### 不建议使用 import * ，容易与自己代码中写的同名函数混淆！！！
#
# print(add(3, 5))
# print(sub(3, 5))
# print(mul(3, 5))
# print(div(3, 5))
