from flask import Flask,render_template
app=Flask(__name__,template_folder="E:/CSE/sona_web")
@app.route("/")
def index():
    return render_template("first.html",email="rrvp@sonatecha.in",pass="password")
@app.route("/mainpage")
def mainpage():
    return render_template("mainpage.html")
@app.route("/user")
def user():
    return render_template("user.html")
@app.route("/documents")
def doc():
    return render_template("documents.html")
@app.route("/activitylog")
def activity():
    return render_template("activitylog.html")
@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/unknown")
def unknown():
    return render_template("user.html")
@app.route("/backmain")
def backmain():
    return render_template("first.html")






if __name__ == '__main__':
    app.run(debug=True)
