# making class
class Add:
      # class Attribute
      var = 1
      var1 = 2

      # initializer / Instances Attributes
      def __init__(self):
            self.var = 5
            self.var1 = 10

      # instance method
      def calculate(self):
            # variables of instance attributes
            print("var=",self.var)
            print("var1=",self.var1)
            init_sum = (self.var+self.var1)
            print("sum is",init_sum)
            # variable of class arguments
            print("var=",Add.var)
            print("var1=",Add.var1)
            class_sum = Add.var+Add.var1
            print("sum is",class_sum)

# call our instance methods
a1=Add()
a1.calculate()
