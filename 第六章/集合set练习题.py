students = {
    "小张": ["足球", "篮球"],
    "小王": ["篮球", "乒乓球"],
    "小李": ["篮球", "棒球", "台球"],
    "小赵": ["乒乓球", "羽毛球"],
}
likes = set()
for value in students.values():
    for like in value:
        likes.add(like)
print(likes)
