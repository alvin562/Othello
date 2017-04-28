## Alvin Dantic 20927908.  Project 4.  Lab 5


import othello
import tkinter


class OthelloApplication:
    def __init__(self, gamestate: othello.GameState, means: str) -> None:
        '''Initializes Othello Application'''
        self._game_state = gamestate

        self._means = means.lower().strip()
        
        self._root_window = tkinter.Tk()
        
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 600, height = 600,
            background = '#006000')

        self._canvas2 = tkinter.Canvas(master = self._root_window,
                                       width = 75, height = 75,
                                       background = '#006000')
        
        self._canvas.grid(row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas2.grid(row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._place_piece)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)

        self._display_turn()
        self._display_score()

        
    def start(self) -> None:
        '''Starts the Othello Application'''
        self._root_window.mainloop()
        

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Redraws lines and pieces whenever the canvas is resized'''
        self._redraw_all_lines()
        self._redraw_all_pieces()

    
    def _redraw_all_lines(self) -> None:
        '''Redraws lines to fit canvas'''
        self._canvas.delete(tkinter.ALL)

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        for i in range(self._game_state.columns()):
            x_coord = int((canvas_width/self._game_state.columns())*(1 + i))
            self._canvas.create_line(x_coord, 0, x_coord, canvas_height)

        for j in range(self._game_state.rows()):
            y_coord = int((canvas_height/self._game_state.rows())*(1 + j))
            self._canvas.create_line(0, y_coord, canvas_width, y_coord)


    def _col_index(self, event: tkinter.Event):
        '''Returns corresponding column index when given a click Event'''
        canvas_width = self._canvas.winfo_width()
        x_coord = 0
        
        for i in range(self._game_state.columns()):
            if x_coord < event.x < int((canvas_width/self._game_state.columns())*(1 + i)):
                return i
            else:
                x_coord = int((canvas_width/self._game_state.columns())*(1 + i))


    def _row_index(self, event: tkinter.Event):
        '''Returns corresponding row index when given a click Event'''
        canvas_height = self._canvas.winfo_height()
        y_coord = 0

        for i in range(self._game_state.rows()):
            if y_coord < event.y < int((canvas_height/self._game_state.rows())*(1 + i)):
                return i
            else:
                y_coord = int((canvas_height/self._game_state.rows())*(1 + i))


    def _redraw_all_pieces(self):
        '''Redraws pieces to fit canvas'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        for i in range(len(self._game_state.board())):
            for j in range(len(self._game_state.board()[0])):
                x1 = (i*int((canvas_width/self._game_state.columns()))) + 15
                y1 = (j*int((canvas_height/self._game_state.rows()))) + 15
                x2 = ((i + 1)*int((canvas_width/self._game_state.columns()))) - 5
                y2 = ((j + 1)*int((canvas_height/self._game_state.rows()))) - 5
                
                if self._game_state.board()[i][j] == 'W':
                    self._canvas.create_oval(x1, y1, x2, y2, fill = 'white')

                elif self._game_state.board()[i][j] == 'B':
                    self._canvas.create_oval(x1, y1, x2, y2, fill = 'black')


    def _display_turn(self):
        '''Creates and displays labels of whose turn it is'''
        if self._game_state.turn() == 'B':
            self.blacks_turn = tkinter.Label(master = self._root_window,
                    text = "Black's Turn", font = ('Helvetica', 30, 'bold'),
                     background = '#006000', foreground = 'black')
            
            self.blacks_turn.grid(row = 0, column = 0)

        elif self._game_state.turn() == 'W':
            self.whites_turn = tkinter.Label(master = self._root_window,
                    text = "White's Turn", font = ('Helvetica', 30, 'bold'),
                     background = '#006000', foreground = 'white')
            
            self.whites_turn.grid(row = 0, column = 0)


    def _display_score(self):
        '''Creates and displays labels of the scores''' 
        self.white_score = tkinter.Label(master = self._root_window,
            text = othello.count_pieces(self._game_state.board(), 'W'),
            font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'white')

        self.black_score = tkinter.Label(master = self._root_window,
            text = othello.count_pieces(self._game_state.board(), 'B'),
            font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'black')

        self.white_score.grid(row = 0, column = 0, padx = 50, sticky = tkinter.W)
        self.black_score.grid(row = 0, column = 0, padx = 50, sticky = tkinter.E)


    def _display_winner(self):
        '''Creates and displays labels of the winner'''
        if self._game_state.winner() == 'B' and self._means == 'm':
            winner_label = tkinter.Label(master = self._root_window,
                text = 'Black Wins!', font = ('Helvetica', 30, 'bold'), background = '#006000')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == 'W' and self._means == 'm':
            winner_label = tkinter.Label(master = self._root_window,
                text = 'White Wins!', font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'white')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == 'TIE':
            winner_label = tkinter.Label(master = self._root_window,
                text = 'Tie Game No Winner', font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'gray')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == 'W' and self._means == 'l':
            winner_label = tkinter.Label(master = self._root_window,
                text = 'Black Wins!', font = ('Helvetica', 30, 'bold'), background = '#006000')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == 'B' and self._means == 'l':
            winner_label = tkinter.Label(master = self._root_window,
                text = 'White Wins!', font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'white')

            winner_label.grid(row = 0, column = 0)
            

    def _place_piece(self, event: tkinter.Event):
        '''Creates and displays oval whenever the user clicks on a valid
        cell;  also displays score, turn, winner, and flips pieces whenever
        a valid move is made'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        try:
            x1 = (self._col_index(event)*int((canvas_width/self._game_state.columns()))) + 15
            y1 = (self._row_index(event)*int((canvas_height/self._game_state.rows()))) + 15
            x2 = ((self._col_index(event) + 1)*int((canvas_width/self._game_state.columns()))) - 5
            y2 = ((self._row_index(event) + 1)*int((canvas_height/self._game_state.rows()))) - 5

            if self._game_state.turn() == 'B':
                self._game_state.make_move(self._col_index(event), self._row_index(event))
                self.white_score.destroy()
                self.black_score.destroy()
                self._canvas.create_oval(x1, y1, x2, y2, fill = 'black')
                
            elif self._game_state.turn() == 'W':
                self._game_state.make_move(self._col_index(event), self._row_index(event))
                self.white_score.destroy()
                self.black_score.destroy()
                self._canvas.create_oval(x1, y1, x2, y2, fill = 'white')

            self._display_score()
            self._display_turn()
            self._display_winner()
            self._redraw_all_pieces()

        except:
             pass


class GreetingApplication:
    def __init__(self):
        '''Initializes Greeting Application'''
        self._root_window = tkinter.Tk()

        self._label1 = tkinter.Label(self._root_window, text = 'Number of Columns')
        self._label1.grid(row = 0, column = 0)

        self._label2 = tkinter.Label(self._root_window, text = 'Number of Rows')
        self._label2.grid(row = 1, column = 0)

        self._label3 = tkinter.Label(self._root_window, text = 'Enter who goes first (black or white)')
        self._label3.grid(row=2, column = 0)

        self._label4 = tkinter.Label(self._root_window, text = 'Enter top left piece (black or white)')
        self._label4.grid(row = 3, column = 0)

        self._label5 = tkinter.Label(self._root_window, text = "Enter 'M' if more pieces wins or 'L' if less wins")
        self._label5.grid(row = 4, column = 0)
        
        self._entry2 = tkinter.Entry(self._root_window)
        self._entry2.grid(row = 1, column = 1)
        
        self._entry1 = tkinter.Entry(self._root_window)
        self._entry1.grid(row = 0, column = 1)

        self._button1 = tkinter.Button(self._root_window, text = 'Enter')
        self._button1.grid(row=6, column = 0, columnspan = 1)
        self._button1.bind('<Button-1>', self._on_button1_clicked)

        self._button2 = tkinter.Button(self._root_window, text = 'Cancel')
        self._button2.grid(row=6, column=0, columnspan = 2)
        self._button2.bind('<Button-1>', self._on_button2_clicked)

        self._entry3 = tkinter.Entry(self._root_window)
        self._entry3.grid(row = 2, column = 1)

        self._entry4 = tkinter.Entry(self._root_window)
        self._entry4.grid(row = 3, column = 1)

        self._entry5 = tkinter.Entry(self._root_window)
        self._entry5.grid(row = 4, column = 1)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.rowconfigure(5, weight = 1)
        self._root_window.rowconfigure(6, weight = 1)
        

    def start(self):
        '''Starts the Greeting Application'''
        self._root_window.mainloop()

        
    def _on_button2_clicked(self, event: tkinter.Event):
        '''Closes window when 'cancel' button is clicked'''
        self._root_window.destroy()


    def _on_button1_clicked(self, event: tkinter.Event):
        '''Starts othello application when 'start button' is clicked; displays
           error window when use inputs invalid input'''
        self.col = self._entry1.get()
        self.row = self._entry2.get()
        self.top_left = self._entry4.get().strip().lower()
        self.first_player = self._entry3.get().strip().lower()
        means = self._entry5.get().strip().lower()

        if self.col.strip().isdigit() and 4 <= int(self.col) <= 16 and int(self.col) % 2 == 0 and self.row.strip().isdigit() \
           and 4 <= int(self.row) <= 16 and int(self.row) % 2 == 0 and self.top_left == 'white' and (means == 'm' or means == 'l'):
 
            board = othello.construct_board_with_pieces(othello.construct_board(int(self.col), int(self.row)), 'white')
            app = OthelloApplication(self._construct_gamestate(board, self.first_player), means)
            self._root_window.destroy()
            
            
        elif self.col.strip().isdigit() and 4 <= int(self.col) <= 16 and int(self.col) % 2 == 0 and self.row.strip().isdigit() and 4 <= int(self.row) <= 16 \
             and int(self.row) % 2 == 0 and self.top_left == 'black' and (means == 'm' or means == 'l'):
            board = othello.construct_board_with_pieces(othello.construct_board(int(self.col), int(self.row)), 'black')
            
            app = OthelloApplication(self._construct_gamestate(board, self.first_player), means)
            self._root_window.destroy()

        else:
            second_window = tkinter.Tk()
            error_message = tkinter.Label(second_window, text = 'Invalid Entry; Please Try Again')
            error_message.pack()
            


    def _construct_gamestate(self, board: [[]], first_player):
        '''Takes a board and the player who goes first and creates a GameState object'''
        if first_player == 'white':
            return othello.GameState(board, 'W')
        elif first_player == 'black':
            return othello.GameState(board, 'B')


if __name__ == '__main__':
    Othello = GreetingApplication()
    Othello.start()



