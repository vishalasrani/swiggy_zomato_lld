from cart import Cart


class CartManager:

    instance = None

    def __init__(self):
        CartManager.instance = self
        self.user_carts = {}

    @staticmethod
    def get_instance():
        if CartManager.instance is None:
            CartManager.instance = CartManager()
        return CartManager.instance

    def get_user_cart(self, user_id):
        if user_id not in self.user_carts:
            self.user_carts[user_id] = Cart(user_id)
        return self.user_carts[user_id]
