# importing tkinter module
from tkinter import *
root = Tk()

# calling var_states when clicked on button
def var_states():
    print("Hoppy 1: %d, \nHobby 2: %d, \nHobby 3: %d" % (var1.get(), var2.get(), var3.get()))

#creating variable like IntVar for getting the value of checkButton (1 or 0)
var1 = IntVar()
c1 = Checkbutton(root, text="Hobby 1", variable=var1)

var2 = IntVar()
c2 = Checkbutton(root, text="Hobby 2", variable=var2)

var3 = IntVar()
c3 = Checkbutton(root, text="Hobby 3", variable=var3)
b = Button(root, text="Show", command=var_states)
# packing to display in gui window
c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)
b.pack(side=LEFT)
# mainloop of tkinter program
root.mainloop()
