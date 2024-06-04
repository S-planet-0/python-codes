numbers = range(10)
# 一个列表：里面是每个偶数数字的平方。
data_list = [ x * x for x in numbers if x % 2 == 0 ]
print("data_list:", data_list)
# 一个字典：里面的key是偶数数字，value是它的平方，注意字典key是无序的。
data_dict = {x: x * x for x in numbers if x % 2 == 0}
print("data_dict:", data_dict)
# 一个集合：每个元素是偶数数字的平方，注意集合是无序的。
data_set = {x * x for x in numbers if x % 2 == 0}
print("data_set:", data_set)
