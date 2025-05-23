from flask import Flask, render_template, url_for, request, redirect
import uuid

app = Flask(__name__)

todos = [
    {'id': 1, 'name': 'Write SQL', 'checked': False},
    {'id': 2, 'name': 'Write Python', 'checked': False},
]

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        todo_name = request.form["todo_name"]
        cur_id = uuid.uuid4().int
        todos.append({'id': cur_id, 'name': todo_name, 'checked': False})
    return render_template("index.html", items=todos)

@app.route("/checked/<int:todo_id>", methods=["POST"])
def checked_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['checked'] = not todo['checked']
            break
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for("home"))

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
