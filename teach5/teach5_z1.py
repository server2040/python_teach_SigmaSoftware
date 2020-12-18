

class Calculator():

    def add(self, a: float, b: float):
        return a + b

    def subtcact(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float):   # -> float,str
        return a / b if b != 0 else 'Error: Division by zerro' 

    def exponent(self, a: float, b: float) -> float:
        return a ** b


a = float( input('input a: '))
b = float( input('input b: '))

calculator = Calculator()

print( f'\nclass calculator methods:')
print( f' .add({a}, {b}) -> ', calculator.add(a, b) )
print( f' .subtcact({a}, {b}) -> ', calculator.subtcact(a, b) )
print( f' .multiply({a}, {b}) -> ', calculator.multiply(a, b) )
print( f' .divide({a}, {b}) -> ', calculator.divide(a, b) )
print( f' .exponent({a}, {b}) -> ', calculator.exponent(a, b) )
