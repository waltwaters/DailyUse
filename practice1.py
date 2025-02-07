# to do list app: web-based
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list (use a database for persistence in production)
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    description = request.form.get("description")
    date = request.form.get("date")  # Get the date from the form
    notes = request.form.get("notes")  # Get the notes from the form

    if description:
        tasks.append({
            "description": description,
            "date": date,
            "notes": notes,
            "completed": False
        })
    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
