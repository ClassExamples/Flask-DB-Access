from flask import Flask
from db_helper import StudentRecordHelper, connect_db

app = Flask(__name__)

db = connect_db()
st_db_helper = StudentRecordHelper(db)


@app.route("/")
def index():
    students = st_db_helper.get_all()
    display = ""
    for st in students:
        display = f"{display} </br> {st.name}-{st.dob}"
    return display


if __name__ == "__main__":
    app.run(debug=True)
