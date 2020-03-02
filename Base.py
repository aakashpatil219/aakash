# Python example to show working of multiple
# inheritance
class Base1(object):
    # initializer or instance 
    def __init__(self):
        self.str1 = "Hi"
        print ("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Hello"
        print ("Base2")

class Derived(Base1, Base2):
    
    def __init__(self):

 # caling constructor of Base1
# and Base 2 classes
Base1.__init__(self)
Base2.__init__(self)
