import json
data = list(range(20))
print(json.dumps(data), type(json.dumps(data)))

data_dict = {
    number: number * number
    for number in data
    if number % 2 == 0
}

print(json.dumps(data_dict), type(json.dumps(data_dict)))

