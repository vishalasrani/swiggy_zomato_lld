from restaurant_owner import RestaurantOwner
from menu import Menu
from restaurant_manager import RestaurantManager


class Restaurant:

    counter = 1

    def __init__(self, name: str, address: str, owner: RestaurantOwner, is_avail: bool):
        self.name = name
        self.address = address
        self.owner = owner
        self.menu = None
        self.is_avail = is_avail
        self.restaurant_id = Restaurant.counter
        Restaurant.counter += 1
        self.__add_menu()
        self.__update_restaurant_manager()

    def __add_menu(self):
        print("\nAdding menu for restaurant %s" % self.name)
        self.menu = Menu()

    def __update_restaurant_manager(self):
        restaurant_manager_instance = RestaurantManager.get_instance()
        if self.is_avail:
            restaurant_manager_instance.add_restaurant(self.restaurant_id, self)
        else:
            restaurant_manager_instance.remove_restaurant(self.restaurant_id)

    def set_is_availability(self, is_avail):
        self.is_avail = is_avail
        self.__update_restaurant_manager()

    def get_restaurant_name(self):
        return self.name

    def get_menu(self):
        return self.menu.get_dishes()
