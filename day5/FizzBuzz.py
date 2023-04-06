#Write your code below this row 👇

for x in range(1,101):
    if x%3==0 and x%5==0:
        x="FizzBuzz"
    elif x%5==0:
        x="Buzz"
    elif x%3==0:
        x="Fizz"
    print(x)