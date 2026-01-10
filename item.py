
import csv
class Item:
    discount = 0.2 #class attributes
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        # validation check
        assert price>=0, f"price {price} must be greater than or eq zero"
        assert quantity>=0, f"quantity {quantity} must be greater than or eq zero"
        # instance attributes
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # for append instance
        Item.all.append(self)
    #magic methods -- automatically called by python, use for control objects behavior
    def __str__(self):
        return f"name: {self.__name},price: {self.__price}, quantity: {self.__quantity}"
    def __eq__(self,other):
        return self.__name==other.__name
    def __gt__(self,other):
        return self.__quantity>other.__quantity
    def __lt__(self, other):
        return self.__quantity<other.__quantity
    def __add__(self, other):
        return self.__price + other.__price
    def __getitem__(self, item):
        if item == "name":
            return self.__name
        elif item == "price":
            return self.__price
        elif item == "quantity":
            return self.__quantity
        else:
            return f"{item} is not a valid item"
    def __contains__(self, item):
        if item in self.__name:
            return True
        else:
            return False

    #decorator = property(read_only), setter(update value), deleter(delete value)
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def quantity(self):
        return self.__quantity
    @name.setter
    def name(self,new_name):
        if len(new_name)>10:
            raise Exception(f"new name length {len(new_name)} is too long")
        else:
            self.__name = new_name
    @price.setter
    def price(self,value):
        assert value>0, f"price {value} must be greater than zero"
        self.__price = value
    @quantity.setter
    def quantity(self,value):
        assert value>=0, f"quantity {value} must be greater than or eq zero"
        self.__quantity = value
    # @name.deleter
    # def name(self):
    #     del self.__name
    # instance methods
    def apply_discount(self):
        self.__price = self.__price - (self.__price * self.discount)

    def calculate_total_price(self):
        return self.__price*self.__quantity

    # represent something, eg. in all list (ethics how it will repr)
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}',{self.__price},{self.__quantity})"

    @classmethod
    def instantiate_csv(cls):
        with open(r"items.csv","r") as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(
                name= item.get("name"),
                price= float(item.get("price")),
                quantity= int(item.get("quantity"))
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,color:str,is_filled:bool):
        self.color = color
        self.is_filled = is_filled

    @abstractmethod
    def area(self):
        pass
