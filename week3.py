# 21. zip() and unzip
names = ["alex","anthony","sammy","taylor","bob"]
ages = [19,20,21,18,20]
subs = ["math","physics","chemistry","biology","computer"]
about = list(zip(names,ages,subs))
print(about)
for itr in about:
    print(itr)
name,age,sub = zip(*about)
print(list(name))
print(list(age))
print(list(sub))

# 22. enumerate() func
names = ["alex","anthony","sammy","taylor","bob"]
ages = [19,20,21,18,20]
subs = ["math","physics","chemistry","biology","computer"]
about = list(zip(names,ages,subs))
print(about)
name,age,sub = about[0]
print(name)
print(age)
print(sub)
for name,age,sub in about:
    print(name,age,sub)
for index,itr in enumerate(about):
    name,age,sub = itr
    print(f"{index}|{name}|{age}|{sub}")

# 23. zip file and unzip file
import zipfile as zf
with zf.ZipFile(r"New2026.zip","w") as file:
    file.write("2025.pdf")
    file.write("mml-book.pdf")
import zipfile as zf
with zf.ZipFile(r"python.zip","w") as file:
    file.write("mml-book.pdf")
    file.write("imshadow-500 difficulty rating.pdf")
import zipfile as zf
with zf.ZipFile(r"New2026.zip","r") as file:
    file.extractall("This_is_unzip1")
import zipfile as zf
with zf.ZipFile(r"python.zip","r") as file:
    file.extractall("this_is_unzip2")

# 24.search and replace text
with open(r"text1.txt","r") as file:
    data = file.read()
    data = data.replace("python","python programming")
with open(r"text1.txt","w") as file:
    file.write(data)
import re
data = "this is a test file for search and replace text in python. so let's try it."
change = re.sub("python","python programming",data)
print(change)

# 25. build-in 25 functions
# print()
print("Hey guys, I'm Taiyob. I like AI and ml so, learning python to make my dream true.")
print("2026")
print(123)
# len()
data = [1,5,9,5]
print(len(data))
data = "string"
print(len(data))
# range()
data = list(range(6))
print(data)
# str(), int(), float(), complex(), dict(), list(), set()
# those are for type casting
num = "123"
print(type(int(num)))
# round()
pi = 3.1416
num = round(pi)
print(num) # 3 , make it int around the most possible of num
flo = round(pi,2)
print(flo) # two decimal
# sorted()  make iterable ascending
li = [95,85,96,32,45,14]
print(sorted(li))
# reversed()
li = [95,85,96,32,45,14]
rev = reversed(li)
print(list(rev))
# any(), all() = bool
data = [True,True,True,False,False]
data2 = [True,True,True]
print(any(data))
print(all(data))
print(any(data2))
print(all(data2))
nums = [184,""]
print(any(nums))
print(all(nums))
# chr(), ord()
num = 65
print(chr(num))
print(ord("A"))
# input()
user = input("enter your user name: ")
print(user)
# type(), isinstance()
print(type(user))
print(isinstance(user,str))
# enumerate()
data = ["a","b","c"]
for i,value in enumerate(data):
    print(i+1,value)
# max(),min()
data = [12,85,96,32,85,96,45,75,85,96,36,569,265,96,65,569]
print(max(data))
print(min(data))
# sum()
total = sum(data)
print(total)
new = sum(data,100)
print(new)
# abs()
print(abs(-15))
zet = 5+3j
print(abs(zet))
# slice()
new = data[slice(1,5)]
print(new)
# zip()
name = ["alex","tony","bob"]
age = [25,30,35]
new = list(zip(name,age))
print(new)
#pow()
x = 5
y = 2
z = 2
sqr = pow(x,y)
print(sqr)
mod = pow(x,y,z)
print(mod)

# 26. def func and factorial
"""
def func(parameters):
    statement
    return
func(arg)
"""
def add(a,b):
    return a+b
print(add(10,9))
def about(name,age):
    return f"Hey,{name}, you're {age}"
print(about("taylor",19))
def multi(a,b):
    return a*b
def multi2(z):
    return multi(5,2)*z
print(multi2(5))
def fac(x):
    if x==0:
        return 1
    else:
        return x*fac(x-1)
print(fac(5))
def fact(x):
    if x==0:
        return 1
    else:
        total = 1
        for i in range(1,x+1):
            total *= i
        return total
print(fact(5))

# 27. list manipulation
data = [12,14,2,5,3,9,8,7,6,5,21,2,6,9,24,15,68,41,12,30,10,50,12,32,14,41,15,17,18,19,17,12,18,15,14,12]
def dupli_rm(x:list)->list:
    new = []
    for i in x:
        if i not in new:
            new.append(i)
    return new
print(dupli_rm(data))
def sqr(x:list)->list:
    new = []
    for i in x:
        new.append(pow(i,2))
    return new
print(sqr(data))

# 28. match-case statement
"""
match x:
    case 1:
        statement
    case 2:
        statement
    case_:
        statement
"""
user = input("Enter a num(1-5): ").strip()
match user:
    case "1":
        print("Name")
    case "2":
        print("Age")
    case "3":
        print("Major")
    case "4":
        print("Interest")
    case "5":
        print("Address")
    case _:
        print("Invalid input")

# 29. parameters and argument
"""
def func(parameters): the variable
    .......
fucn(arguments) value
there are 4 types of arguments:
i. positional argument
ii. keyword argument
iii. default argument
iv. variable length argument
"""
# positional argument
def about(name:str,age:int):
    return f"{name} is {age}"
print(about("bob",35))
# keyword argument
def job(name:str,age:int,salary:float):
    return f"{name} is {age} and his salary is {salary}"
print(job(age=35,name="bob",salary=50000))
print(job("bob",age=30,salary=50000.0))
print(job("bob",25,salary=50000))
# default argument
def add(x,y,z=100):
    return x+y+z
print(add(5,10,20))
print(add(5,10))
print(add(10,50))
# variable length argument
# *y = args, **z = kargs
def multi_data(x,*y,**z):
    return f"{x}\n{y}\n{z}"
print(multi_data(56,50,50.10,30,80,name="bob",age=35))

# 30. func recursion
def fac(x):
    if x==0:
        return 1
    return x*fac(x-1)
print(fac(5))





