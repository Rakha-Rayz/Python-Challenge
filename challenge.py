import random

players = []
challenges = [
    'Clap your hands loudly',
    'Sing',
    'Slap yourself',
    'Jump as high as you can',
    'Slap the person on your left, in front of you, or your opponent',
    'Do something that makes your opponent laugh',
    'Do everything!'
]

print("===== WELCOME TO THE CHALLENGE GAME =====")

# Game handler
def play():
    while True:
        selected_player = random.choice(players)
        selected_challenge = random.choice(challenges)

        print(f"The challenge will be given to {selected_player}, which is {selected_challenge}")
        print("Or simply like this")
        print(selected_player + ": " + selected_challenge)

        proceed = input("Continue? Y/n: ")
        proceed.lower()

        if proceed == "y":
            print("Okay, the game continues")
            continue
        else:
            print("Game over!")
            exit()

# Player handler
def setup_players():
    try:
        total_players = int(input("Enter number of players: "))
        for i in range(total_players):
            player_name = input(f"Enter name of player {i + 1}: ")
            if player_name == "":
                print("Name cannot be empty")
                exit()
            players.append(player_name)
    except ValueError:
        print("Please enter a number")

if not players:
    setup_players()

play()
