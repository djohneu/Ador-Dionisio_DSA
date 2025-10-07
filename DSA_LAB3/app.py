from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route("/touppercase", methods=["GET", "POST"])
def touppercase():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = text.upper()
    return render_template("touppercase.html", result=result)

@app.route("/triangle", methods=["GET", "POST"])
def triangle():
    area = None
    if request.method == "POST":
        base = float(request.form["base"])
        height = float(request.form["height"])
        area = 0.5 * base * height
    return render_template("triangle.html", area=area)

@app.route("/circle", methods=["GET", "POST"])
def circle():
    area = None
    if request.method == "POST":
        radius = float(request.form["radius"])
        area = 3.14159 * radius * radius
    return render_template("circle.html", area=area)

if __name__ == "__main__":
    app.run(debug=True)
