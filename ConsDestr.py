class Rectangle:
    def __init__(self, width, height):
        print("I am initializing a new Rectangle Instance.")
        self.width = width
        self.height = height
        print("The width is :", self.width)
        print("The heightidth is :", self.height)

    def __del__(self):
        print("A Rectangle instance is being destroyed. ")

Rectangle(120, 70)
