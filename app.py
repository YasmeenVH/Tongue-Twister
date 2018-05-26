from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello tongue twisters!"
    name="Peter Piper Pan"
    tongueTwisters = ["she sells sea shells", "peter piper pan likes pokemon"]
    return render_template("index.html", name=name, list=tongueTwisters)

@app.route("/anotherPage")
def hello1():
    return "This is another page."  

if __name__ == "__main__":
    app.run()