from flask_login import UserMixin
from flask_mysqldb import MySQL

from db import get_db

class UserEvent():
    def __init__(self, id_, email, emails, dateStart, dateEnd, titre, isValid):
        self.id = id_
        self.email = email
        self.emails = emails
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.titre = titre
        self.isValid

    @staticmethod
    def get(userEvent_id):
        db = get_db()
        userEvents = db.execute(
            "SELECT * FROM userEvent WHERE rowid = %s", (userEvent_id,)
        ).fetchall()
        if not userEvents:
            return None

        return userEvents

    @staticmethod
    def create(mysql, email, emails, dateStart, dateEnd, titre):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userEvent (email, emails, dateStart, dateEnd, titre)"
            " VALUES (%s, %s, %s, %s, %s)", [email, emails, dateStart, dateEnd, titre] )
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def clean(mysql, email):

        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM userEvent WHERE email = '"+email+"'")
        mysql.connection.commit()
        cur.close()
