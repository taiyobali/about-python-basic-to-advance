# # 31. format specifies
# # {value:flags}
# print(f"${50:.2f}")
# print(f"${50:10}")
# print(f"${50:010}")
# print(f"${50: }")
# print(f"${50:<010}")
# print(f"${50:>010}")
# print(f"${50:+}")
# print(f"${5000000:,}")
# print(f"${5000000000:+,.2f}")

# # 32. dir() and help()
# # to about something in python
# import random
# print(dir(random))
# print(help(random))

# # 33. digital watch
# import time
# seconds = int(input("Enter time in seconds: "))
# for i in range(seconds,0,-1):
#     sec = i%60
#     mint = (i//60)%60
#     hou = i//3600
#     print(f"{hou:02}:{mint:02}:{sec:02}")
#     time.sleep(1)
# print("Times up")

# 34. quiz game

# 35. number guessing game

# 36. rock-paper-scissors game

# 37. dice-roller game

# # 38. random module
# import random
# data = [12,85,63,45,89,96,45,25,36,14,25,362,152,142]
# print(random.random()) #float 0-1
# num = random.randint(1,100)
# print(num)
# print(random.choice(data)) #one element
# print(random.choices(data)) #list of value one or multi element
# print(random.choices(data,k=3))
# data = [12,85,63,45,89,96,45,25,36,14,25,362,152,142]
# random.shuffle(data)
# print(data)

# # 39. lambda anonymous func
# # lambda args: expression
# add = lambda x,y: x+y
# print(add(5,50))
# multi = lambda x,y: x*y
# print(multi(5,50))
# def add(x,y,operation):
#     return operation(x,y)
# print(add(50,50,lambda x,y: x+y))

# # 40.map(), filter() , reduce()
# data = [12,85,63,45,89,96,45,25,36,14,25,362,152,142]
# new = map(lambda x: pow(x,2),data)
# print(list(new))
# even = filter(lambda x: x%2==0, data)
# print(list(even))
# from functools import reduce
# print(reduce(lambda x,y: x+y, data))

# # 41. module in python
# import check
# print(check.name)
# print(check.age)
# print(check.num)
# print(check.add(5,80))
# from check import *
# print(name)
# print(age)
# print(add(50,96))
# import check as ck
# print(ck.name)
# print(ck.add(52,66))
"""
different folder:
from folder import file
"""


