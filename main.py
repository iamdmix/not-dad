from flask import Flask, request, render_template

FLAG = "c0d{fake_flag}"

app = Flask(__name__)

qna = {
    "dob": [
        "May 26, 1974", "26 May 1974", "1974-05-26", "26-05-1974",
        "1974/05/26", "26/05/1974", "26 05 1974", "1974 05 26",
        "26th May 1974", "Twenty sixth of May, 1974",
        "May 26th, 1974", "26th, May 1974", "1974, May 26",
        "26, May 1974",
        "May 26, 1974 CE", "26 May 1974 AD",
        "26th of May, '74", "May 26, '74",
        "5/26/74", "26.05.1974"
    ],
    "org": [
        "Satara, Maharashtra, India", "Satara", "Maharashtra",
        "Satara, MH", "Satara, India", "Satara district",
        "Satara, Maharashtra State", "Satara, Western India",
        "Satara, India (Western Ghats)", "Satara, Maharashtra, India (Western Ghats)",
        "Satara, Western India (Maharashtra)"
    ],
    "mcycle": [
        "Royal Enfield Classic 500", "Royal Enfield 500",
        "Classic 500", "RE Classic 500", "RE 500",
        "Royal Enfield", "Bullet",
        "Royal Enfield Interceptor 650", "Royal Enfield Continental GT 650",
        "Royal Enfield Classic 350", "Royal Enfield Bullet 350",
        "RE Bullet", "RE Classic"
    ],
    "cuisine": [
        "Italian cuisine", "Italian", "Italian food",
        "Italian dishes", "Italian meals", "Pasta", "Pizza",
        "Spaghetti", "Lasagna", "Risotto", "Tiramisu",
        "Italian-American cuisine", "Sicilian cuisine",
        "Pizza Margherita", "Pasta Carbonara"
    ],
    "curr": [
        "Stockholm, Sweden", "Stockholm", "Stockholm, SE",
        "Stockholm, Sverige", "Swedish capital",
        "Capital of Sweden",
        "Stockholm, the capital city of Sweden",
        "Stockholm, Sweden (Scandinavia)"
    ],
    "track": [
        "Tarmac", "Asphalt", "Road", "Blacktop", "Paved road",
        "Race track", "Circuit", "F1 track",
        "Circuit de Barcelona-Catalunya", "Silverstone Circuit",
        "Formula 1 track", "Grand Prix circuit"
    ],
    "degree": [
        "Mechanical Engineering", "Mech Engg", "Mech Engineering",
        "Mechanical Engg", "Mech E", "B.Tech Mechanical", "M.Tech Mechanical",
        "Mechanical Engineer", "Mechanical Engineering Degree",
        "Bachelor of Technology (B.Tech.) in Mechanical Engineering",
        "Mech. Engg."
    ],
    "rally": [
        "WRC EKO Acropolis Rally Greece", "Acropolis Rally Greece",
        "EKO Acropolis Rally", "Acropolis Rally", "WRC Acropolis",
        "WRC Rally Chile Bio Bio", "Rally Chile Bio Bio",
        "Chile Rally", "Rally Chile", "WRC Chile Rally",
        "WRC Rally Finland", "WRC Rally Monte Carlo",
        "Rallying event", "Rally competition"
    ],
    "next": [
        "WRC Rally Chile Bio Bio", "Rally Chile Bio Bio",
        "Chile Rally", "Rally Chile", "WRC Chile Rally",
        "WRC Rally Japan", "WRC Rally Mexico"
    ],
    "team": [
        "Subaru World Rally Team (SWRT)", "SWRT", "Subaru World Rally Team",
        "Subaru Rally Team", "Subaru WRT", "Subaru",
        "Subaru Racing",
        "Hyundai Motorsport", "Toyota Gazoo Racing"
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        for key, valid_answers in qna.items():
            user_input = request.form.get(key).lower()  # Convert input to lowercase
            valid_lower = [answer.lower() for answer in valid_answers]  # Convert valid answers to lowercase
            if user_input not in valid_lower:
                return f"Wrong answer! Try again. {user_input}"
        return FLAG

    return render_template("ques.html")

app.run('0.0.0.0', 8080)