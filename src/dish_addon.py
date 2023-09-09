class DishAddOn:

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.is_available = True

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def get_is_available(self):
        return self.is_available

    def set_is_available(self, is_available):
        self.is_available = is_available
