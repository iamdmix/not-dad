from flask import Flask, request, render_template

FLAG = "c0d{fake_flag}"

app = Flask(__name__)

qna = {
    "dob": "May 26, 1974",
    "org": "Satara, Maharashtra, India",
    "mcycle": "Royal Enfield Classic 500",
    "cuisine": "Italian cuisine",
    "curr": "Stockholm, Sweden",
    "track": "Tarmac",
    "degree": "Mechanical Engineering",
    "rally": "WRC EKO Acropolis Rally Greece",
    "next": "WRC Rally Chile Bio Bio",
    "team": "Subaru World Rally Team (SWRT)",
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        for key, value in qna.items():
            if request.form.get(key) != value:
                return "Wrong answer! Try again."
        return FLAG

    return render_template("ques.html")

app.run('0.0.0.0', 8080)