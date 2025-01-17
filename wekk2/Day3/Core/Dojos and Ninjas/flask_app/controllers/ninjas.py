from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)


@app.route("/ninjas/create", methods=["POST"])
def create_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect("/dojos")