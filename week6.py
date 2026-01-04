# 53. oop basics
class Car: #class
    country = "USA" #class var
    def __init__(self,car1,car2,car3): #class constractor
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3

    def info(self): #instance method
        return f"{self.car1},{self.car2},{self.car3}"

car = Car("tesla","bmw","toyota") #object
print(car.car1)
print(car.car2)
print(car.car3)
print(car.info())
print(Car.country)

# 54.class-object
class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        return f"The Human is {self.name}, he's {self.age} and {self.gender}"

person = Human("Bob",35,"Male")
print(person.name)
print(person.info())

# 55.inheritance and constractor
class Human:
    def __init__(self,planet,spacies):
        self.planet = planet
        self.spaces = spacies

class Male(Human):
    def __init__(self,planet,spacies,gender,body,lifetime):
        super().__init__(planet,spacies)
        self.gender = gender
        self.body = body
        self.lifetime = lifetime
    def basis(self):
        return f"Lives in the {self.planet},spaices = {self.spaces}"
    def info(self):
        return f"gender = {self.gender},body = {self.body},lifetime = {self.lifetime}"

class Female(Human):
    def basis(self):
        return f"Lives in the {self.planet},spaices = {self.spaces}"

male = Male("Earth","Homo sapience","Male","Strong",80)
print(male.basis())
print(male.info())
female = Female("Earth","Homo sapience")
print(female.basis())

# 56. class methods
class Shape:
    def __init__(self,color,is_fill):
        self.color = color
        self.is_fill = is_fill

class Circle(Shape):
    def __init__(self,color,is_fill,radius):
        super().__init__(color,is_fill)
        self.radius = radius

    def area(self): #instance methods
        return f"area is {3.1416 * self.radius**2:.2f} cm²"

obj = Circle("red",True,16)
print(obj.area())

# 57. super()
class Shape:
    def __init__(self,color,is_fill):
        self.color = color
        self.is_fill = is_fill

class Circle(Shape):
    def __init__(self,color,is_fill,radius):
        super().__init__(color,is_fill)
        self.radius = radius
    def area(self):
        return f"circle color {self.color} and is_fill is {self.is_fill} = {3.1416 * self.radius**2:.2f} cm2"
class Triangle(Shape):
    def __init__(self,color,is_fill,height,side):
        super().__init__(color,is_fill)
        self.height = height
        self.side = side
    def area(self):
        return f"Triangle color {self.color} and is_fill is {self.is_fill} = {0.5* self.height * self.side:.2f} cm2"
circle = Circle("red",True,16)
triang = Triangle("white",False,16,8)
print(circle.area())
print(triang.area())

# 58.polymorphism - inheritance and duck typing
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,color,is_fill):
        self.color = color
        self.is_fill = is_fill
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,color,is_fill,side):
        super().__init__(color,is_fill)
        self.side = side
    def area(self):
        return f"Square is {self.color} and is_fill {self.is_fill}. the area is {pow(self.side,2):.2f} cm2"
class Circle(Shape):
    def __init__(self,color,is_fill,radius):
        super().__init__(color,is_fill)
        self.radius = radius
    def area(self):
        return f"{self.color} and fill is {self.is_fill}. area is {3.1416 * self.radius**2} cm2"
sqr = Square("yellow",True,10)
cir = Circle("brown",False,8)
data = [sqr,cir]
for val in data:
    print(val.area())
# duck typing
class Animal:
    alive = True
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"wof! wof!"
class Duck(Animal):
    def speak(self):
        return f"pag! pag!"
class Car:
    alive = True
    def speak(self):
        return "hmm! hmm"
obj = [Dog(),Duck(),Car()]
for spk in obj:
    print(spk.speak())
    print(spk.alive)

# 59.magic methods
# known as dunder methods
"""__init__,__str__,__lt__,__gt__,__eq__,__add__...."""
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __lt__(self,other):
        return self.pages<other.pages
    def __gt__(self,other):
        return self.pages>other.pages
    def __eq__(self,other):
        return self.title==other.title and self.author==other.author
    def __add__(self,other):
        return self.pages+other.pages
    def __contains__(self,item):
        return item in self.title or item in self.author
    def __getitem__(self,item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "pages":
            return self.pages
        else:
            return f"hell!"

book1 = Book("Harry Potter","J.K. Rowling",3600)
book2 = Book("The Pychology of Money","Morgun Housell",300)
book3 = Book("Dopamine Detox","Thibaus Murish",120)
# all operations here you can do/

# 60. @property - read, write, delete = getter,setter,deleter
class Shape:
    def __init__(self,height,weight):
        self._height = height
        self._weight = weight

    @property
    def height(self):
        return f"{self._height:.2f} cm"
    @property
    def weight(self):
        return f"{self._weight:.2f} cm"
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height = new_height
    @weight.setter
    def weight(self,new_weight):
        if new_weight>0:
            self._weight = new_weight
    @height.deleter
    def height(self):
        del self._height
        print("height deleted")
    @weight.deleter
    def weight(self):
        del self._weight
        print("weight deleted")

obj = Shape(50,60)
print(obj.height)
print(obj.weight)
obj.height = 40
obj.weight = 30
print(obj.height)
print(obj.weight)
del obj.height
del obj.weight

# 61. @classmethod
class Students:
    count = 0
    gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.gpa += gpa

    def info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def result(cls):
        return f"{Students.gpa/Students.count}"

stu1 = Students("bob",3.2)
print(stu1.info())
print(Students.result())
stu2 = Students("sammy",4.0)
print(Students.result())

# 62. @staticmethod
class Students:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def info(self):
        return f"student name is {self.name} and roll {self.roll}"

    @staticmethod
    def position(pos):
        data = ["cook","manager","ceo","worker"]
        return pos in data
stu1 = Students("bob",19)
print(stu1.info())
print(Students.position("cook"))

# 63. decorator
def sprinkles(func):
    def wrappers(*args,**kwargs):
        print("** your sprinkles **")
        func(*args,**kwargs)
        print("** now enjoy your icecream")
    return wrappers

@sprinkles
def get_icecream(flavor):
    print(f"This is your icecream with {flavor} flavor")

get_icecream("Chocolate")





