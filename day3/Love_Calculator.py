# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name=name1+name2
len=len(name)
t=0
r=0
u=0
e=0
l=0
o=0
v=0
for i in range (0,len):
    if name[i]=='T' or name[i] =='t':
        t+=1
    elif name[i]=='R' or name[i] =='r':
        r+=1
    elif name[i]=='U' or name[i] =='u':
        u+=1
    elif name[i]=='E' or name[i] =='e':
        e+=1
    elif name[i]=='L' or name[i] =='l':
        l+=1
    elif name[i]=='O' or name[i] =='o':
        o+=1
    elif name[i]=='V' or name[i] =='v':
        v+=1
a=t+r+u+e
b=l+o+v+e
c=str(a)+str(b)
c=int(c)
if c<10 or c>90:
    print(f"Your score is {c}, you go together like coke and mentos.")
elif c>39 and c<51:
    print(f"Your score is {c}, you are alright together.")
else:
    print(f"Your score is {c}.")


