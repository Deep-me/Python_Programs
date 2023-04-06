# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
computer=[rock, paper, scissors]
c = random.choice(computer)
a=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if a==0:
  b=rock
  print(b) 
elif a==1:
  b=paper
  print(b)
else:
  b=scissors
  print(b)
print(f"Computer Chose:\n {c}")
if b==c:
  print("It's a draw")
else:
  if b==rock and c==scissors:
    print("You win")
  elif b==paper and c==rock:
    print("You win")
  elif b==scissors and c==paper:
    print("You win")
  else:
    print("You lose")
