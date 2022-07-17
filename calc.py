class Calc:

    def __init__ (self):
        self.value = 0

    def add(self, new_val):
        self.value += new_val
        yield self.value
    def sub(self, new_val):
        self.value -= new_val
        yield self.value



calc = Calc()

print(list(calc.add(5)))