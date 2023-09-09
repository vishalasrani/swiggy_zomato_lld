class Cart:

    def __init__(self):
        self.restaurant_id = None
        self.items = {}

    def add_items_to_cart(self, dish_id, qty):
        self.items.update({
            "dish": dish_id,
            "quantity": qty
        })
        return

    def update_restaurant(self, restaurant_id):
        self.restaurant_id = restaurant_id
        self.items = {}

    def get_restaurant_id(self):
        return self.restaurant_id

    def get_items_in_cart(self):
        return self.items
