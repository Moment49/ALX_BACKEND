from item import Item

class Speaker(Item):
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity=0):
        # Call the super function to have access to all attrbutes/methods of the parent class
        super().__init__(name, price, quantity)
        # Run validations to the recieved arguments
    