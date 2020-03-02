# making class
class Email:

    # initializer / Instance Attributes
    def __init__(self):
        self.is_sent = False

    # instance method
    def send_email(self):
        self.is_sent = True

# calling class by assigning in variable
my_email = Email()
print(my_email.is_sent)
my_email.send_email()
print(my_email.is_sent)
