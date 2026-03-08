from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "akash_2001"

@app.route("/", methods=["GET", "POST"])
def home():

    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["count"] = 0

    message = None

    if request.method == "POST":
        guess = int(request.form["guess"])
        session["count"] += 1

        if guess == session["number"]:
            message = "win"
            number = session["number"]
            count = session["count"]

            session.clear()

            return render_template(
                "index.html",
                message=message,
                number=number,
                count=count
            )

        elif guess > session["number"]:
            message = "lower"

        else:
            message = "higher"

    return render_template(
        "index.html",
        message=message,
        count=session.get("count", 0),
        number=session.get("number")
    )


if __name__ == "__main__":
    app.run(debug=True)