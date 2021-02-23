import sqlite3
from sys import argv
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def add_user(self, table_name, login, passwd):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES (Null, '{login}', '{passwd}', 0)")
        self.connection.commit()

    def get_user(self, table_name, user):
        self.cursor.execute(f'SELECT * FROM {table_name} WHERE id=? AND login=?', (user, 'Aldona'))
        print(self.cursor.fetchone())


if len(argv) > 1 and argv[1] == 'setup':
    print("Creating Table in Datebase")
    db = Database(getenv('DB_NAME'))
    db.create_table('''CREATE TABLE users
         (id  INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT, amount REAL)''')

if len(argv) == 5 and argv[1] == 'add':
    print("Creating Table in Datebase")
    db = Database(getenv('DB_NAME'))
    table_name = argv[2]
    login = argv[3]
    password = argv[4]
    db.add_user(table_name, login, password)

if len(argv) > 1 and argv[1] == 'get':
    print("User is")
    db = Database(getenv('DB_NAME'))
    db.get_user('users', '1')
