from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Todo
from app import db

main = Blueprint('main', __name__)

# Home Page
@main.route('/')
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


# Add Todo
@main.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        flash("Taks added!")
    return redirect(url_for('main.index'))

# Mark as Done
@main.route('/done/<int:id>')
def mark_done(id):
    todo = Todo.query.get_or_404(id)
    todo.done = not todo.done
    db.session.commit()
    
    if todo.done == True:
        flash(f"Marked '{todo.task}' as done")
    else:
        flash(f"Marked '{todo.task}' as ongoing")
    return redirect(url_for('main.index'))

# Delete Todo
@main.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash(f"Deleted task: '{todo.task}'")
    return redirect(url_for('main.index'))

@main.route('/initdb')
def initdb():
    db.create_all()
    return "Database initialized!"
