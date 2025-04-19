from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append({"task": task, "done": False})
    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:task_id>")
def done(task_id):
    tasks[task_id]["done"] = True
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks.pop(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
