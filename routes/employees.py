from app import app, db
from flask import render_template, request, redirect
from models.models import Employee


@app.route("/add-employee")
def add_employee():
    return render_template("employee.html")


@app.route("/save-employee", methods=["POST"])
def save_employee():
    name = request.form.get("name")
    type_of_work = request.form.get("type_of_work")
    employee = Employee(name=name, type_of_work=type_of_work)
    db.session.add(employee)
    db.session.commit()
    return redirect("/")
