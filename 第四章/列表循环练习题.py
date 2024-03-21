print("方法1（grades自变）：")
grades = [77, 88, 73, 99, 82, 89, 95, 86, 93]
grades.sort(reverse=True)
# 0是False(升序)，1是True(降序)!
print("Max:", max(grades))
print("Min:", min(grades))
print("Avg:", sum(grades)/len(grades))
print("Top 3:", grades[:3])
# *****************************************************
print("方法2（grades置入新变量）：")
grades = [77, 88, 73, 99, 82, 89, 95, 86, 93]
sorted_grades = sorted(grades, reverse=True)
print("Max:", max(sorted_grades))
print("Min:", min(sorted_grades))
print("Avg:", sum(grades)/len(grades))
print("Top 3:", sorted_grades[:3])
