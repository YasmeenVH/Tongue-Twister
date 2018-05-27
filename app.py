from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from processing import *

app = Flask(__name__)

labelMap = {
    "clam": "How can a clam cram in a clean cream can?",
    "can": "Can you can a can as a can opener can?",
    "noisy": "A noisy noise annoys an oyster",
    "seashells": "She sells sea shells by the seashore"
}

#get_audio?tt="" 
#pete, wood

@app.route("/get_audio", methods=['GET'])
def getAudio():
    tt = request.args.get('tt', '')
    if tt == "clam":
        #audioLink = "https://github.com/anna-ilina/ai-tongue-twisters/blob/master/static/index_files/clam.wav"
        audioLink = "https://raw.githubusercontent.com/anna-ilina/ai-tongue-twisters/master/static/index_files/clam.wav"
    elif tt == "can":
        audioLink = "https://raw.githubusercontent.com/anna-ilina/ai-tongue-twisters/master/audio_files/can.wav"
    elif tt == "noisy":
        audioLink = "https://raw.githubusercontent.com/anna-ilina/ai-tongue-twisters/master/audio_files/noisy.wav"
    elif tt == "seashells":
        audioLink = "https://raw.githubusercontent.com/anna-ilina/ai-tongue-twisters/master/audio_files/sea%20shells.wav"
    else:
        audioLink = ""
    if tt == "clam":
        audioLink = ""

    text = labelMap[tt]

    # [result_string, result_array] = speech_to_text(os.path.join("audio_files", "sea shells.wav")) 

    # result = find_error(tt, [result_string, result_array], "sh")

    # resultString = ""
    # if result == False:
    #     pass
    # else:
    #     pass

    return jsonify({"url":audioLink})

@app.route("/process_audio", methods=['GET'])
def processAudio():
    tt = request.args.get('tt', '')
    text = labelMap[tt]

    recording = request.files['file[]']

    #[result_string, result_array] = speech_to_text(os.path.join("audio_files", "sea shells.wav")) 

    actual = speech_to_text('correct.wav')
    test = speech_to_text('wrong.wav')

    result = find_error(actual, test, ["sh", "se"])

    # result = find_error(tt, [result_string, result_array], "sh")

    return jsonify({"text":result})







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