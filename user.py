from flask_login import UserMixin

from db import get_db


class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic, familly_name, locale):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.familly_name = familly_name
        self.locale = locale
        self.tokenPath =name+familly_name+'.pickle'

    @staticmethod
    def get(mysql, user_id):

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE id = %s", [user_id] )
        user = cur.fetchone()
        if not user:
            return None
        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3], familly_name = user[4], locale = user[5]
        )
        return user

    @staticmethod
    def create(mysql, id_, name, email, profile_pic, familly_name, locale):
        tokenPath = name.replace(" ","" ) + "token.pickle"
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (id, name, email, profile_pic, familly_name, locale, tokenPath) VALUES (%s, %s, %s, %s, %s, %s, %s)", [id_, name, email, profile_pic, familly_name, locale, tokenPath] )
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete(mysql, email):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM user WHERE email = '"+email+"'")
        cur.close()


def delete(mysql, email):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM user WHERE email = '"+email+"'")
    cur.close()
