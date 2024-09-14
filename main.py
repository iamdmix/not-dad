from flask import Flask, request, render_template

FLAG = "c0d{fake_flag}"

app = Flask(__name__)

# Dictionary of questions and valid answers
qna = {
    "dob": [
        "May 26, 1974", "26 May 1974", "1974-05-26", "26-05-1974",
        "1974/05/26", "26/05/1974", "26 05 1974", "1974 05 26",
        "26th May 1974", "Twenty sixth of May, 1974",
        "May 26th, 1974", "26th, May 1974", "1974, May 26",
        "26, May 1974", "May 26, 1974 CE", "26 May 1974 AD",
        "26th of May, '74", "May 26, '74", "5/26/74", "26.05.1974"
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
        "Classic 500", "RE Classic 500"
    ],
    "cuisine": [
        "Italian cuisine", "Italian", "Italian food",
        "Italian dishes", "Italian meals"
    ],
    "curr": [
        "Stockholm, Sweden", "Stockholm", "Stockholm, SE",
        "Stockholm, Sverige", "Swedish capital",
        "Capital of Sweden",
        "Stockholm, the capital city of Sweden",
        "Stockholm, Sweden (Scandinavia)"
    ],
    "track": [
        "Tarmac"
    ],
    "degree": [
        "Mechanical Engineering", "Mech Engg", "Mech Engineering",
        "Mechanical Engg", "Mech E", "B.Tech Mechanical", "M.Tech Mechanical",
        "Mechanical Engineer", "Mechanical Engineering Degree",
        "Bachelor of Technology (B.Tech.) in Mechanical Engineering",
        "Mech. Engg.", "Mechanical", "Mech"
    ],
    "rally": [
        "WRC EKO Acropolis Rally Greece", "Acropolis Rally Greece",
        "EKO Acropolis Rally", "Acropolis Rally", "WRC Acropolis", "Greece"
    ],
    "next": [
        "WRC Rally Chile Bio Bio", "Rally Chile Bio Bio",
        "Chile Rally", "Rally Chile", "WRC Chile Rally", "Chile"
    ],
    "team": [
        "Subaru World Rally Team (SWRT)", "SWRT", "Subaru World Rally Team",
        "Subaru Rally Team", "Subaru WRT", "Subaru",
        "Subaru Racing"
    ]
}

# User-friendly field names for displaying errors
field_labels = {
    "dob": "Date of Birth",
    "org": "Place of Origin",
    "mcycle": "Favorite Motorcycle",
    "cuisine": "Favorite Cuisine",
    "curr": "Current Residence",
    "track": "Favorite Track Type",
    "degree": "Degree",
    "rally": "Recent Rally Event",
    "next": "Next Rally Event",
    "team": "Rally Team"
}

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Handle GET and POST requests for the root URL.
    
    On GET request, renders the form. On POST request, processes form data,
    checks answers, and returns appropriate response.
    """
    if request.method == "POST":
        incorrect_fields = []
        
        # Check user's answers against valid answers
        for key, valid_answers in qna.items():
            user_input = request.form.get(key, "").strip().lower()
            valid_lower = [answer.lower() for answer in valid_answers]
            
            if user_input not in valid_lower:
<<<<<<< HEAD
                return f"Wrong answer! Try again."
=======
                incorrect_fields.append(field_labels.get(key, key))
        
        # Return message if there are incorrect answers
        if incorrect_fields:
            incorrect_list = ", ".join(incorrect_fields)
            return f"Wrong answer! The following fields are incorrect: {incorrect_list}"
        
        # Return the flag if all answers are correct
>>>>>>> 9322ef3 (Fix: removed the wrong options)
        return FLAG

    # Render the form template on GET request
    return render_template("ques.html")

# Run the Flask app
app.run('0.0.0.0', 8080)
