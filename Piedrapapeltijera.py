print("Welcome to this Rock, Paper, Scissors game")

print("Player 1 name:")
Player_1_name = input()

print("Player 2 name:")
Player_2_name = input()

print(Player_1_name, "What's yout pick?: Rock, Paper, Scissors")
player_1_move = input()

print(Player_1_name, "You choose", player_1_move)

print(Player_2_name, "What's yout pick?: Rock, Paper, Scissors")
player_2_move = input()

print(Player_2_name, "You choose", player_2_move)

valid_moves = ["Rock", "Paper", "Scissors"]

if player_1_move not in valid_moves or player_2_move not in valid_moves:
    print("Players, please check your picks as one or both are invalid picks. (don't play like that mf)")
    
else:
    if player_1_move == player_2_move:
        print("It's a Tie!")
    elif (player_1_move == "Rock" and player_2_move == "Scissors") or (player_1_move == "Scissors" and player_2_move == "Paper") or (player_1_move == "paper" and player_2_move == "Rock"):
        print(Player_1_name, "¡WINS!")
    
    else:
        print(Player_2_name, "¡WINS!")