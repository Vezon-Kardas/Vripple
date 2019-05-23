import sqlite3
import datetime

class Database(object):

    def __init__(self, path, text, original_img_path, path_table):
        self.path = path
        self.text = text
        self.original_img_path = original_img_path
        self.path_table = path_table
    def addDataRetrieval(self):
        today = datetime.datetime.today().strftime("%d.%m.%Y")
        link = "piu@yandex.ru/Photo/{0}.jpg".format(self.original_img_path)

        connection = sqlite3.Connection(self.path, check_same_thread=False)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO " + self.path_table+ " (link_photo, date, text) VALUES(?,?,?)", [link, today, self.text])
        connection.commit()

        cursor.execute("SELECT id FROM "+self.path_table+" WHERE rowid=last_insert_rowid()")
        id = cursor.fetchone()
        id = str(*id)
        connection.close()
        return today, id



#p = Database("pirogow.alesha@yandex.ru/pirogow.alesha@yandex.ru.db", "I am Jedi")
#print(p.addDataRetrieval())
