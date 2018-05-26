from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/")
def index():
    #return "Hello tongue twisters!"
    name="Peter Piper Pan"
    tongueTwisters = ["she sells sea shells", "peter piper pan likes pokemon"]
    return render_template("index.html", name=name, list=tongueTwisters)

@app.route("/selectPage1")
def selectPage1():
    #return "This is another page."  
    return render_template("selectTTPage1.html")

@app.route("/selectPage2")
def selectPage2():
    #return "This is another page."  
    return render_template("selectTTPage2.html")

@app.route("/selectPage3")
def selectPage3():
    #return "This is another page."  
    return render_template("selectTTPage3.html")

if __name__ == "__main__":
    app.run()