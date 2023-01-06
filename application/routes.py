from application import app, todo
from flask import render_template, request, url_for, flash, redirect
from .forms import TodoForm
from datetime import datetime

@app.route("/")
def home_page():
    return render_template("view_todos.html", title="View")

@app.route("/add_todo", methods=["GET", "POST"])
def add_todo_page():
    if request.method == "POST":
        form = TodoForm(request.form)
        name = form.name.data
        description = form.description.data
        completed = form.completed.data

        todo.insert_one({
            "name": name,
            "description": description,
            "completed": completed,
            "completed_date": datetime.utcnow()
        })

        flash("Todo added successfully!", "success")
        return redirect(url_for("home_page"))
    form = TodoForm()
    return render_template("add_todo.html", form=form)


