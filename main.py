from item import Item
from phone import Phone
from laptop import Laptop
from shape_child_classes import Circle,Triangle
item1 = Item("phone",500,3)
item2 = Item("laptop",700,5)
print(Item.all)
for instance in Item.all:
    print(instance)
item1.apply_discount()
print(item1.calculate_total_price())
item2.discount = 0.8
item2.apply_discount()
print(item2.calculate_total_price())
print(Item.__dict__) #all class level attributes
print(item1.__dict__) #all instance level attributes
phone1 = Phone("Iphone",1200,3,5)
print(Phone.all)

Item.instantiate_csv()
print(Item.all)
print(Item.is_integer(10.0))

print(Phone.about_this_class())

laptop1 = Laptop("Apple macbook",1500,2)
print(Laptop.all)

shape1 = Circle("red",True,16)
print(shape1.area())

shape2 = Triangle("white",False,2.78,9,30)
print(shape2.area())
item1.name = "something"
item1.price = 705
item1.quantity = 5
print(item1.name)
print(item1.price)
print(item1.quantity)
# del item1.name
# print(item1.name) it will be an error
print(item1)
item3 = Item("laptop",1500,7)
print(item1==item3)
print(item2==item3)
print(item3>item1)
print(item1<item3)
print(item1 + item2)
print(item1["name"])
print(item2["price"])
print("laptop" in item3)
print("lap" in item3)