# 1.about python
"""
python is an open source, interpreted, dynamically typed, high_level language,
object-oriented programming, functional, case-sensitive,
portable, platform independent, embeddable and extensible language.
"""
# comment in python: we can read, but it doesn't execute in interpreter.
# there are two types of comment: this is a single line comment(ctrl+/)
"""
this is
a
multi-line comment or doc.str
"""
# output func: print() func used to print something on screen
print("Hello World!")
print("Hello","World!")
print(123)
print("12"+"3")
print(12+3)
# others
"""
we must follow indentation rules.
python file extension is .py
"""

# 2.variables: var is a name where we can store data
# var_name =(assignment operator) value
"""
variable name is case-sensitive(A,a not same)
we can't use a special word of python as a variable name: for , while, print, True, in.
variable name must be character(alpha-num) and _ only.
start with char, we can't use num first,
eg; var, var2, var_, var_2, var2_, _var
"""
name = "Guido van"
age = 53
country = "America"
print("{0} is the python creator, he's {1} years old. He lives in {2}.".format(name,age,country))
name,num,pi = "Taiyob",123,3.1416
print(name,num,pi)
# to see the size of a variable
import sys
print(sys.getsizeof(name))
print(sys.getsizeof(pi))
# global var and local var
# local_var = inside a func, works inside the func
# global var = outside and accessible from anywhere.
"""
to run program in pycharm = shift+F10
to run program in vs code = shift+enter
"""

# 3. data types basic
# data_type is the type of var, what type of data we stored
# to know data type of any var, we can use type(), or isinstance()
name = "Guido van"
print(name)
print(type(name))
print(isinstance(name,str)) #return bool
num = 123
print(type(num))
print(isinstance(num,int))
"""
there are many types of data in pyhon:
1. number types: int, float, complex
2. set types: set, frozenset
3. sequence: list, tuple, range, array, str
4. mapping: dict
5. binary: bytes, bytearray, memoryview
6. None : None types
"""
"""
type casting: convert from one type to another
some type casting functions:
int(), float(), complex(), str(), list(), tuple(), set(),
dict(), range(), bytes(), bytearray()
"""
num = 123
pi = 3.1416
print(num)
print(float(num))
print(pi)
print(int(pi))

# 4.number types: int, float, complex
num = 123 #int
pi = 3.1416 #float
zet = 3+4j #complex (x+yj)
print(type(num))
print(type(pi))
print(type(zet))
print(isinstance(num,int))
print(isinstance(pi,int))
# we can type cast from int|float = float|int|complex, but complex != ...
num1 = int(pi)
print(num1)
print(type(num1))
num2 = float(num)
print(num2)
print(isinstance(num2,float))
num3 = complex(num)
print(num3)
print(type(num3))
num4 = complex(pi)
print(num4)
print(isinstance(num4,complex))
summ = num+num
print(summ)
summ = num+pi #replace by new value
print(summ)
summ = num+zet
print(summ)
mult = num*num
print(mult)
mult = num*pi
print(mult)
mult = num*zet
print(mult)
mult = pi*pi
print(mult)
mult = zet*zet
print(mult)
divi = num/num
print(divi)

# 5.str type
"""
anything in "" or '' is a str.
immutable, ordered.
there are many methods in str type.
"""
name = "Guido van"
print(type(name))
print(isinstance(name,str))
import sys
print(sys.getsizeof(name))
data = "I love ml, I want to Become an engineer. I like Python. Don't you? you should love python too!"
# methods: var.method()
print(data.count("I"))
print(data.count("a",5,20))
print(data.find("I")) #return index
print(data.find("I",5,20))
print(data.find("ai")) #if not exist, return -1
print(data.index("I")) #same as find
# print(data.index("ai")) #if not exist, error
print(data.lower())
print(data.casefold())
print(data.upper())
print(data.swapcase())
print(data.islower())
print(data.isupper())
print(data.isalpha())
num = "1234556"
print(num.isdigit())
print(num.isnumeric())
print(num.isalpha())
name = "Guido"
print(name.isalpha())
print(data.encode())
print(data.split())
print(data.split(" "))
print(data.split(","))
print(data.center(100))
print(name.center(100))
print(data.replace("I","We"))
print(data.strip("I"))
print(data.strip("!"))
print("_".join(data))
print("_".join(data.split()))
print(f"{name} was the genius who created python.{data}")
print(data.capitalize())
print(data.title())
# we can dir() and help() func for comprehension or any help
# print(help(str))
# print(dir(str))
# index in python: 0,1,2,3,4,5,6....
print(data[0])
print(data[-1])
print(data[0:10]) # 0 to 10-1
print(data[0:])
print(data[10:])
print(data[:])
print(data[-10:])
print("I love my \"Country\"") # \ is a special char
print("\\")

# 6.bool type and basic sequence types
# bool = True, False
num1 = 20
num2 = 50
print(num1>num2)
print(num1<num2)
print(num1==20)
print(num1!=num2)
# sequence: list,tuple,range,array,str
# range()
for i in range(5):
    print(i,end=" ")
print()
for i in range(1,5):
    print(i,end=" ")
print()
for i in range(1,20,2):
    print(i,end=" ")
print()
for i in range(20,1,-2):
    print(i,end=" ")
print()

# 7.Binary types and None type
# None
val = None
print(type(val))
# binary: bytes, bytearray, memoryview
# bytes: immutable, ordered, range(0-255), allow duplicate value,bytes()
data = [0,5,2,3,5,2,6,120,150,241,254,30,65,123]
byte = bytes(data)
print(byte)
print(type(byte))
print(isinstance(byte,bytes))
print(byte[0])
print(byte[-1])
print(byte[5])
# bytearray: mutable,range(0-255),allow duplicates, bytearray()
data = [0,5,2,3,5,2,6,120,150,241,254,30,65,123]
byte_arr = bytearray(data)
print(byte_arr)
print(type(byte_arr))
print(byte_arr[0])
print(byte_arr[-1])
byte_arr[0] = 65
print(byte_arr[0])
name = "Guido van"
byte_arr = bytearray(name,"utf-8")
print(byte_arr)
print(type(byte_arr))
print(byte_arr[0])
byte_arr[0] = ord("g")
print(byte_arr)
# memoryview: mutable,ordered,allow duplicates, memoryview()
mv = memoryview(byte_arr)
print(mv)
print(isinstance(mv,memoryview))
print(mv[0])
print(mv[-1])
mv[0] = ord("G")
print(mv[0])

# 8.user input
# input() takes everything as a str, but we can cast.
name = input("Enter your name: ")
print(name)
print(type(name))
num = int(input("Enter a num: "))
print(num)
print(isinstance(num,int))
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
summ = num1+num2
print(f"Your summation is {summ}")
pi = float(input("Enter the value of pi: "))
print(pi)
zet = complex(input("Enter a complex num: "))
print(zet)
a,b,c = input("Enter comma-separated(a,b,c): ").split(",")
print(a,b,c)
a,b,c = input("Enter space-separated(a b c): ").split()
print(a,b,c)
x,y,z = map(int,input("Enter 3 space separated nums: ").split())
print(type(x))
print(x,y,z)
nums = map(int,input("Nums: ").split())
print(list(nums))
user = input("Enter user name: ")
pin = int(input("Enter pin: "))
print("Your user_name is {0} and password is {1}".format(user,pin))

# 9.DataFrame
# pandas library's class, two_dimensional table (row*column)
# there are some data types in DataFrame: float64,int64, object, bool
import pandas as pd
df = pd.read_csv("python_stu.csv")
print(df)
import pandas as pd
data = [(1,"Alex",18,"computer"),
        (2,"Bob",19,"mathematics"),
        (3,"Sammy",19,"biology")]
df = pd.DataFrame(data,columns=["sl","name","age","major"])
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.size)
print(df.shape)
print(df.values)
print(df.columns)
print(df.dtypes)
print(df.index)
print(dir(pd.DataFrame))
print(df.name)
print(df.age)
print(df[["name","age"]])

# 10.set data str
# immutable(can add and remove), no duplicates, unordered, set(), 17 methods+
data = {1,2,5,5,2,6,8,10}
print(data)
data = {1,2,5,5,2,6,8,10,"Hello",True,False,(1,5,3),3.1416}
print(data)
from copy import deepcopy
set_data = deepcopy(data)
print(set_data)
data.add(85)
print(data)
data.update([45,86,"Bob"])
print(data)
values = {85,96,45,False,"Bob","2026","Hello"}
print(data.difference(values))
data.difference_update(values)
print(data)
data = {1,2,5,5,2,6,8,10,"Hello",True,False,(1,5,3),3.1416}
print(data.intersection(values))
data.intersection_update(values)
print(data)
print(data.issubset(values))
print(data.issuperset(values))
print(data.isdisjoint(values))
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.isdisjoint(set2))
data = {1,2,5,5,2,6,8,10,"Hello",True,False,(1,5,3),3.1416}
print(data.symmetric_difference(values))
data.symmetric_difference_update(values)
print(data)
print(data.union(values))
print(data)
data.pop()
print(data)
data.remove("Bob")
print(data)
data.discard(10)
print(data)
data.clear()
print(data)
print(dir(set))

# 11. dict data str
# dict: mutable, ordered(key), allow duplicates but not keys, dict()
dic = {
    "name": "Spongebob",
    "age": 30,
    "country": "usa",
    "major": "cse",
    "current": "usa"
}
print(dic)
print(type(dic))
print(isinstance(dic,dict))
dic["age"] = 35
print(dic)
from copy import deepcopy
data = deepcopy(dic)
print(data)
dic["school"] = "Bro code"
print(dic)
dic.update({"class": 10,"dad": "Bob"})
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
dic.pop("dad")
print(dic)
dic.pop("class")
print(dic)
del dic["school"]
print(dic)
del dic["current"]
print(dic)
print(dic.get("major"))
print(dic.get("country"))
print(dic.get("agge")) #None
print(dir(dict))

# 12. swapping values
num = 123
pi = 3.1416
print(num)
print(pi)
num,pi = pi,num
print(num)
print(pi)