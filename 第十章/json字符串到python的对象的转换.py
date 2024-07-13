info = """
{"0": 0, "2": 4, "4": 16, "6": 36, "8": 64, "10": 100, "12": 144, "14": 196, "16": 256, "18": 324} 
"""

import json

data = json.loads(info)
print(data)
print(type(data))

