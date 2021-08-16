from flask import Flask, render_template


app = Flask(__name__)

votes = 0

@app.route("/up", methods=["POST"])
def upvote():
    global votes
    votes = votes + 1
    return str(votes)

@app.route("/down", methods=["POST"])
def downvote():
    global votes
    if votes >= 1:
        votes = votes - 1
    return str(votes)

@app.route("/")
def index():
    return render_template("index.html", votes=votes)