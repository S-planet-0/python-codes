# key 是英语，value 是汉语
key = []
value = []

with open("英汉词典.txt", encoding='utf8') as fin:
    for line in fin:
        l = line.split(",", 1)
        key.append(l[0])
        value.append(l[1])


while True:
    word = input("请输入你要翻译的英语:")
    if word == "quit":
        break
    elif word in key:
        i = key.index(word)
        print(f"翻译的结果是:{value[i]}")
    else:
        print("没有这个词语")

