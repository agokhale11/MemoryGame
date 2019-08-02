from Memory import MemoryGame

choice = 'Y'
while choice == 'Y':
    game = MemoryGame()

    print("Welcome to the Memory Game!\n")

    while True:
        try:
            num_users = int(input("Please enter an integer number of players > 0\n"))
        except ValueError:
            continue
        else:
            break

    game.users = [0 for i in range(num_users)]

    player_count = 0
    while not game.is_completed():
        print("Player " + str(player_count + 1) + " guess:")

        guesses = game.get_guesses()
        r_one = guesses[0]
        c_one = guesses[1]
        r_two = guesses[2]
        c_two = guesses[3]

        card_one = game.board[guesses[0]][guesses[1]]
        card_two = game.board[guesses[2]][guesses[3]]

        if game.check_guess(card_one, card_two):
            game.users[player_count] += 1
            game.correct_guesses += 1
            game.set_cell(r_one, c_one, r_two, c_two)

            print("You got a match! It was: ")

        else:
            print("Sorry! The cards were not a match:")

        print("First: " + str(card_one[0]) + " of " + game.get_card_name(card_one) + ". Second: " + str(card_two[0])
              + " of " + game.get_card_name(card_two))

        game.display_board(r_one, c_one, r_two, c_two)

        if player_count == num_users - 1:
            player_count = 0
        else:
            player_count += 1

    print("That's the game! Final scores:")

    max_score = 0
    max_player = 0
    for i in range(num_users):
        print("Player " + str(i) + " : " + str(game.users[i - 1]))
        if game.users[i - 1] > max_score:
            max_score = game.users[i - 1]
            max_player = i

    print("Player " + str(max_player) + " wins!")

    choice = input("Would you like to play again? (Enter Y or N)")



