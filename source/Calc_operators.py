class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return(self.num1 + self.num2)
    def sub(self):
        return(self.num1 - self.num2)
    def mult(self):
        return(self.num1 * self.num2)
    def div(self):
        try:
            return(self.num1 / self.num2)
        except ZeroDivisionError:
            return("Error: Cannot divide by zero")
