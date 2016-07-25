import sqlite3
import os.path
from objects.items import *

class DBConnector():
    db = ''

    def __init__(self, dbName):
        if not os.path.isfile(dbName):
            self.db = sqlite3.connect(dbName)
            self.initTables()
        else:
            self.db = sqlite3.connect(dbName)
            self.cleanDB()

    def insertItem(self, Item):
        item = [Item.name, Item.attackpower, Item.description]
        self.db.execute("INSERT INTO items VALUES (?, ?, ?)", item)
        self.db.commit()

    def getItems(self):
        result = self.db.execute("SELECT * FROM items")
        print(result.fetchall())

    def getItem(self, name):
        result = self.db.execute("SELECT * FROM items WHERE name = '%s'" % name)
        return Item(result.fetchone())

    def initTables(self):
        self.db.execute('''CREATE TABLE items
             (name text, attackpower integer, description text)''')
        self.db.commit()

    def cleanDB(self):
        self.db.execute("DELETE FROM items")
