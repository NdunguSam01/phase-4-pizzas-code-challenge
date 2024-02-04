from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    address=db.Column(db.String, nullable=False)

    #Creating the relationships
    pizzas=db.relationship("Pizza", secondary="restaurantpizzas", backref="restaurants", viewonly=True)
    restaurant_pizzas=db.relationship("RestaurantPizza", backref="restaurant")

    def __repr__(self):
        return f"Restaurant Name: {self.name}\nAddress: {self.address}\n"

class Pizza(db.Model):

    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    ingredients=db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #Creating a relationship to the secondary table
    restaurant_pizzas=db.relationship("RestaurantPizza", backref="pizza")

    def __repr__(self):
        return f"Pizza Name: {self.name}\nIngredients: {self.ingredients}\n"

class RestaurantPizza(db.Model):

    __tablename__ = "restaurantpizzas"

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id=db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    pizza_id=db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    price=db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("price")
    def validate_price(self, key, price):
        
        if price < 1 or price > 30:
            return ValueError("Price must be a value between $1 and $30.")
        
        else:
            return price
        
    def __repr__(self):
        return f"Restaurant Name: {self.restaurant.name}\nPizza Name: {self.pizza.name}\nPrice: {self.price}"
        