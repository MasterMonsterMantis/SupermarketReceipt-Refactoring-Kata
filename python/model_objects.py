from enum import Enum

#product calss
class Product:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit
    

#product No. class
class ProductQuantity:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


#package and pair item in a package class    
public class productpackage:
    def __init__(self,product)
        self.product = product
        product.product = product


class SpecialOfferType(Enum):
    THREE_FOR_TWO = 1
    TEN_PERCENT_DISCOUNT = 2
    TWO_FOR_AMOUNT = 3
    FIVE_FOR_AMOUNT = 4

#new specialoffer
class SpecialOfferNew:
    def __init__(self,product,item)
        self.item = item
        self.pruduct = pruduct
    
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
