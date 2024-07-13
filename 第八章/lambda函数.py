sgrades = [("xiaoming", 89), ("xiaozhao", 77), ("xiaoxiaozhang", 99)]
# 方法 1 ：
# sgrades.sort(key=lambda m: m[1], reverse=True)
# print(sgrades)
# 方法 2 ：
print(sorted(sgrades, key=lambda m: m[1], reverse=True))
