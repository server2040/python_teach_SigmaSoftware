
class Pizza():

    order_count = 0

    def __init__(self, ingr):
        Pizza.order_count += 1
        self.order_number = Pizza.order_count
        self.ingredients = ingr

    @classmethod
    def pepperoni(cls):
        return cls( ['bacon', 'mozzarella', 'oregano'] )

    @classmethod
    def hawaiian(cls):
        return cls( ['ham', 'pineapple'] )
 
    @classmethod
    def margherita(cls):
        return cls( ['mozzarella', 'olives', 'tomatoes'] )


p1 = Pizza( ['bacon', 'parmesan', 'ham'] )    # order 1
p2 = Pizza.pepperoni()                        # order 2          

print( p1.ingredients )
print( p1.order_number )

print( p2.ingredients )
print( p2.order_number )

