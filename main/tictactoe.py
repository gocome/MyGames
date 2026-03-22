

class Player:
    def __init__(self, type):
        self.type = type
        self.input1 = 0
        self.waiting = True

    def checkline(self, num1, num2, num3):
        if grid[str(num1)] == self.type and grid[str(num2)] == self.type and grid[str(num3)] == self.type:
            return True
        return False

    def checkwin(self):
        if self.checkline(1,2,3):
            return True
        elif self.checkline(4,5,6):
            return True
        elif self.checkline(7,8,9):
            return True

        elif self.checkline(1,4,7):
            return True
        elif self.checkline(2,5,8):
            return True
        elif self.checkline(3,6,9):
            return True

        elif self.checkline(1,5,9):
            return True
        elif self.checkline(3,5,7):
            return True
        else:
            return False


    def playturn(self):
        self.waiting = True
        while self.waiting:
            self.input1 = input(f"Player {self.type}, type your move: ")

            if self.input1.isdigit():

                input1 = int(self.input1)
                if input1 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if grid[str(input1)] == "_" or grid[str(input1)] == " ":
                        grid[str(input1)] = self.type
                        show_board(grid)
                        self.waiting = False
                    else:
                        show_board(grid)
                        print("Already played")
                else:
                    show_board(grid)
                    print("Must be 1 to 9")
            else:
                show_board(grid)
                print("Invalid input")


X = Player("X")
O = Player("O")

def show_board(grid):
    print(f""" _{grid["1"]}_|_{grid["2"]}_|_{grid["3"]}_
 _{grid["4"]}_|_{grid["5"]}_|_{grid["6"]}_
  {grid["7"]} | {grid["8"]} | {grid["9"]} """)


def checkdraw():
    if not grid["1"] == "_" and not grid["2"] == "_" and not grid["3"] == "_":
        if not grid["4"] == "_" and not grid["5"] == "_" and not grid["6"] == "_":
            if not grid["7"] == " " and not grid["8"] == " " and not grid["9"] == " ":
                return True
            return False
        return False
    return False

print()
print("Tictactoe")
print(f"Play by typing the number of the square you want to play like this:")

grid = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

show_board(grid)

realgrid = {
    "1": "_",
    "2": "_",
    "3": "_",
    "4": "_",
    "5": "_",
    "6": "_",
    "7": " ",
    "8": " ",
    "9": " "
}

grid.update(realgrid)

print()
show_board(grid)


playing = True

while playing:
    X.playturn()
    if X.checkwin():
        print("X is the winner!")
        playing = False
        break
    if checkdraw():
        print("Draw!")
        playing = False
        break
    O.playturn()
    if O.checkwin():
        print("O is the winner!")
        playing = False
        break
    if checkdraw():
        print("Draw!")
        playing = False
        break