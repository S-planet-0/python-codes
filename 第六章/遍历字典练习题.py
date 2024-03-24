friends_FavFruits = {"小明": "apple", "小花": "orange", "小张": "banana", "小白": "pear", }
message_f = "朋友"
message_m = "最喜欢的水果是"
for friend in friends_FavFruits.keys():
    print(message_f, " ", friend, " ", message_m, " ", friends_FavFruits[friend])
