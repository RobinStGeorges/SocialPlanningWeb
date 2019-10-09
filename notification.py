from flask_login import UserMixin
from dateutil.parser import parse as dtparse
from datetime import datetime as dt
import datetime


class notification():
    def __init__(self, id_, email, content, idEvent, accepted):
        self.id = id_
        self.email = email
        self.content = content
        self.idEvent = idEvent
        self.accepted = accepted

    @staticmethod
    def get(mysql, email):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM notification WHERE email = %s", [email] )
        notifs = cur.fetchall()
        if not notifs:
            print("pas de notifications dans la database")
            return None
        return notifs

    @staticmethod
    def getById(mysql, id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM GoogleEvent WHERE id = %s", [id] )
        notif = cur.fetchone()
        if not notif:
            print("pas de notif dans la database par id")
            return None
        return notif

    @staticmethod
    def create(mysql, email, content, idEvent, accepted):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO notification(email, content, idEvent, accepted) VALUES (%s, %s, %s, %s)", [email, content, idEvent, accepted] )
        mysql.connection.commit()
        cur.close()


def create(mysql, email, content, idEvent, accepted):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO notification(email, content, idEvent, accepted) VALUES (%s, %s, %s, %s)", [email, content, idEvent, accepted] )
    mysql.connection.commit()
    cur.close()


def get(mysql, email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM notification WHERE email = %s", [email] )
    notifs = cur.fetchall()
    if not notifs:
        print("pas de notifications dans la database")
        return None
    return notifs

def getById(mysql, id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM notification WHERE id = %s", [id] )
    notif = cur.fetchone()
    if not notif:
        print("pas de notification dans la database")
        return None
    return notif


def setStatusById(mysql, idNotif, value):
    print("idNotif, value")
    print(idNotif)
    print(value)
    cur = mysql.connection.cursor()
    cur.execute("UPDATE notification SET accepted = %s WHERE id = %s", [value, idNotif] )
    mysql.connection.commit()
    return None
