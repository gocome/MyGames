import numpy as np


class Player:
    def __init__(self, type):
        self.type = type
        self.input1 = 0
        self.waiting = True
        self.grid = np.full((10, 10), "_")
        self.shipsplaced = []

    def show_board(self):
        # Print the header numbers
        print("    1   2   3   4   5   6   7   8   9   10")

        # Define row labels
        rows = "ABCDEFGHIJ"

        for i in range(10):
            # Start the line with the Letter (A, B, C...)
            row_str = f"{rows[i]} "

            # Loop through each column in that row
            for j in range(10):
                row_str += f"|_{self.grid[i, j]}_"

            # Close the last cell and print the row
            print(row_str + "|")

    def check_coords(self, input2):
        if len(input2) == 2 or len(input2) == 3:
            letter = input2[0]
            number = input2[1:]
            if letter.isalpha() and number.isdigit():
                row_val = letter.upper()
                col_val = int(number)
                if "A" <= row_val <= "J" and 1 <= col_val <= 10:
                    row_idx = ord(letter) - ord("A")
                    col_idx = int(number) - 1
                    return row_idx, col_idx
                else:
                    print("Must be on the board")
                    return None, None
            else:
                print("Invalid input")
                return None, None
        else:
            print("Must be a coordinate")
            return None, None

    def place_ships(self):

        ships_list = [2,3,3,4,5]
        waiting = True
        print(f"Player {self.type}, place your ships: ")
        print("Ships left: ", ships_list)
        while self.waiting:
            for ship in ships_list:
                end1_row, end1_col = None, None
                end2_row, end2_col = None, None
                while True:
                    while end1_row is None:
                        coords = input("Enter end of a ship: ")
                        end1_row, end1_col = self.check_coords(coords)

                    while end2_row is None:
                        coords = input("Enter the other end of a ship: ")
                        end2_row, end2_col = self.check_coords(coords)
                    if not end1_row == end2_row or not end1_col == end2_col:
                        if end1_row == end2_row:
                            ship_len = abs(end1_col - end2_col)
                            if ship_len in ships_list:
                                print(ship_len)
                                ships_list.remove(ship_len)
                                break
                            else:    # have to check if the inputs are already placed, and ship has already been placed
                                # create a list of filled spots?




                                print(ship_len)
                                print("This ship has already been placed or is too long.")
                        elif end1_col == end2_col:
                            ship_len = abs(end1_row - end2_row)

                        else:
                            print("Must place a ship on a straight line")
                    else:
                        print("Ships must be longer than 1 square")
                    end1_row, end1_col = None, None
                    end2_row, end2_col = None, None







    def playturn(self):
        self.waiting = True

        while self.waiting:
            self.input1 = input(f"Player {self.type}, type your move: ")
            # if len(self.input1) ==


            if self.input1.isdigit():

                input1 = int(self.input1)
                if input1 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if self.grid[str(input1)] == "_" or self.grid[str(input1)] == " ":
                        self.grid[str(input1)] = self.type
                        self.waiting = False
                    else:
                        print("Already played")
                else:
                    print("Must be 1 to 9")
            else:
                print("Invalid input")

P1 = Player("1")
P2 = Player("2")


P1.show_board()

playing = True

while playing:
    P1.place_ships()