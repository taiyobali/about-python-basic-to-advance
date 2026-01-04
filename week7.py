# 64. exception handle and raise error
"""
try:
except:
finally:
"""
try:
    user = int(input("Enter a int num🧑🏼‍💻: "))
    print(f"{user} it's correct")
except TypeError:
    print("You don't allow to give another type data idiot!")
except ValueError:
    print("You must try with int value.")
except Exception:
    print("something wrong")
finally:
    print("this is try-except-finally test")

try:
    age = int(input("enter age: "))
    if age<=0:
        raise ValueError("You are not to be less than zero idiot!")
    else:
        print(f"you are {age}")
except TypeError:
    print("something wrong")
finally:
    print(f"learn from mistakes")

# 65. datetime module
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(today)
print(now)
date = datetime.date(2026,1,7)
print(date)

# 66. multithreading
import threading
import time
def walking(first,last):
    time.sleep(8)
    print(f"bro is walking for 8 seconds with {first} {last}")
def clean_up():
    time.sleep(2)
    print("it should takes two seconds to clean up")
def eat():
    time.sleep(4)
    print("you ate the coffee in 4 seconds! how?")

thread1 = threading.Thread(target=walking,args=("Sponge","bob"))
thread1.start()
thread2 = threading.Thread(target=clean_up)
thread2.start()
thread3 = threading.Thread(target=eat)
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("all those tasks are completed")

# 67. requests API
import requests
url = "https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    address = url+"/pokemon/"+name
    response = requests.get(address)
    if response.status_code == 200:
        return response.json()
    else:
        print("you can't retrieve data now.")

pokemon = "pikachu"
data = get_pokemon_info(pokemon)
print(f"name: {data["name"]}")
print(f"id: {data["id"]}")
print(f"height: {data["height"]}")
print(f"weight: {data["weight"]}")


# 68. weather api
import requests
api = "9d21829b925a160abe4bd346791dfa70"
def get_weather():
    address = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api}"
    response = requests.get(address)
    if response.status_code == 200:
        return response.json()
    else:
        print("something wrong")
data = get_weather()
print(round(data["list"][0]["main"]["temp"]-273.15))







