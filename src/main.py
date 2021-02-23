from database import Database
from os import getenv
from dotenv import load_dotenv
load_dotenv()


def display_hello():
    """Function display hello message for user"""
    print('''Hello in our Bank System. We hope you enjoy our service!''')
    print('''Log-in to your account. If you still don\'t have account in our Bank, please $ign-in
    1. Log-in
    2. Sign-in''')
    choice = input("Choice, please.: ")
    if choice == "1":
        login()
    if choice == "2":
        signin()


def login() -> tuple:
    db = Database(getenv('DB_NAME'))
    while True:
        login = input("Please enter your login: ")
        passwd = input("and password: ")

        user = db.get_user('users', login, passwd)
        if user is False:
            print("No user in database")
        else:
            print(f"Hi {user[1]}")
            return user


def signin():
    db = Database(getenv('DB_NAME'))
    while True:
        login = input("Please enter your login: ")
        isupper = False
        isint = False
        while isupper is False or isint is False:
            passwd = input("and password (Remember u have to place min. one upper letter and one int): ")
            for i in passwd:
                if i.isupper(): isupper = True
                if i.isalnum(): isint = True
        if db.check_login_taken('users', login) is True:
            db.add_user('users', login.lower(), passwd)
            print("Register Complete")
            break
        else:
            print("Login is Taken! Try Again.")


def main():
    display_hello()


if __name__ == '__main__':
    main()
