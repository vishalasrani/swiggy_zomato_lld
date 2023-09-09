class RestaurantManager:
    instance = None

    def __init__(self):
        RestaurantManager.instance = self
        self.__restaurant_map = {}

    @staticmethod
    def get_instance():
        if RestaurantManager.instance is None:
            RestaurantManager.instance = RestaurantManager()
        return RestaurantManager.instance

    def add_restaurant(self, restaurant_id, restaurant_obj):
        self.__restaurant_map.update({
            restaurant_id: restaurant_obj
        })

    def remove_restaurant(self, restaurant_id):
        del self.__restaurant_map[restaurant_id]

    def get_restaurant(self, restaurant_id):
        return self.__restaurant_map.get(restaurant_id)

    def get_all_restaurants(self):
        return self.__restaurant_map
