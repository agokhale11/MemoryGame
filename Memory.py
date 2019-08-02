#Aditya Gokhale

import random

class MemoryGame:
    board = [[[0, 0] for i in range(4)] for j in range(13)]
    correct_guesses = 0
    users = []



    def __init__(self):
        suit_counter = 1
        number_counter = 1
        for x in range(1, 53):
            next_card = [suit_counter, number_counter]
            row = random.randint(0, 12)
            col = random.randint(0, 3)
            while self.board[row][col] != [0,0]:
                row = random.randint(0, 12)
                col = random.randint(0, 3)

            self.board[row][col] = next_card
            suit_counter += 1
            number_counter += 1
            if suit_counter == 5:
                suit_counter = 1
            if number_counter == 14:
                number_counter = 1


    def set_user(self, num):
        self.users = num

    def get_user(self):
        return self.users

    def is_valid_guess(self, r_one, c_one, r_two, c_two):
        if r_one > 12 or r_two > 12 or c_one > 3 or c_two > 3:
            return '\nPlease enter a valid guess'
        elif self.board[r_one][c_one] == [0,0] or self.board[r_two][c_two] == [0,0]:
            return '\nOne or more of the spots has already been guessed!'
        else:
            return True

    def check_guess(self, card_one, card_two):
        return card_one[1] == card_two[1]

    def is_completed(self):
        return self.correct_guesses == 26

    def set_cell(self, first_row, first_col, second_row, second_col):
        self.board[first_row][first_col] = [0,0]
        self.board[second_row][second_col] = [0, 0]

    def get_guesses(self):
        invalid = True
        while True:
            try:
                while invalid:
                    r_one = int(input("Please enter integer for row of first guess (0-12)"))
                    c_one = int(input("Please enter integer for col of first guess (0-3)"))
                    r_two = int(input("Please enter integer for row of second guess (0-12)"))
                    c_two = int(input("Please enter integer for col of second guess (0-3)\n"))

                    if self.is_valid_guess(r_one, c_one, r_one, c_two) == True:
                        invalid = False
                    else:
                        print(self.is_valid_guess(r_one, c_one, r_two, c_two))

            except ValueError:
                print("\nPlease enter valid integer values for rows and columns\n")
                continue
            else:
                break
        return [r_one, c_one, r_two, c_two]

    def get_card_name(self, card):
        if card[0] == 1:
            return "Hearts"
        elif card[0] == 2:
            return "Spades"
        elif card[0] == 3:
            return "Diamonds"
        else:
            return "Clubs"

    def display_board(self, r_one, c_one, r_two, c_two):
        printed_board = [["X" for i in range(4)] for j in range(13)]
        printed_board[r_one][c_one] = "1"
        printed_board[r_two][c_two] = "2"

        row = ""
        for x in range(len(printed_board)):
            for y in range(len(printed_board[x])):
                if self.board[x][y] == [0,0]:
                    printed_board[x][y] = "O"
                row += " " + printed_board[x][y]
            print(row)
            row = ""
