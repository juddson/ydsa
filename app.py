from flask import Flask, render_template
app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html", active_page="home")

@app.route("/about")
def about():
    return render_template("about.html", active_page="about")

@app.route("/join")
def join():
    return render_template("join.html", active_page="join")

if __name__ == "__main__":
    # Codespaces forwards ports automatically
    app.run(host="0.0.0.0", port=5000, debug=True)
