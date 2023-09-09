from dish import Dish


class Menu:

    def __init__(self):
        self.dishes = {}
        self.__add_dishes()

    def __add_dishes(self):
        while True:
            dish_name = input("Please enter dish name: ")
            dish_description = input("Please enter dish description: ")
            dish_price = input("Please enter dish price: ")
            dish_image = input("Please enter dish image: ")
            dish = Dish(dish_name, dish_description, dish_price, dish_image, None)
            self.dishes.update({
                dish.get_dish_id(): dish
            })
            more_dishes = input("Do you want to add more dishes(Y/N)? ")
            if more_dishes != "Y":
                break

    def get_dishes(self):
        return self.dishes
