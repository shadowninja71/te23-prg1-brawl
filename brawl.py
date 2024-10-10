from random import randint

player_one_name = input('skriv in dit namn:') 

player_one_life = 10
player_two_life = 10

round = 0

while player_one_life > 0 and player_two_life > 0:

        player_one_role = randint(1, 6)
        player_two_role = randint(1, 6)

        if player_one_role > player_two_role:
                if player_one_role == 6:
                    print(f"{player_one_name} rulade en 6 och gjorde dubelt så mycket skada på spelare två")
                    player_two_life -= 2
                    round += 1
                    input("enter:")
                elif player_one_role == 1:
                    print(f"{player_one_name} rulade en 1 och misade")
                    round += 1
                    input("enter:")

                else:
                    print(f"{player_one_name} van med tärningskastet: {player_one_role}")
                    player_two_life -= 1
                    round += 1
                    input("enter:")
        elif player_two_role > player_one_role:
                if player_two_role == 6:
                    print(f"spelare två rulade en 6 och gjorde dubelt så mycket skada på {player_one_name}")
                    player_one_life -= 2
                    round +=1
                    input("enter:")
                elif player_one_role == 1:
                    print(f"spelare två rulade en 1 och misade")
                    round += 1
                    input("enter:")
                else:
                    print(f"Spelare två van med tärningskastet: {player_two_role}")
                    player_one_life -= 1
                    round += 1
                    input("enter:")
        else:
                print(f"ingen spelare van, det är oavgjort med tärningstalet: {player_one_role}")
                round += 1
                input("enter")
        if player_one_life == 0:
                print(f"spelare två van med {player_two_life} liv kvar")
                print(f"och det tog {round} runder för spelare twå att vina")
        elif player_two_life == 0:
                print(f"{player_one_name} van med {player_one_life} liv kvar")
                print(f"och det tog {round} runder för {player_one_name} att vina")