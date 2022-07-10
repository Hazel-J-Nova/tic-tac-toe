import board
class TicTacTo:

    def __init__(self):
        self.board = self.board = " 1|2|3\n" \
                                  " _|_|_\n" \
                                  " 4|5|6\n" \
                                  " _|_|_\n" \
                                  " 7|8|9\n" \
                                  "  | | "
        self.position = [i for i, element in enumerate(self.board) if self.board[i].isnumeric()]
        self.game_over = False
        self.turn = 1

    def game_is_over(self):

        if self.board[(self.position[0])] == self.board[(self.position[1])] == self.board[(self.position[2])]:
            print(f'{self.board[(self.position[0])]} won the game')
            return True, self.position[0]
        elif self.board[(self.position[3])] == self.board[(self.position[4])] == self.board[(self.position[5])]:
            print(f'{self.board[(self.position[3])]} won the game')
            return True, self.position[3]
        elif self.board[(self.position[6])] == self.board[(self.position[7])] == self.board[(self.position[8])]:
            print(f'{self.board[(self.position[6])]} won the game')
            return True, self.position[6]
        elif self.board[(self.position[0])] == self.board[(self.position[3])] == self.board[(self.position[6])]:
            print(f'{self.board[(self.position[0])]} won the game')
            return True, self.position[0]
        elif self.board[(self.position[1])] == self.board[(self.position[4])] == self.board[(self.position[7])]:
            print(f'{self.board[(self.position[1])]} won the game')
            return True, self.position[1]
        elif self.board[(self.position[2])] == self.board[(self.position[5])] == self.board[(self.position[8])]:
            print(f'{self.board[(self.position[2])]} won the game')
            return True, self.position[2]
        elif self.board[(self.position[0])] == self.board[(self.position[4])] == self.board[(self.position[8])]:
            print(f'{self.board[(self.position[0])]} won the game')
            return True, self.position[0]
        elif self.board[(self.position[2])] == self.board[(self.position[4])] == self.board[(self.position[6])]:
            print(f'{self.board[(self.position[2])]} won the game')
            return True, self.position[2]
        else:
            return False

    def update_board(self, place):
        if self.turn % 2 == 0:
            self.board = self.board.replace(place, "O")
            self.turn += 1
        else:
            self.board = self.board.replace(place, "X")
            self.turn += 1

    def print_board(self):
        print(self.board)

    def check_if_position(self, position):
        while not self.board[position].isnumeric():
            position = int(input("Select where you wish to place you token"))


    def select_position(self):
        position = int(input("Select where you wish to place you token"))
        self.check_if_position(position)
        str_position = str(position)
        self.update_board(str_position)

        self.print_board()


board = TicTacTo()
