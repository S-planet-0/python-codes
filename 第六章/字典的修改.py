# 创建一个人的信息字典
user = {"id": 123, "name": "小明", "age": 20}
print(user)

print(user["id"])
print(user["name"])
print(user["age"])

# 如下如果写user["grade"]会报错说KeyError:'grade'
# 写get就不会报错(默认返回None)，也可以指定默认值
print(user.get("grade"))
print(user.get("grade", 80))
