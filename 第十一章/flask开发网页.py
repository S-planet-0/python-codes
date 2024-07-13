from flask import Flask

app = Flask("我的网页")


# http://127.0.0.1:5000/myindex
@app.route("/myindex")
def hello():
    return "hahaha..我的网页!myflask!"

app.run()
