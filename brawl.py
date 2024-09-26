from random import randint

input('Enter your name:')
x = input()

player_one_life= 10
player_two_life = 10

player_one_role = randint(1, 6)
player_two_role = randint(1, 6)

if player_one_role > player_two_role:
        print(f"Spelare ett vinner med tärningskastet: {player_one_role}")
        player_two_life -= 1
elif player_two_role > player_one_role:
        print(f"Spelare två vinner med tärningskastet: {player_two_role}")
        player_one_life -= 1
else:
        print(f"ingen spelare vinner, det är oavgjort med tärningstalet: {player_one_role}")
if player_one_life == 0:
        print(f"spelare två van med {player_two_life} kvar")
elif player_two_life == 0:
        print(f"spelare ett van med {player_one_life} kvar")