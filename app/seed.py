from app import app
from models import db, Restaurant, Pizza, RestaurantPizza
from faker import Faker
# from random import choice, random
import random
faker=Faker()

if __name__ == "__main__":
    with app.app_context():
        Restaurant.query.delete()
        Pizza.query.delete()
        RestaurantPizza.query.delete()

        restaurants=[]

        for _ in range(10):
            r = Restaurant(name=faker.company(), address=faker.address())
            restaurants.append(r)

        db.session.add_all(restaurants)

        pizzas=[]
        ingredients = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bell Peppers", "Olives", "Tomatoes", "Bacon", "Spinach", "Pineapple"]
        for _ in range(10):
            pizza=Pizza(name=faker.word(), ingredients=random.choice(ingredients))
            pizzas.append(pizza)

        db.session.add_all(pizzas)

        restaurant_pizzas=[]
        for _ in range(15):
            restaurant_pizza=RestaurantPizza(restaurant=random.choice(restaurants), pizza=random.choice(pizzas), price=random.randint(1, 30))
            restaurant_pizzas.append(restaurant_pizza)

        db.session.add_all(restaurant_pizzas)

        db.session.commit()