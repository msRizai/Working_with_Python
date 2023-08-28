# We are Playing Rock-Paper-Scissor Game

import random
import time

print("Welcome to the game\n")
choice = ['P', 'S', 'R']
shape = ['🖐', '✌', '✊']

# To set the marks
comp_mark = 0
per_mark = 0
counter = 0

while counter < 3:
    if comp_mark == 2 or per_mark == 2:
        break

    # computer select its choice randomly
    computer = choice[random.randint(0, 3) - 1]
    person = input("Please enter your choice.\t For 🖐 'P' for ✌ 'S' for ✊ 'R'\n").upper()

    # while their choice is the same, it ignores.
    while person == computer:
        print(f"Your choice: {shape[choice.index(person)]}\tPC choice: {shape[choice.index(computer)]}\t it is draw\n")
        time.sleep(3)
        computer = choice[random.randint(0, 3) - 1]
        person = input("Please enter your choice for 🖐 'P' for ✌ 'S' for ✊ 'R'\n").upper()

    # here we go for challenges
    if (person == 'P' and computer == 'S') or (person == 'S' and computer == 'R') or (
            person == 'R' and computer == 'P'):

        print(f"Your choice: {shape[choice.index(person)]}\tPC choice: {shape[choice.index(computer)]}")
        print("Computer got this time\n")
        comp_mark += 1
    else:
        print(f"Your choice: {shape[choice.index(person)]}\tPC choice: {shape[choice.index(computer)]}")
        print("Congratulation you got it\n")
        per_mark += 1

    # to make it fun lets pause it for a while 🤪
    time.sleep(3)
    counter += 1

if per_mark > comp_mark:
    print(f"Congratulation you won the game {per_mark} to {comp_mark}")
else:
    print(f"Try next time. Computer won the game {comp_mark} to {per_mark}")
time.sleep(10)
