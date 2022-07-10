from game_over import TicTacTo

print("let's play tic-tac-to")
game_on = True
game = TicTacTo()
game.print_board()
while game_on:
    game.select_position()
    a = game.game_is_over()
    if a:
        play_again = input("play again y/n").upper()
        if play_again == "Y":
            game.print_board()
        else:
            print("Bye")
            break
