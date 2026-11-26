class Calculator():

    def __init__(self, number):
        self.number=number
        print(f"The square of the number is {self.square()}")
        print(f"The cube of the number is {self.cube()}")
        print(f"The square root of the number is {self.square_root()}")
        

    def square(self):
        return self.number * self.number
    def cube(self):
        return self.number* self.number * self.number
    def square_root(self):
        return self.number**0.5
    

square=Calculator(2)



        