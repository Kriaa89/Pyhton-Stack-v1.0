from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojos)


@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/dojos")
