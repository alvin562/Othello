## Alvin Dantic 20927908.  Project 4.  Lab 5.

import othello

def _number_of_rows() -> int:
    '''Prompts user for number of rows for game board; returns user's response'''
    while True:
        response = input("Enter number of rows: ").strip()
        if response.isdigit() and 4 <= int(response) <= 16 and int(response) % 2 == 0:
            return int(response)
        else:
            print("Invalid entry; number of rows must be even int between 4 and 16")


def _number_of_columns() -> int:
    '''Prompts user for number of columns for game board; returns user's response'''
    while True:
        response = input("Enter number of columns: ").strip()
        if response.isdigit() and 4 <= int(response) <= 16 and int(response) % 2 == 0:
            return int(response)
        else:
            print("Invalid entry; number of columns must be even int between 4 and 16")


def _who_goes_first() -> str:
    '''Asks user who will go first; returns user's response'''
    while True:
        response = input("Enter who goes first (black or white): ").strip().lower()
        if response == 'black':
            return othello.BLACK
        elif response == 'white':
            return othello.WHITE
        else:
            print("Invalid entry; choose black or white")


def _top_left() -> str:
    '''Asks user how the starting pieces of the game should be placed'''
    while True:
        response = input("Enter which piece will go on top left center of board (black or white): ").strip().lower()
        if response == 'black':
            return response
        elif response == 'white':
            return response
        else:
            print("Invalid entry; choose black or white")


def _means_to_win() -> str:
    '''Asks user how the winner should be determined'''
    while True:
        response = input("Enter 'M' if player with more pieces wins or 'L' if less wins: ").strip().lower()
        if response == 'm':
            return response
        elif response == 'l':
            return response
        else:
            print("Invalid entry; enter 'M' or 'L'")

            
def _construct_board(number_of_columns: int, number_of_rows: int) -> [list]:
    '''Given a number of columns and rows, returns a list of lists
       representing the game board
    '''
    board = []
    for i in range(number_of_columns):
        board.append([othello.NONE]*number_of_rows)
    return board


def _construct_board_with_pieces(board: [list], piece: str) -> [list]:
    '''Returns a list of lists with the starting pieces included'''
    if piece == 'black':
        board[(len(board)//2) - 1][(len(board[0])//2) - 1] = othello.BLACK
        board[len(board)//2][len(board[0])//2] = othello.BLACK
        board[(len(board)//2) - 1][len(board[0])//2] = othello.WHITE
        board[len(board)//2][(len(board[0])//2) - 1] = othello.WHITE
        
    elif piece == 'white':
        board[(len(board)//2) - 1][(len(board[0])//2) - 1] = othello.WHITE
        board[len(board)//2][len(board)//2] = othello.WHITE
        board[(len(board)//2) - 1][len(board[0])//2] = othello.BLACK
        board[len(board)//2][(len(board[0])//2) - 1] = othello.BLACK
                            
    return board


def _display_column_numbers(board: [list]) -> None:
    '''Prints column numbers'''
    for i in range(1, len(board) + 1):
        print('{:2}'.format(i), end = ' ')
    print()
        

def _display_board(board: [list]) -> None:
    '''Prints board to console'''
    print('  ', end='')
    _display_column_numbers(board)
    for i in range(len(board[0])):
        print('{:2}'.format(i + 1), end=' ')
        for j in range(len(board)):
            if board[j][i] == othello.NONE:
                print('.', end='  ')
            else:
                print(board[j][i], end='  ')
        print()
    print()


def _display_score(board: [list]) -> None:
    '''Prints the score of each player'''
    print()
    print("      WHITE       BLACK")
    print("    ---------   ---------")
    print("       ", othello.count_pieces(board, othello.WHITE), "         ", othello.count_pieces(board, othello.BLACK))
    print()


def _display_turn(turn: str) -> None:
    '''Prints whose turn it is'''
    if turn.lower() == 'b':
        print()
        print('-------------------------------')
        print("         Black's Turn          ")
        print('-------------------------------')

    elif turn.lower() == 'w':
        print()
        print('-------------------------------')
        print("         White's Turn          ")
        print('-------------------------------')


def _specify_column(board: [list]) -> int:
    '''Prompts user to enter a column number to execute move; returns number'''
    while True:
        response = input("Enter column number (1 to {}): ".format(len(board))).strip()
        if response.isdigit() and 1 <= int(response) <= len(board):
            return int(response) - 1
        else:
            print("Invalid entry; column number must be int between 1 and {}".format(len(board)))


def _specify_row(board: [list]) -> int:
    '''Prompts user to enter a row number to execute move; returns number'''
    while True:
        response = input("Enter row number (1 to {}): ".format(len(board[0]))).strip()
        if response.isdigit() and 1 <= int(response) <= len(board[0]):
            return int(response) - 1
        else:
            print("Invalid entry; column number must be int between 1 and {}".format(len(board[0])))


def _display_winner(board: [list], winner: str, means: str) -> None:
    '''Prints the winner of the game along with the score and the board'''
    _display_score(board)
    _display_board(board)
    if winner == 'TIE':
        print("Game over.  No winner.")

    elif winner == othello.BLACK and means == 'm':
        print("Game over.  Black wins!")

    elif winner == othello.BLACK and means == 'l':
        print("Game over.  White wins!")

    elif winner == othello.WHITE and means == 'm':
        print("Game over.  White wins!")

    elif winner == othello.WHITE and means == 'l':
        print("Game over.  Black wins!")

def _display_everything(board: [list], turn: str) -> None:
    '''Prints everything to the console (i.e. whose turn it is, the score, and the board)'''
    _display_turn(turn)
    _display_score(board)
    _display_board(board)
        


def _prompt_and_execute_move(gamestateobject: othello.GameState, means: str) -> None:
    '''Prompts user to enter a column and row number and executes move if the
       move is valid
    '''
    while True:
        column = _specify_column(gamestateobject.board())
        row = _specify_row(gamestateobject.board())
        try:
            gamestateobject.make_move(column, row)
        except othello.InvalidOthelloMoveError:
            print("Invalid move; try again")
        except othello.OthelloGameOverError:
            _display_winner(gamestateobject.board(), gamestateobject.winner(), means)
        else:
            break

        
def _othello() -> None:
    '''Runs the game of othello'''
    number_of_rows = _number_of_rows()
    number_of_columns = _number_of_columns()
    first = _who_goes_first()
    starting_piece = _top_left()
    how_to_win = _means_to_win()
    board = _construct_board_with_pieces(_construct_board(number_of_columns, number_of_rows), starting_piece)
    game = othello.GameState(board, first)
    while True:

        if game.winner() == othello.NONE:
            _display_everything(game.board(), game.turn())
            _prompt_and_execute_move(game, how_to_win)

        else:
            _display_winner(game.board(), game.winner(), how_to_win)
            break



        
if __name__ == '__main__':
    _othello()
