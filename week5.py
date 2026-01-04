# 41. regex
from blib2to3.pgen2.tokenize import Ignore
text = """We will hold AtCoder Beginner Contest 439
- Contest URL: https://atcoder.jp/contests/abc439
- Start Time: http://www.timeanddate.com/worldclock/fixedtime.html?iso=20260103T2100&p1=248
- Duration: 100 minutes
- Writer: physics0523, Nyaan, kyopro_friends, blackyuki
- Tester: MMNMM, yuto1115
- Rated range: ~ 1999
- The point values: 100-200-300-425-450-525-650
We are looking forward to your participation!
- How to Unsubscribe Email Newsletters
1: First, please sign in => https://atcoder.jp/login
2: Clear all 'Notification settings' from => https://atcoder.jp/settings
AtCoder Development Team
https://atcoder.jp/
If you wish to unsubscribe from this mailing list, please click the link below."""
import re
pattern = r"\d+"
match = re.search(pattern,text)
print(match)
pattern = r"\d+"
match = re.findall(pattern,text)
print(match)
pattern = r"https?://[a-z]+\.[a-z]+/[a-z]+"
match = re.findall(pattern,text)
print(match)
pattern = r"\d{3}-\d{3}-\d{3}-\d{3}-\d{3}-\d{3}-\d{3}"
match = re.search(pattern,text)
print(match)
pattern = r"\s+"
match = re.split(pattern,text)
print(match)
pattern = r"Email"
match = re.sub(pattern,"contact",text)
print(match)
pattern = r"we"
match = re.match(pattern,text, re.I)
print(match)

# 42. pytubefix
from pytubefix import YouTube
from pytubefix.cli import on_progress
url = "https://www.youtube.com/watch?v=mk48xRzuNvA&list=RDmk48xRzuNvA&start_radio=1"
yt = YouTube(url,on_progress_callback=on_progress)
print(yt.title)
stream = yt.streams.get_highest_resolution()
stream.download()

# 43.write, append, read file in python
# for .txt file
with open(r"text_demo.txt","w") as file:
    file.write(text)
with open(r"text_demo.txt","r") as file:
    content = file.read()
    print(content)
with open(r"text_demo.txt","a") as file:
    file.write(text)
# .csv file
import csv
data = [(1,"Alex",18,"computer"),
        (2,"Bob",19,"mathematics"),
        (3,"Sammy",19,"biology")]
with open(r"demo.csv","w",newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
import csv
data = [(1,"Alex",18,"computer"),
        (2,"Bob",19,"mathematics"),
        (3,"Sammy",19,"biology")]
with open(r"demo.csv","a",newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
import csv
with open(r'demo.csv',"r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# .json file
import json
dic = {
    "name": "Spongebob",
    "age": 30,
    "country": "usa",
    "major": "cse",
    "current": "usa"
}
with open(r"test.json","w") as file:
    json.dump(dic,file,indent=4)
import json
with open(r"test.json","r") as file:
    content = json.load(file)
    print(content)

# 44. generators
def maxi(x:int):
    count = 1
    while count<=x:
        yield count
        count += 1
counter = maxi(10)
print(next(counter))
print(next(counter))
print(next(counter))

#45. PyPDF2
from PyPDF2 import PdfReader
with open(r"2025.pdf","rb") as file:
    content = PdfReader(file).pages[0].extract_text()
    print(content)

# 46. variable scope LEGB = Local,Enclosed,Global,Built-in
from math import pi #built-in
num3 = 123 #global
def var():
    num3 = 456 #enclosed
    print(num3)
    def encl():
         #local
        num3 = 7798
        print(num3)
    encl()
print(num3)
print(pi)
var()

# 47. webbrowser module
import webbrowser
url = r"https://chatgpt.com/c/69450bb5-f280-8324-b4f5-385039932a62"
webbrowser.open(url)

# 48. if __name__ == "__main__":
def about(name,age,school):
    return f"The student is {name}, {age} years old. The school name is {school}"

def main():
    name = "bob"
    age = 35
    school = "bro code"
    print(about(name,age,school))
if __name__ == "__main__":
    main()

# 49. banking program
#
# 50. slot machine

# 51. encryption
import random
import string
from copy import deepcopy
chars = list(string.whitespace+string.punctuation+string.ascii_letters+string.digits)
rand = deepcopy(chars)
random.shuffle(rand)
print(chars)
print(rand)
mess = input("Enter your message: ")
encrypt = ""
for ch in mess:
    ind = chars.index(ch)
    encrypt += rand[ind]
print(mess)
print(encrypt)

# 52. hangman program

# 53. file detection
import os
file_path = r"C:\Users\Taiyob Ali\Desktop\myportfolio_Linkedin,Github\python full course basic to advance\This_is_unzip1"
if os.path.exists(file_path):
    print("File exists")
    if os.path.isfile(file_path):
        print("it's a file")
    elif os.path.isdir(file_path):
        print("it's a dir")
else:
    print("File is not exists")

