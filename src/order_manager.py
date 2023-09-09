from food_manager import FoodManager


class OrderManager:

    instance = None

    def __init__(self):
        OrderManager.instance = self
        self.orders_map = {}

    @staticmethod
    def get_instance():
        if OrderManager.instance is None:
            OrderManager.instance = OrderManager()
        return OrderManager.instance

    def add_order(self, order):
        self.orders_map.update({
            order.get_order_id(): order
        })
        self.prepare_food(order)

    def prepare_food(self, order):
        food_manager_instance = FoodManager()
        food_manager_instance.prepare_food(order.get_order_id(), order.get_restaurant_id(), order.get_dishes())
