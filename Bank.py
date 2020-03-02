for i in range(1, 3):
    class Bank(object):
        name = ""
        acctno = 0
        initial_bal = 0.0
        amt = 0

        def accept(self):
            print("WELCOME TO ABC BANK")
            print("   ")
            print("PLEASE ENTER YOUR DETAILS")
            self.name = input("ENTER YOUR NAME = ")
            self.acctno = int(input("ENTER YOUR ACCOUNT NO. = "))
            self.initial_bal = 5000
            print("YOUR BALANCE IS = ", self.initial_bal)
            print("Customer Details")
            print("NAME = ", self.name, "       ACCOUNT NO. = ", self.acctno)
            print("CURRENT BALANCE = ", self.initial_bal)

        def deposit(self):
            print("enter amount to be deposited")
            self.amt = int(input())
            self.initial_bal = self.initial_bal + self.amt
            print("update balance is", self.initial_bal)

        def withdraw(self):
            print("enter amount to be withdraw")
            self.amt = int(input())
            self.initial_bal = self.initial_bal - self.amt
            print("update balance is", self.initial_bal)
            print("     ")
            print("------------------------------------")

    b1 = Bank()
    b1.accept()
    b1.deposit()
    b1.withdraw()
