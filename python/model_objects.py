from enum import Enum

#pair two product for initializing discount
class pairproductspackage:
    def __init__(self,pair ,price):
        self.pair = pair
        pair.pair = pair
        self.price = price
        
#total price of pair products
class pairprice:
    def __init__(product):
        if product == pairproductspackage.pair:
            pairprices = unit_price.price + pairproductspackage.price 
class Product:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit


class ProductQuantity:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class ProductUnit(Enum):
    EACH = 1
    KILO = 2


class SpecialOfferType(Enum):
    THREE_FOR_TWO = 1
    TEN_PERCENT_DISCOUNT = 2
    TWO_FOR_AMOUNT = 3
    FIVE_FOR_AMOUNT = 4
    #
    PAIR_PRO = 5

class Offer:
    def __init__(self, offer_type, product, argument):
        self.offer_type = offer_type
        self.product = product
        self.argument = argument


class Discount:
    def __init__(self, product, description, discount_amount):
        self.product = product
        self.description = description
        self.discount_amount = discount_amount
