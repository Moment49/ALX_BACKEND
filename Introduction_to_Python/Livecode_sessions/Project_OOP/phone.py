from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call the super function to have access to all attrbutes/methods of the parent class
        super().__init__(name, price, quantity)
        # Run validations to the recieved arguments
        assert broken_phones >= 0
        self.broken_phone = broken_phones