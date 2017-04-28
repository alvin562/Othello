## Alvin Dantic 20927908.  Project 4.  Lab 5


############################
## GAMESTATE CLASS
############################


class GameState:
    def __init__(self, board: [list], turn: str) -> None:
        '''Initializes a GameState consisting of a board and whose turn it is'''
        self._board = board
        self._turn = turn

    def board(self) -> [list]:
        '''Returns a list of lists representing the game board'''
        return self._board

    def turn(self) -> str:
        '''Returns whose turn it is'''
        return self._turn

    def rows(self) -> int:
        '''Returns number of rows in game board'''
        return len(self._board[0])

    def columns(self) -> int:
        '''Returns number of columns in game board'''
        return len(self._board)

    def cell(self, col: int, row: int) -> str:
        '''Returns which piece is in specified cell; returns ' ' if cell isn't
           occupied
        '''
        _require_valid_column_number(self._board, col)
        _require_valid_row_number(self._board, row)
        
        return self._board[col][row]

    def winner(self) -> str:
        '''Returns winner of game; returns 'TIE' if a tie occurs and ' '
           if game isn't over
        '''
        try:
            _require_game_not_over(self._board)

        except:
            
            if count_pieces(self._board, 'B') > count_pieces(self._board, 'W'):
                return 'B'
            elif count_pieces(self._board, 'W') > count_pieces(self._board, 'B'):
                return 'W'
            elif count_pieces(self._board, 'W') == count_pieces(self._board, 'B'):
                return "TIE"
        else:
            return ' '

    def make_move(self, col: int, row: int) -> None:
        '''Given a column and row number, executes move and raises
           InvalidOthelloMoveError if move is invalid
        '''
        _require_valid_column_number(self._board, col)
        _require_valid_row_number(self._board, row)
        _require_game_not_over(self._board)
            
        if _is_valid_move(self._board, self._turn, col, row) and _moves_are_available(self._board, self._turn):

            self._board = _flip_pieces(self._board, self._turn, col, row)
            self._board[col][row] = self._turn
            self._turn = _opposite_turn(self._turn)

            if not _moves_are_available(self._board, self._turn):
                self._turn = _opposite_turn(self._turn)

        else:
            raise InvalidOthelloMoveError()
        

##############################
## MISCELLANEOUS FUNCTIONS
##############################


def _require_valid_column_number(board: [list], column: int) -> None:
    '''Raises a ValueError if its parameter is not a valid column number'''
    if type(column) != int or not _is_valid_column_number(board, column):
        raise ValueError("Column number must be int between 0 and {}".format(len(board) - 1))


def _require_valid_row_number(board: [list], row: int) -> None:
    '''Raises a ValueError if its parameter is not a valid row number'''
    if type(row) != int or not _is_valid_row_number(board, row):
        raise ValueError("Row number must be int between 0 and {}".format(len(board[0]) - 1))
    
                         
def _is_valid_column_number(board: [list], column: int) -> bool:
    '''Returns True if the given column number is valid; returns False otherwise'''
    return 0 <= column < len(board)


def _is_valid_row_number(board: [list], row: int) -> bool:
    '''Returns True if the given row number is valid; returns False otherwise'''
    return 0 <= row < len(board[0])


def _opposite_turn(turn: str) -> str:
    '''Given the player whose turn it is now, returns the opposite player'''
    if turn == 'W':
        return 'B'
    else:
        return 'W'
    

def _is_valid_move(board: [list], turn: str, col: int, row: int) -> bool:
    '''Return True if move is valid in at LEAST one direction'''
    return _is_valid_move_in_direction(board, turn, col, row, 0, 1) \
           or _is_valid_move_in_direction(board, turn, col, row, 1, 1) \
           or _is_valid_move_in_direction(board, turn, col, row, 1, 0) \
           or _is_valid_move_in_direction(board, turn, col, row, 1, -1) \
           or _is_valid_move_in_direction(board, turn, col, row, 0, -1) \
           or _is_valid_move_in_direction(board, turn, col, row, -1, -1) \
           or _is_valid_move_in_direction(board, turn, col, row, -1, 0) \
           or _is_valid_move_in_direction(board, turn, col, row, -1, 1)


def _is_valid_move_in_direction(board: [list], turn: str, col: int, row: int, coldelta: int, rowdelta: int) -> bool:
    '''Return True if move is valid in specified direction'''
    if board[col][row] == ' ':
        i = 1
        while _is_valid_column_number(board, col + coldelta*i) and _is_valid_row_number(board, row + rowdelta*i):
            if board[col + coldelta*i][row + rowdelta*i] == ' ' or (i == 1 and board[col + coldelta*i][row + rowdelta*i] == turn):
                return False
            elif board[col + coldelta*i][row + rowdelta*i] == _opposite_turn(turn):
                i += 1
            elif i >= 2 and board[col + coldelta*i][row + rowdelta*i] == turn:
                return True
        return False
    return False


def _flip_pieces_in_direction(board: [list], turn: str, col: int, row: int, coldelta: int, rowdelta: int) -> [list]:
    '''Flips pieces in a specified direction'''
    if _is_valid_move_in_direction(board, turn, col, row, coldelta, rowdelta):
        i = 1
        while not board[col + coldelta*i][row + rowdelta*i] == turn:
            board[col + coldelta*i][row + rowdelta*i] = turn
            i += 1
    return board


def _flip_pieces(board: [list], turn: str, col: int, row: int) -> [list]:
    '''Flips pieces in directions where the specified move is valid'''
    board1 = _flip_pieces_in_direction(board, turn, col, row, 0, 1)
    board2 = _flip_pieces_in_direction(board1, turn, col, row, 1, 1)
    board3 = _flip_pieces_in_direction(board2, turn, col, row, 1, 0)
    board4 = _flip_pieces_in_direction(board3, turn, col, row, 1, -1)
    board5 = _flip_pieces_in_direction(board4, turn, col, row, 0, -1)
    board6 = _flip_pieces_in_direction(board5, turn, col, row, -1, -1)
    board7 = _flip_pieces_in_direction(board6, turn, col, row, -1, 0)
    board8 = _flip_pieces_in_direction(board7, turn, col, row, -1, 1)
    return board8


def _moves_are_available(board: [list], turn: str) -> bool:
    '''Returns True if there are moves available for the specified player'''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if _is_valid_move(board, turn, i, j):
                return True
    return False


def _require_game_not_over(board: [list]) -> None:
    '''
    Raises an OthelloGameOverError if the given board represents a situation
    where the game is over
    '''
    if not _moves_are_available(board, 'B') and not _moves_are_available(board, 'W'):
        raise OthelloGameOverError()


def count_pieces(board: [list], turn: str) -> int:
    '''Returns total number of a given player's pieces'''
    count = 0
    for column in board:
        for cell in column:
            if cell == turn:
                count += 1
    return count

def construct_board(number_of_columns: int, number_of_rows: int) -> [list]:
    '''Given a number of columns and rows, returns a list of lists
       representing the game board
    '''
    board = []
    for i in range(number_of_columns):
        board.append([' ']*number_of_rows)
    return board

def construct_board_with_pieces(board: [list], piece: str) -> [list]:
    '''Returns a list of lists with the starting pieces included'''
    if piece == 'black':
        board[(len(board)//2) - 1][(len(board[0])//2) - 1] = 'B'
        board[len(board)//2][len(board[0])//2] = 'B'
        board[(len(board)//2) - 1][len(board[0])//2] = 'W'
        board[len(board)//2][(len(board[0])//2) - 1] = 'W'
        
    elif piece == 'white':
        board[(len(board)//2) - 1][(len(board[0])//2) - 1] = 'W'
        board[len(board)//2][len(board)//2] = 'W'
        board[(len(board)//2) - 1][len(board[0])//2] = 'B'
        board[len(board)//2][(len(board[0])//2) - 1] = 'B'
                            
    return board

############################
## EXCEPTION CLASSES
############################


class InvalidOthelloMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass


class OthelloGameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over
    '''
    pass
