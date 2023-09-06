import art
import game_data
import random
import os

shuffled_list = game_data.data
random.shuffle(shuffled_list)

full_point = len(shuffled_list) - 1
point = 0
Game_Over = False


def gamer(Data, Game_statue, Point):
    print(f"Compare A: {Data[-1]['name']} is a(n) {Data[-1]['description']} from {Data[-1]['country']}")
    print(art.vs)
    print(f"Against B: {Data[-2]['name']} is a(n) {Data[-2]['description']} from {Data[-2]['country']}")
    choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()
    if choice == 'A':
        if Data[-1]['follower_count'] > Data[-2]['follower_count']:
            os.system("CLS")
            Point += 1
            print(f"You got it. Your point is {Point}")
        elif Data[-1]['follower_count'] < Data[-2]['follower_count']:
            print(f"Sorry you were wrong. Your final point is {Point}")
            Game_statue += 1
    elif choice == 'B':
        if Data[-1]['follower_count'] < Data[-2]['follower_count']:
            Point += 1
            os.system('cls')
            print(f"You got it. Your point is {Point}")
        elif Data[-1]['follower_count'] > Data[-2]['follower_count']:
            print(f"Sorry you were wrong. Your final point is {Point}")
            Game_statue += 1
    return Game_statue, Point


print("welcome to higherlower game".title())
while point < full_point and not Game_Over:
    print(art.logo)
    Game_Over, point = gamer(shuffled_list, Game_Over, point)
    shuffled_list.pop()
    if not Game_Over and point == full_point:
        print("We should give you a prize. You got the highest possible Point.")

os.system('PAUSE')
