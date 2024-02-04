#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
api=Api(app)
db.init_app(app)

@app.route('/')
def home():
    return '<h1>Home</h1>'

class Restaurants(Resource):
    def get(self):
        restaurants=Restaurant.query.all()
        response=[]

        for restaurant in restaurants:
            response.append({
                'id': restaurant.id,
                'name': restaurant.name,
                "address": restaurant.address
            })

        return make_response(jsonify(response), 200)
    
api.add_resource(Restaurants, "/restaurants")

class RestaurantByID(Resource):
    def get(self, id):
        restaurant=Restaurant.query.filter(Restaurant.id == id).first()

        if not restaurant:
            response={
                "error":"Restaurant not found"
            }
            return make_response(jsonify(response),404)
        
        restaurant_dict={
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': []
        }

        for pizza in restaurant.pizzas:
            pizza_dict={
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }

            restaurant_dict["pizzas"].append(pizza_dict)
        
        return make_response(jsonify(restaurant_dict), 200)

api.add_resource(RestaurantByID, "/restaurants/<int:id>")

class Pizzas(Resource):
    def get(self):
        pizzas=Pizza.query.all()
        response=[]

        for pizza in pizzas:
            response.append(
            {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            })
        return make_response(jsonify(response), 200)

api.add_resource(Pizzas, "/pizzas")

class RestaurantPizzas(Resource):
    def post(self):
        pizza_id=request.json['pizza_id']
        restaurant_id=request.json['restaurant_id']
        price=request.json['price']

        price_validation=RestaurantPizza().validate_price(key=price, price=price)

        if price_validation != price:
            response={
                "error": ["Validation errors"]
            }
            return make_response(jsonify(response), 400)

        else:
            new_restaurant_pizza=RestaurantPizza(price=price, pizza_id=pizza_id,restaurant_id=restaurant_id)
            db.session.add(new_restaurant_pizza)
            db.session.commit()
            response={
                "id": new_restaurant_pizza.pizza.id,
                "name": new_restaurant_pizza.pizza.name,
                "ingredients": new_restaurant_pizza.pizza.ingredients
            }

            return make_response(jsonify(response), 201)

api.add_resource(RestaurantPizzas, "/restaurant_pizzas")
if __name__ == '__main__':
    app.run(port=5555, debug=True)
