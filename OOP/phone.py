from item import Item

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