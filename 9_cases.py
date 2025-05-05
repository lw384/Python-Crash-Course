# 9.1 9.3
class Restaurant:
    """describe a restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """print info"""
        print(f"{self.restaurant_name}{self.cuisine_type}")
    def open_restaurant(self):
        """print status"""
        print(f"{self.restaurant_name} is open")
    def set_number_served(self,num):
        self.number_served = num

    def increment_number_served(self,add_num):
        self.number_served +=add_num


restaurant = Restaurant('麻辣烫','djdj')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.number_served = 1
print(restaurant.number_served)

restaurant.set_number_served(100)
restaurant.increment_number_served(20)
print(restaurant.number_served)

# 9.6

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple','orange','milk','chocolate']
    def show_flavors(self):
        print(f"{self.flavors}")

ice_cream = IceCreamStand('ice cream','cold')
ice_cream.show_flavors()