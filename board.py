class Board():
    def __init__(self):
        self.board = " 1|2|3\n" \
        " _|_|_\n" \
        " 4|5|6\n" \
        " _|_|_\n" \
        " 7|8|9\n" \
        "  | | "
        self.postion =  [i for i, element in enumerate(self.board) if self.board[i].isnumeric()]
board = Board()
