import csv

class Item: 
    pay_rate = 0.8 # the pay rate after 20% discount
    all = [] # empty list to stack all objects
     
    def __init__(self, name: str, price: float, quantity: int = 0):  
       # Run validations to the received arguments  
       assert price >= 0, f"{price} should not be negative"
       assert quantity >= 0, f"{quantity} should not be negative"
       
       # Assign to self object 
       self.name = name
       self.price = price 
       self.quantity = quantity
       
       # Run Actions
       Item.all.append(self) 
       
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
    
# Inheritance 
class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity: int = 0, broken_items: int = 0):  
        # Run validations to the received arguments  
        assert price >= 0, f"{price} should not be negative"
        assert quantity >= 0, f"{quantity} should not be negative"
        assert broken_items >= 0, f"{broken_items} should not be negative"

        # Assign to self object 
        self.name = name
        self.price = price 
        self.quantity = quantity
        self.broken_items = broken_items

        # Run Actions
        Phone.all.append(self) 
    

phone1 = Phone("JSOCPhonev10", 10, 5, 2)
print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)