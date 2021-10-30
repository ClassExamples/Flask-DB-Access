from flask import Flask, render_template, request
from db_example import Student
from db_helper import StudentRecordHelper, connect_db

app = Flask(__name__)

db = connect_db()
st_db_helper = StudentRecordHelper(db)


@app.route("/")
def index():
    students = st_db_helper.get_all()
    context = {
        "name": "Student List",
        "students": students
    }
    return render_template("index.html.j2", **context)


@app.route("/student/create", methods=["GET", "POST"])
def insert_student():
    if request.method == "POST":
        data = request.form
        st = (data.get("name"), data.get("dob"), data.get("grade"),
              data.get("address"), data.get("parent_name"))
        st_db_helper.insert(st)

    return render_template("student/create.html.j2")


if __name__ == "__main__":
    app.run(debug=True)
