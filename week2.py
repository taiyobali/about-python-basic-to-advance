# 13.Operators and some examples
"""
There are 7 types of important operators in python.
1. Arithmetic, 2.Assignment, 3.Logical,
4. Identify, 5.Bitwise, 6.Membership
7.Comparison operators
"""
# arithmetic operators: + - * / // ** %
x = 20
y = 50
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//5)
print(y%x)
import math
print(math.floor(29/5))
print(math.ceil(29/5))
# assignment operators: = += -= *= /= //= **= %= &= |=
var = "Hello"
print(var)
num = 5
total = 0
for i in range(1,num+1):
    total += i
print(total)
# logical operators: and or not
x = 50
y = 60
print(x<y and x<70)
print(x<y or x<40)
print(not(x<y))
# comparison operators: < > <= >= == !=
print(5 == 2)
print(5 != 2)
# bitwise operators: & | ~ ^ << >>
x = 50
y = 60
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x<<2)
print(x>>2)
# identify operators: is , is not (memory location same or not)
x = 5
y = x
print(x is y)
print(x is not y)
# membership operators: in, not in
data = [1,2,3,4,5,6]
print(1 in data)
print(9 in data)
print(9 not in data)

# 14. conditional statements: if elif else
"""
if expression:
    statement
elif expression:
    statement
...............
else:
    statement
"""
x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x<y:
    print("x is less than y")
elif y<x:
    print("y is less than x")
else:
    print("x and y are equal")

# 15. for and while loops
for i in range(5):
    print(i,end=" ")
print()
total = 0
num = 50
for i in range(1,num+1):
    total += i
print(total)
data = [1,5,8,96,63,45,85,78]
for i in data:
    print(i)

x = 0
while x<11:
    print(x)
    x += 1
x = 0
num = 50
total = 0
while x<num+1:
    total += x
    x += 1
print(total)

num = 50
total = sum(range(50+1))
print(total)

# 16.break,continue,pass control statements
for i in range(10):
    if i == 5:
        break
    print(i)
x = 0
while x<10:
    if x == 5:
        break
    print(x)
    x += 1
for i in range(1,21):
    if i%2==1:
        continue
    print(i,end=" ")
print()
x = 0
num = 21
while x<num:
    x += 1
    if x%2==1:
        continue
    print(x,end=" ")
print()
for i in range(1,100):
    print(f"{10}*{i} = {10*i}")
    if i==10:
        break
x = 0
num = 50
while x<num:
    x += 1
    print(f"{10}*{x} = {10*x}")
    if x==10:
        break

for i in range(1):
    pass
while x<50:
    pass

# 17. list data str and list comprehension
# list: mutable, ordered, allow duplicates and all data types, list()
data = [1,5,5,6,"Hello",True,{1,5,8},(8,9,10,20),[48,96,75],3.1416]
print(data)
print(isinstance(data,list))
print(data[0])
print(data[-1])
print(data[-2][1])
data[0] = 125
print(data[0])
data[2] = "Bob"
print(data)
list1 = [1,2,3,4]
list2 = [4, 5, 6, 7]
list3 = list1 + list2
print(list3)
data = list((1,2,3,4,54))
print(data)
# list methods 12
from copy import deepcopy
copy_list = deepcopy(data)
print(copy_list)
print(data is copy_list)
data = [1,2,3,4,5]
data.append(65)
print(data)
data.append("Python")
print(data)
data.insert(0,255)
print(data)
data.insert(len(data),"ML")
print(data)
data.extend(list3)
print(data)
data.pop(-1)
print(data)
data.remove("Python")
print(data)
del data[0]
print(data)
list3.clear()
print(list3)
print(data.index("ML"))
print(data.count(3))
print(len(data))
print(dir(list))
list4 = [5,9,2,7,8,63,95,15,75,85,365,14,285,45]
list4.sort()
print(list4)
list4 = [5,9,2,7,8,63,95,15,75,85,365,14,285,45]
list4.sort(reverse=True)
print(list4)
list4 = [5,9,2,7,8,63,95,15,75,85,365,14,285,45]
list4.reverse()
print(list4)
# list comprehension: [expression for i in iter if condition]
data = [i**2 for i in range(1,10) if i%2!=1]
print(data)
# inner loop and outer loop
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)
string = "Hello World! I love python"
words = string.split()
length = [len(word) for word in words]
print(length)
odds = [i for i in range(50) if i%2==1]
print(odds)

# 18.tuple data str: immutable,ordered,allow duplicates, allow all types, tuple()
tup = (1,8,96,3.1416,6+6j,"Bob",True,(1,253,3),1,2,3,12,1)
print(tup)
print(type(tup))
print(tup[0])
print(tup[-1])
data = tuple((1,5))
print(data)
tupl = (24,)
print(isinstance(tupl,tuple))
print(tup.count(1))
print(tup.index("Bob"))
from copy import deepcopy
second = deepcopy(tup)
print(second)

# 19. frozenset: immutable, unordered, no duplicates, values immutable
set_data = {1,2,5,3,6,"This is set",(15,85)}
fro_set = frozenset(set_data)
print(fro_set)
print(type(fro_set))
li = [1,5,9,6]
data = frozenset(li)
print(data)

# 20. array data: almost same with list just one data type at a time
import array as ar
data = ar.array("i",[1,5,9,63,85,85,74,1,2,3,456,85,74,25,36,15,25,1,25,36])
print(data)
print(type(data))
data.append(5)
print(data)
data.append(255)
print(data)
data.insert(0,25)
print(data)
data2 = ar.array("i",[456,123,789,741,852,9633])
data.extend(data2)
print(data)
print(data.count(1))
print(data.index(63))
data.pop(-1)
print(data)
data.remove(789)
print(data)
del data[0]
print(data)
data.reverse()
print(data)
li = [1,2,3,6]
print(ar.array("i",li))
