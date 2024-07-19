import random
choices = ["R", "P", "S"]
player = False
cpu_score = 0
player_score = 0
n = int(input("how many times u want to play"))
while n>0:
    n = n-1
    computer = random.choice(choices)

    player = input("Rock(R), Paper(P) or  Scissors(S)?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "P":
        if computer == "S":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "S":
        if computer == "R":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1

print("\n")
print("Final Scores:")
print(f"CPU:{cpu_score}")
print(f"Plaer:{player_score}")