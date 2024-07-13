file = "婚礼礼金.txt"

import os
print(f"{file}:", os.path.exists(file))
print(f"XXX.txt:", os.path.exists("XXX.txt"))

file_1 = r"D:\python codes - 1\第十章\婚礼礼金.txt"
print(f"{file_1}:", os.path.exists(file_1))


