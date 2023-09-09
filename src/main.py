from restaurant_owner import RestaurantOwner
from restaurant_manager import RestaurantManager
from restaurant import Restaurant
from user import User
from cart_manager import CartManager
from order import Order
from order_manager import OrderManager

def main():
    vijay = User("Vijay", "fasdfs", "fsdf")

    restaurant_manager = RestaurantManager.get_instance()
    restaurant_owner1 = RestaurantOwner("Vishal")
    restaurant = Restaurant("Hotel Taj", "Mumbai", restaurant_owner1, True)

    restaurant_owner2 = RestaurantOwner("Pari")
    restaurant = Restaurant("Faasos", "Mumbai", restaurant_owner2, True)

    user_cart = vijay.get_cart()

    print("Available Restaurants")
    all_restaurants = restaurant_manager.get_all_restaurants()
    for rest_id, rest in all_restaurants.items():
        print("Restaurant ID: %s, Restaurant Name: %s" % (rest_id, rest.get_restaurant_name()))
    selected_restaurant = int(input("Enter restaurant id to view menu: "))
    user_cart.update_restaurant(selected_restaurant)
    print("Menu of Restaurant: %s" % all_restaurants[selected_restaurant].get_restaurant_name())
    dishes = all_restaurants[selected_restaurant].get_menu()
    for dish_id, dish in dishes.items():
        print(dish_id, dish.get_name(), dish.get_description(), dish.get_price())
    while True:
        selected_dish = input("Enter dish id to select dish: ")
        if selected_dish not in dishes.keys():
            continue
        qty = input("Enter the quantity of selected dish: ")
        user_cart.add_items_to_cart(selected_dish, qty)
        add_more_items = int(input("Select 1 if you want to add more items to the cart: "))
        if add_more_items != 1:
            break
    order = Order(vijay.get_user_id(), user_cart.get_restaurant_id(), user_cart.get_items_in_cart())
    order_manager_instance = OrderManager()
    order_manager_instance.add_order(order)


if __name__ == "__main__":
    main()
