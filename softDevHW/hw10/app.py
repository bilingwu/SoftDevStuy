from flask import Flask, render_template, redirect, request
import utils

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return redirect('/{}'.format(request.form.get('location').replace(" ","_")))

@app.route("/<location>",methods = ["GET","POST"])
def page(location):
    info = utils.getWiki(location)
    if info:
        info = info.decode("utf-8")
    coord = utils.coordinates(location)
    return render_template("page.html", location = location, info = info, coord = coord)
    
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Idk"
    app.run(host = "0.0.0.0", port = 8000)
