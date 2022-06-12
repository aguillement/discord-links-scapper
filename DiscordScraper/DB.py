import sqlite3
import os

class Database(object):
    def __init__(self, guild, channel):
        dbfile = os.path.join(os.getcwd(), 'database', f'{guild}_{channel}.db')
        installed = True

        if not os.path.isfile(dbfile):
            installed = False

        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()

        if not installed:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS messages (created DATE, messages BLOB, UNIQUE(created))')
            self.cursor.execute('CREATE INDEX IF NOT EXISTS message_date ON messages(created)')
            self.connection.commit()
    
    def write(self, date, data):
        self.cursor.execute('REPLACE INTO messages VALUES (?, ?)', (date, data))
        self.connection.commit()
