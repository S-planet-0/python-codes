from flask import Flask

app = Flask("英汉小词典")


@app.route("/english")
def trans():
    with open("英汉小词典.txt", encoding='utf8') as f:
        ECdict = f.read()
        ECdict = ECdict.replace("\n", "<br/>")
        return ECdict

app.run()
