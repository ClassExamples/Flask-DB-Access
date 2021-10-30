from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost/student_details'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

admin = User(username='admin', email='admin@example.com')
db.session.add(admin)
db.session.commit()

print(User.query.all())

@app.route("/")
def index():
    pass


if __name__ == "__main__":
    app.run(debug=True)
