while True:
    print("#" * 20)
    info = input("请输入一个你喜欢的颜色，输入quit表示退出：\n")
    if info == "quit":
        break
    else:
        print(f"很好，你喜欢这个颜色：{info}")
