class Order:

    id = 1

    def __init__(self, user_id, restaurant_id, dishes):
        self.order_id = Order.id
        Order.id += 1
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.dishes = dishes

    def get_order_id(self):
        return self.order_id

    def get_restaurant_id(self):
        return self.restaurant_id

    def get_dishes(self):
        return self.dishes
