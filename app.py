from flask import Flask, render_template, request
import random

app = Flask(__name__)

number = random.randint(1, 100)
count = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global count
    message = ""
    guess = None

    if request.method == "POST":
        guess = int(request.form["guess"])
        count += 1

        if guess == number:
            message = "win"
        elif guess > number:
            message = "lower"
        else:
            message = "higher"

    return render_template("index.html",
                           guess=guess,
                           count=count,
                           number=number,
                           message=message)

if __name__ == "__main__":
    app.run(debug=True)