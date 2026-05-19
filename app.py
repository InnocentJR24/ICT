from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = "sayangasd-demo-2026"

@app.route("/")
def index():
    return render_template("home.html", active="home")

@app.route("/therapy")
def therapy():
    return render_template("therapy.html", active="therapy")

@app.route("/therapy/submit", methods=["POST"])
def therapy_submit():
    data = request.json
    score = sum(1 for v in data.get("tries", []) if v == "check")
    session["score"] = score
    session["mood"]  = data.get("mood", "happy")
    return jsonify({"score": score})

@app.route("/therapy/result")
def therapy_result():
    score = session.get("score", 3)
    mood  = session.get("mood", "happy")
    bars  = [20,18,22,25,19,28,24,30,26,32,28,35,38,score*8+8]
    return render_template("therapy_result.html", active="therapy", score=score, mood=mood, bars=bars)

@app.route("/chat")
def chat():
    return render_template("chat.html", active="chat")

@app.route("/milestone")
def milestone():
    return render_template("milestone.html", active="milestone")

@app.route("/milestone/result", methods=["POST"])
def milestone_result():
    data  = request.json
    sc    = {"check":2,"partial":1,"cross":0}
    keys  = ["ms1","ms2","ms3","ms4","ms5","ms6","ms7","ms8"]
    total = sum(sc.get(data.get(k,"partial"),1) for k in keys)
    soc   = sum(sc.get(data.get(k,"partial"),1) for k in keys[:4])
    com   = sum(sc.get(data.get(k,"partial"),1) for k in keys[4:])
    pct   = round(total/(len(keys)*2)*100)
    return jsonify({"total":total,"max":len(keys)*2,"pct":pct,"social":soc,"comm":com})

@app.route("/aid")
def aid():
    return render_template("aid.html", active="aid")

@app.route("/referral")
def referral():
    return render_template("referral.html", active="referral")

@app.route("/offline")
def offline():
    return render_template("offline.html", active="offline")

@app.route("/conflict")
def conflict():
    return render_template("conflict.html", active="conflict")

if __name__ == "__main__":
    app.run(debug=True, port=5050)
