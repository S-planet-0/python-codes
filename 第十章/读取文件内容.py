# # 方法 1：
# f = open("访客列表.txt", encoding='utf8')
# content = f.read()
# print(content)
# f.close()
#####################################################
# # 方法 2：
# with open("访客列表.txt", encoding='utf8') as fin:
#     print(fin.read())
#####################################################
# # 方法 3：
# with open("访客列表.txt", encoding='utf8') as fin:
#     for line in fin:
#         line = line[:-1]
#         # line = line.rstrip()
#         print(line)
#####################################################
# # 方法 4：
with open("访客列表.txt", encoding='utf8') as fin:
    lines = fin.readlines()
    lines = [x[:-1] for x in lines]
    print(lines)

