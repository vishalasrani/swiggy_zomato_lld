class Dish:

    counter = 1

    def __init__(self, name, description, price, dish_images, dish_addons):
        self.dish_id = Dish.counter
        Dish.counter += 1
        self.name = name
        self.description = description
        self.price = price
        self.dish_images = dish_images
        # self.dish_addons = dish_addons

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_dish_id(self):
        return self.dish_id
