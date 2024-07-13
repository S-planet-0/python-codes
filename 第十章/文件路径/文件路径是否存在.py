file = "文件路径是否存在.txt"

import os
if os.path.exists(file):
    fexist = "文件存在!"
else:
    fexist = "文件不存在!"
print(f"'{file}',{fexist}")

file_1 = "文件路径是否存在/测试路径.txt"
if os.path.exists(file_1):
    fexist_1 = "文件存在!"
else:
    fexist_1 = "文件不存在!"
print(f"'{file_1}',{fexist_1}")

file_2 = r"D:\python codes - 1\第十章\文件路径\文件路径是否存在.txt"
if os.path.exists(file_2):
    fexist_2 = "文件存在!"
else:
    fexist_2 = "文件不存在!"
print(f"'{file_2}',{fexist_2}")

file_3 = "xxx.txt"
if os.path.exists(file_3):
    fexist_3 = "文件存在!"
else:
    fexist_3 = "文件不存在!"
print(f"'{file_3}',{fexist_3}")

