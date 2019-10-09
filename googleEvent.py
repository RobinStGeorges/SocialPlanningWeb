from flask_login import UserMixin
from dateutil.parser import parse as dtparse
from datetime import datetime as dt
import datetime


class GoogleEvent():
    def __init__(self, id_, idGoogle, email, dateStart, dateEnd, titre):
        self.id = id_
        self.idGoogle = idGoogle
        self.email = email
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.titre = titre

    @staticmethod
    def get(mysql, email):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM googleevent WHERE email = %s", [email] )
        events = cur.fetchall()
        if not events:
            print("pas d'event dans la database")
            return None
        return events

    @staticmethod
    def getById(mysql, id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM googleevent WHERE idGoogle = %s", [id] )
        event = cur.fetchone()
        if not event:
            print("pas d'event dans la database par id")
            return None
        return event

    @staticmethod
    def create(mysql, idGoogle, email, dateStart, dateEnd, titre):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO googleevent(idGoogle, email, dateStart, dateEnd, titre) VALUES (%s, %s, %s, %s, %s)", [idGoogle, email, dateStart, dateEnd, titre] )
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def clean(mysql, email):

        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM googleevent WHERE email = '"+email+"'")
        mysql.connection.commit()
        cur.close()
