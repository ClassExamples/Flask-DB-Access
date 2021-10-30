import mysql.connector
from mysql.connector.connection import MySQLConnection
from collections import namedtuple

Student = namedtuple("Student", "id name dob grade address parent_name")

class StudentRecordHelper:
    db: MySQLConnection

    def __init__(self, db):
        self.db = db

    def get_all(self):
        cur = self.db.cursor()
        sql = "SELECT * FROM student"
        cur.execute(sql)
        results = cur.fetchall()
        students = []
        for re in results:
            st = Student(*re)
            students.append(st)
        return students

def connect_db() -> MySQLConnection:
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass",
        database="ijse_db_1"
    )