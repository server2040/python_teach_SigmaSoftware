
class Human( ):

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name.capitalize()
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return  self.first_name +' '+ self.last_name

    
class Employee(Human):

    def __init__(self, first_name: str, last_name: str, salary: int):
        super().__init__( first_name, last_name )
        self.salary = salary

    @classmethod
    def from_string(cls, param):
        params = param.split( '-' )
        first_name = params[0]
        last_name = params[1]
        salary = params[2]
        return cls( first_name , last_name , salary )


emp1 = Employee('JOAN', 'Smith', 85000)
emp2 = Employee.from_string('John-doe-73000')

print( emp1.first_name ) # ➞ 'Joan'
print( emp1.full_name ) #➞ 'Joan Smith'
print( emp1.salary ) # ➞85000
print( emp2.first_name ) # ➞ 'John'
print( emp2.full_name ) # ➞ 'John Doe'
print( emp2.salary ) # ➞73000
