from flask import Flask
app=Flask(__name__)
@app.route("/")
def homepage():
    return "primeiro site 2"
app.run(debug=True)

