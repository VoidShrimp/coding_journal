def main():
    answer = "brand"
    hidden_answer = []
    for letter in answer:
        hidden_answer.append(letter)
    is_playing = True
    hidden_word = ["_","_","_","_","_"]
    wrong_guess = 1
    attempts = 6
    duplicate = []

    while is_playing:
        print("Please guess a letter (or enter . to quit): ")
        guess = input()

        if guess == ".":
            is_playing = False

        elif duplicate.count(guess) != 0:
            print(f"You've already guessed {guess}, try a different letter")
            is_playing = True

        elif answer.find(guess) != -1:
            duplicate.append(guess)
            position = int(answer.find(guess))
            hidden_word.pop(position)
            hidden_word.insert(position, guess)
            #new_hidden_word = hidden_word.replace(hidden_word[position], guess)
            for word in hidden_word:
                print(word, end=" ")
            print()
            create_game_board(wrong_guess)
            if hidden_answer == hidden_word:
                print("YOU WIN!")
                is_playing = False

        elif answer.find(guess) == -1:
            duplicate.append(guess)
            print(f"Sorry, {guess} is wrong guess")
            wrong_guess += 1
            attempts_left = attempts - wrong_guess

            if attempts_left <= 0:
                create_game_board(5)
                print("Sorry, you lose")
                is_playing = False

            create_game_board(wrong_guess)
            print(f"You have {attempts_left} attempts left.")

        else:
            print("Invalid guess,try again.")
            is_playing = True


def create_game_board(wrong_guess):
    game_board = {1: ("____________",
                      "_    |     _",
                      "           _",
                      "           _",
                      "           _",
                      "           _",
                      "           _",
                      "_____________"),
                  2: ("____________",
                      "_    |     _",
                      "     O     _",
                      "           _",
                      "           _",
                      "           _",
                      "           _",
                      "_____________"),
                  3: ("____________",
                      "_    |     _",
                      "     O     _",
                      "    -|     _",
                      "           _",
                      "           _",
                      "           _",
                      "_____________"),
                  4: ("____________",
                      "_    |     _",
                      "     O     _",
                      "    -|-    _",
                      "           _",
                      "           _",
                      "           _",
                      "_____________"),
                  5: ("____________",
                      "_    |     _",
                      "     O     _",
                      "    -|-    _",
                      "    |      _",
                      "           _",
                      "           _",
                      "_____________"),
                  6: ("____________",
                      "_    |     _",
                      "     O     _",
                      "    -|-    _",
                      "    | |    _",
                      "           _",
                      "    End    _",
                      "_____________")
                  }
    boards = game_board[wrong_guess]
    for board in boards:
        print(board)

main()