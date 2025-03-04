import csv

class Item: 
    pay_rate = 0.8 # the pay rate after 20% discount
    all = [] # empty list to stack all objects
     
    def __init__(self, name: str, price: float, quantity: int = 0):  
       # Run validations to the received arguments  
       assert price >= 0, f"{price} should not be negative"
       assert quantity >= 0, f"{quantity} should not be negative"
       
       # Assign to self object 
       self.__name = name # adding one underscore makes it accessible but can't alter the value 
       # adding two underscores will it make it completely private(no write or read)
       self.price = price 
       self.quantity = quantity
       
       # Run Actions
       Item.all.append(self) 
       
    @property # a getter method (coz you're trying to get the name)
    # property decorater = read only attribute 
    def name(self): 
        ''' 
        This is a read only attribute and if you try to change it you'll get 
        an attribute error     
        '''
        return self.__name
    
    # even though you set name as private you can use a setter method to change that private attribute
    # (it is confusing indeed)
    
    @name.setter # a setter method (coz you're trying to set the name)
    def name(self, value): 
        if len(value) > 10: 
            raise Exception("The item name is too long")
        else: 
            self.__name = value
    
    @classmethod 
    def instanciate_from_csv(cls): 
        with open('items.csv', 'r') as file: 
            reader = csv.DictReader(file)
            items = list(reader)
        
        for item in items: 
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num): # gonna check if the num is floating or not using the isinstance() function
        if isinstance(num, float): 
            #excludes the floats with .0 i.e 7.0, 10.0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: 
            return False

    def calculate_total_price(self):   
        return self.price * self.quantity
     
    def apply_discount(self): 
        return self.price * self.pay_rate 
    
    def __repr__(self): 
        # self.class.name is a generic way of accessing the name of the class 
        return f"{self.__class__.__name__}('{self.name}'),Item('{self.price}'),Item('{self.quantity}'), "
    