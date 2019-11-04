from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def prva_stran():
    return render_template("Homepage.html")

@app.route("/boggle")
def bogle():
    return render_template("boggle.html")


@app.route("/Fakebook")
def fakebook():
    return render_template("Fakebook.html")

if __name__ == '__main__':
    app.run()
