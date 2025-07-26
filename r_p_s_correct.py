import random
players_win_count = 0
computer_win_count = 0
game_selection = ["rock" , "paper", "scissors"]

while players_win_count < 3 and computer_win_count < 3:
    players_choice = input("Please select rock, paper, or scissors: ")
    computer_play = random.choice(game_selection)
    while players_choice not in game_selection:
        players_choice = input("Invalid selection, please type rock, paper, scissors:")
    if players_choice == computer_play:
        print("You tied!")
        print(f"Total wins are : \n Player: {players_win_count} \n Computer: {computer_win_count}")
    elif (players_choice == "rock" and computer_play == "scissors") or \
        (players_choice == "paper" and computer_play == "rock") or \
        (players_choice == "scissors" and computer_play == "paper"):
        print("You win!")
        players_win_count += 1
        print(f"Total wins are : \n Player: {players_win_count} \n Computer: {computer_win_count}")
    else:
        print("Computer wins nah!") 
        computer_win_count += 1
        print(f"Total wins are : \n Player: {players_win_count} \n Computer: {computer_win_count}")


