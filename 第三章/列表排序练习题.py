heights = []
heights.append(178.4)
heights.append(179.3)
heights.append(176.8)
heights.append(180.5)
heights.append(177.7)
print(f"列表中有{len(heights)}个值")

# 方法1：
heights.sort(reverse=True)
print(heights)
# 方法2：
print(sorted(heights, reverse=True))
