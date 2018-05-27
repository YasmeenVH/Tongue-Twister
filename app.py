from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

#get_audio?tt="" 
#pete, wood

@app.route("/get_audio", methods=['GET'])
def getAudio():
    tt = request.args.get('tt', '')
    if tt == "clam":
        audioLink = "https://github.com/anna-ilina/ai-tongue-twisters/blob/master/static/index_files/clam.wav"
        return jsonify({"url":audioLink})
    elif tt == "can":
        audioLink = "https://github.com/anna-ilina/ai-tongue-twisters/blob/master/audio_files/can.wav"
        return jsonify({"url":audioLink})
    elif tt == "noisy":
        audioLink = "https://github.com/anna-ilina/ai-tongue-twisters/blob/master/audio_files/noisy.wav"
        return jsonify({"url":audioLink})
    elif tt == "seashells":
        audioLink = https://github.com/anna-ilina/ai-tongue-twisters/blob/master/audio_files/sea%20shells.wav
        return jsonify({"url":audioLink})
    else:
        audioLink = ""
        return jsonify({"url":audioLink})

@app.route("/")
def index():
    
    name="Peter Piper Pan"
    tongueTwisters = ["she sells sea shells", "peter piper pan likes pokemon"]
    return render_template("index.html", name=name, list=tongueTwisters)

@app.route('/select', methods=['GET','POST'])
def select():
    name="Pinnochio"
    tongueTwisters = ["How can a clam cram in a clean cream can?",
    "She sells sea shells by the seashore.",
    "Can you can a can as a canner can can a can",
    "If Stu chews shoes, should Stu choose the shoes he chews?",
    "A noisy noise annoys an oyster."]

    if request.method == 'GET':
        return render_template("select.html", name=name, twisters=tongueTwisters)
    elif request.method == 'POST':
        return render_template("select.html", name=name, twisters=tongueTwisters)

@app.route("/selectPage1")
def selectPage1():
     
    return render_template("selectTTPage1.html")

@app.route("/selectPage2")
def selectPage2():
     
    return render_template("selectTTPage2.html")

@app.route("/selectPage3")
def selectPage3():
    
    return render_template("selectTTPage3.html")

if __name__ == "__main__":
    app.run()