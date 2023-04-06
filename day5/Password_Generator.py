# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
print("Welcome to the PyPassword Generator!")
apl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9','0']
sym = ['!','@','#','$','%','^','&','*','(',')','_','+']
a=int(input("How many letters would you like in your password\n"))
b=int(input("How many numbers would you like in your password\n"))
c=int(input("How many symbols would you like in your password\n"))
list1=[]
for i in range(0,a):
    list1.append(random.choice(apl))
for i in range(0,b):
    list1.append(random.choice(num))
for i in range(0,c):
    list1.append(random.choice(sym))
random.shuffle(list1)
password = ""
for i in list1:
    password += i
print(password)
