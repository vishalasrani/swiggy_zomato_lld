from cart import Cart
from cart_manager import CartManager


class User:

    id = 1

    def __init__(self, name, email, mobile):
        self.user_id = User.id
        User.id += 1
        self.name = name
        self.email = email
        self.mobile = mobile
        self.cart = None
        self.__initialize_cart()

    def __initialize_cart(self):
        self.cart = Cart()

    def get_user_id(self):
        return self.user_id

    def get_cart(self):
        cart_manager_instance = CartManager.get_instance()
        return cart_manager_instance.get_user_cart(self.user_id)
