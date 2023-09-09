from restaurant_manager import RestaurantManager

class FoodManager:

    instance = None

    def __init__(self):
        FoodManager.instance = None

    @staticmethod
    def get_instance():
        if FoodManager.instance is None:
            FoodManager.instance = FoodManager()
        return FoodManager.instance

    def prepare_food(self, order_id, restaurant_id, dishes):
        restaurant_manager_instance = RestaurantManager.get_instance()

