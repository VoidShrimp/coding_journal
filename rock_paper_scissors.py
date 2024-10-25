import random

def main():
    print("What do you choose?\nRock, Paper, or Scissors: ")
    user_option= (input())
    computer_options = ("rock", "paper", "scissors")
    computer_option = random.choice(computer_options)
    game_loop(user_option, computer_option)

def game_loop(user_option, computer_option):
    if user_option.lower() == "scissors" and computer_option == "paper":
        print(f"{user_option} beats {computer_option}, You win!")
    elif user_option.lower() == "rock" and computer_option == "scissors":
        print(f"{user_option} beats {computer_option}, You win!")
    elif user_option.lower() == "paper" and computer_option == "rock":
        print(f"{user_option} beats {computer_option}, You win!")
    elif user_option.lower() == computer_option:
        print(f"It's a tie! {computer_option} ties {user_option}.")
    elif user_option.lower() != "scissors" and user_option.lower() != "rock" and user_option.lower() != "paper":
        print(f"{user_option} is not a valid choice. Start over.")
    else:
        print(f"{computer_option} beats {user_option}, You lose")

main()