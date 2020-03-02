class Time:
    h = 0
    m = 0

    def accept(self):
        print("Enter time in hours and minutes")
        self.h = int(input())
        self.m = int(input())

    def display(self):
        print(self.h, "hours and", self.m, "minutes")


class final_time:
    h = 0
    m = 0

    def accept(self, t):
        self.h = t.h
        self.m = t.m

    def sum(self, t1,  t2):
        self.m = t1.m + t2.m
        self.h = self.m/60
        self.m = self.h + t1.h + t2.h

    def display(self):
        print(self.h, "hours and", self.m, "minutes")

t1_obj = Time()
t1_obj.accept()
t2_obj = Time()
t2_obj.accept()
t3 = final_time()
t3.accept(t1_obj)
t3.accept(t2_obj)

t3.sum(t1_obj, t2_obj)
print("t1_obj=")
t1_obj.display()
print("t2_obj=")
t2_obj.display()
print("t3=")
t3.display()
