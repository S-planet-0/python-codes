eng_dict = {}
with open("英汉词典.txt", encoding='utf8') as f:
    for line in f:
        line = line.rstrip()
        fields = line.split(",")
        if len(fields) != 2:
            continue
        english, chinese = fields
        eng_dict[english] = chinese

while True:
    print("#"*30)
    info = input("请输入英语词语:")
    if info == "quit":
        break
    elif info in eng_dict:
        print(f"{info}的中文意思是{eng_dict[info]}")
    else:
        print(f"没有{info}这个词语")

