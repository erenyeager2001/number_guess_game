from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "akash_2001"

@app.route("/", methods=["GET", "POST"])
def home():

    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["count"] = 0
        print(session["count"])

    message = None

    if request.method == "POST":
        guess = int(request.form["guess"])
        session["count"] += 1

        if guess == session["number"]:
            message = "win"
            return render_template(
                "index.html",
                message=message,
                number=session["number"],
                count=session["count"]
            )

        elif guess > session["number"]:
            message = "lower"

        else:
            message = "higher"

    return render_template(
        "index.html",
        message=message
    )


@app.route("/replay")
def replay():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)