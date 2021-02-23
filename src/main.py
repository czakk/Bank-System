from database import Database
from os import getenv
from dotenv import load_dotenv
load_dotenv()


def display_hello():
    """Function display hello message for user"""
    print('''Hello in our Bank System. We hope you enjoy our service!''')
    while True:
        print('''Log-in to your account. If you still don\'t have account in our Bank, please $ign-in
        1. Log-in
        2. Sign-in''')
        choice = input("Choice, please.: ")
        if choice == "1":
            return login()
        if choice == "2":
            signin()


def login() -> tuple:
    db = Database(getenv('DB_NAME'))
    while True:
        login = input("Please enter your login: ")
        passwd = input("and password: ")

        user = db.get_user('users', login.lower().strip(), passwd.strip())
        if user is False:
            print("No user in database")
        else:
            print(f"Hi {user[1].title()}")
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
                elif i.isnumeric(): isint = True
        if db.check_login_taken('users', login) is True:
            db.add_user('users', login.lower().strip(), passwd.strip())
            print("Register Complete")
            break
        else:
            print("Login is Taken! Try Again.")


class User:
    def __init__(self, user_info: tuple):
        self.userid = user_info[0]
        self.name = user_info[1].title()
        self.amount = user_info[3]
        self.db = Database(getenv('DB_NAME'))

    def deposit_money(self):
        while True:
            money = float(input("How much you want to deposit?: "))
            if isinstance(money, float):
                if money < 10:
                    print("U have to min. 10 credits")
                else:
                    self.amount += money
                    self.db.change_value('users', 'amount', self.amount, self.userid)
                    return self.amount
            else:
                print('Given value is not a int')

    def payout_money(self):
        while True:
            money = float(input("How much you wan to payout?: "))
            if isinstance(money, float):
                if money > self.amount or money < 0:
                    print("You trying Pay Out more money than u have")
                else:
                    self.amount -= money
                    self.db.change_value('users', 'amount', self.amount, self.userid)
                    return self.amount
            else:
                print('Given value is not a int')

    def transfer_money(self):
        while True:
            money = float(input("How much you want to transfer?: "))
            id = input("You want transfer money for:  ")
            if isinstance(money, float):
                if money > self.amount:
                    print("You trying Pay Out more money than u have")
                else:
                    customer = self.db.info_bylogin('users', id)
                    if customer is not False:
                        self.db.change_value('users', 'amount', customer[3] + money, customer[0])
                        self.amount -= money
                        self.db.change_value('users', 'amount', self.amount, self.userid)
                        return self.amount, customer[3] + money
                    else:
                        print("We can't find customer!")
            else:
                print('Given value is not a int')
                continue

    def show_account_details(self):
        while True:
            print(f'''Account Details:
            Your name: {self.name}
            Balance: {round(self.amount)}
            
            Available operations:
            1. Deposit
            2. Pay out
            3. Transfer
            4. Log Out
            ''')
            choice = input("Choice one of options: ")
            if choice == "1":
                self.deposit_money()
            if choice == "2":
                self.payout_money()
            if choice == "3":
                self.transfer_money()
            elif choice == "4":
                print("See you soon!")
                break


def main():
    user_information = display_hello()
    user = User(user_information)
    user.show_account_details()


if __name__ == '__main__':
    main()

