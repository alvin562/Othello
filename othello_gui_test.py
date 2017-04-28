from othello import GameState, WHITE, BLACK, construct_board_with_pieces, construct_board, count_pieces
from tkinter import Tk, Canvas, N, S, E, W, ALL, Event, Label, Button, Entry


class OthelloApplication:
    def __init__(self, gamestate: GameState, means: str) -> None:
        self._game_state = gamestate

        self._means = means.lower().strip()
        
        self._root_window = Tk()
        
        self._canvas = Canvas(self._root_window, width = 600, height = 600,
                              background = '#006000')

        self._canvas2 = Canvas(self._root_window,
                               width = 75, height = 75, background='#006000')
        
        self._canvas.grid(row = 1, column = 0, padx = 10, pady = 10,
                          sticky = N + S + W + E)

        self._canvas2.grid(row = 0, column = 0, padx = 10, pady = 10,
                           sticky = N + S + W + E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._place_piece)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)

        self._display_turn()
        self._display_score()

        
    def start(self) -> None:
        self._root_window.mainloop()
        

    def _on_canvas_resized(self, event: Event) -> None:
        self._redraw_all_lines()
        self._redraw_all_pieces()

    
    def _redraw_all_lines(self) -> None:
        self._canvas.delete(ALL)

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        for i in range(self._game_state.columns()):
            x_coord = int((canvas_width/self._game_state.columns())*(1 + i))
            self._canvas.create_line(x_coord, 0, x_coord, canvas_height)

        for j in range(self._game_state.rows()):
            y_coord = int((canvas_height/self._game_state.rows())*(1 + j))
            self._canvas.create_line(0, y_coord, canvas_width, y_coord)


    def _col_index(self, event: Event):
        canvas_width = self._canvas.winfo_width()
        x_coord = 0
        
        for i in range(self._game_state.columns()):
            if x_coord < event.x < int((canvas_width/self._game_state.columns())*(1 + i)):
                return i
            else:
                x_coord = int((canvas_width/self._game_state.columns())*(1 + i))


    def _row_index(self, event: Event):
        canvas_height = self._canvas.winfo_height()
        y_coord = 0

        for i in range(self._game_state.rows()):
            if y_coord < event.y < int((canvas_height/self._game_state.rows())*(1 + i)):
                return i
            else:
                y_coord = int((canvas_height/self._game_state.rows())*(1 + i))


    def _redraw_all_pieces(self):
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        for i in range(len(self._game_state.board())):
            for j in range(len(self._game_state.board()[0])):
                x1 = (i*int((canvas_width/self._game_state.columns()))) + 15
                y1 = (j*int((canvas_height/self._game_state.rows()))) + 15
                x2 = ((i + 1)*int((canvas_width/self._game_state.columns()))) - 15
                y2 = ((j + 1)*int((canvas_height/self._game_state.rows()))) - 15
                
                if self._game_state.board()[i][j] == WHITE:
                    self._canvas.create_oval(x1, y1, x2, y2, fill = 'white')

                elif self._game_state.board()[i][j] == BLACK:
                    self._canvas.create_oval(x1, y1, x2, y2, fill = 'black')


    def _display_turn(self):
        if self._game_state.turn() == 'B':
            self._blacks_turn = Label(self._root_window, text = "Black's Turn", font = ('Helvetica', 30, 'bold'),
                                      background = '#006000')
            
            self._blacks_turn.grid(row = 0, column = 0)

        elif self._game_state.turn() == 'W':
            self._whites_turn = Label(self._root_window, text = "White's Turn", font = ('Helvetica', 30, 'bold'),
                                      background = '#006000', foreground = 'white')
            
            self._whites_turn.grid(row = 0, column = 0)


    def _display_score(self):
        self._white_score = Label(self._root_window, text = count_pieces(self._game_state.board(), WHITE),
                                  font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'white')

        self._black_score = Label(self._root_window, text = count_pieces(self._game_state.board(), BLACK),
                                  font = ('Helvetica', 30, 'bold'), background = '#006000')

        self._white_score.grid(row = 0, column = 0, padx = 50, sticky = W)
        self._black_score.grid(row = 0, column = 0, padx = 50, sticky = E)


    def _display_winner(self):
        if self._game_state.winner() == BLACK and self._means == 'm':
            winner_label = Label(self._root_window, text = 'Black Wins!',
                                 font = ('Helvetica', 30, 'bold'), background = '#006000')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == WHITE and self._means == 'm':
            winner_label = tkinter.Label(self._root_window, text = 'White Wins!',
                                         font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'white')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == 'TIE':
            winner_label = Label(self._root_window, text = 'Tie Game No Winner',
                                 font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'gray')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == othello.WHITE and self._means == 'l':
            winner_label = Label(self._root_window, text = 'Black Wins!',
                                 font = ('Helvetica', 30, 'bold'), background = '#006000')

            winner_label.grid(row = 0, column = 0)

        elif self._game_state.winner() == othello.BLACK and self._means == 'l':
            winner_label = Label(self._root_window, text = 'White Wins!',
                                 font = ('Helvetica', 30, 'bold'), background = '#006000', foreground = 'white')

            winner_label.grid(row = 0, column = 0)
            

    def _place_piece(self, event: Event):
         canvas_width = self._canvas.winfo_width()
         canvas_height = self._canvas.winfo_height()
         try:
             x1 = (self._col_index(event)*int((canvas_width/self._game_state.columns()))) + 15
             y1 = (self._row_index(event)*int((canvas_height/self._game_state.rows()))) + 15
             x2 = ((self._col_index(event) + 1)*int((canvas_width/self._game_state.columns()))) - 15
             y2 = ((self._row_index(event) + 1)*int((canvas_height/self._game_state.rows()))) - 15

             if self._game_state.turn() == 'B':
                 self._game_state.make_move(self._col_index(event), self._row_index(event))
                 self._white_score.destroy()
                 self._black_score.destroy()
                 self._canvas.create_oval(x1, y1, x2, y2, fill = 'black')
                
             elif self._game_state.turn() == 'W':
                 self._game_state.make_move(self._col_index(event), self._row_index(event))
                 self._white_score.destroy()
                 self._black_score.destroy()
                 self._canvas.create_oval(x1, y1, x2, y2, fill = 'white')

             self._display_score()
             self._display_turn()
             self._display_winner()
             self._redraw_all_pieces()
             
         except:
             pass


class GreetingApplication:
    def __init__(self):
        self._root_window = Tk()

        self._label1 = Label(self._root_window, text = 'Number of Columns')
        self._label1.grid(row = 0, column = 0)

        self._label2 = Label(self._root_window, text = 'Number of Rows')
        self._label2.grid(row = 1, column = 0)

        self._label3 = Label(self._root_window, text = 'Enter who goes first (black or white)')
        self._label3.grid(row = 2, column = 0)

        self._label4 = Label(self._root_window, text = 'Enter top left piece (black or white)')
        self._label4.grid(row = 3, column = 0)

        self._label5 = Label(self._root_window, text = "Enter 'M' if more pieces wins or 'L' if less wins")
        self._label5.grid(row = 4, column = 0)
        
        self._entry2 = Entry(self._root_window)
        self._entry2.grid(row = 1, column = 1)
        
        self._entry1 = Entry(self._root_window)
        self._entry1.grid(row = 0, column = 1)

        self._button1 = Button(self._root_window, text = 'Enter')
        self._button1.grid(row=6, column = 0, columnspan = 1)
        self._button1.bind('<Button-1>', self._on_button1_clicked)

        self._button2 = Button(self._root_window, text = 'Cancel')
        self._button2.grid(row = 6, column = 0, columnspan = 2)
        self._button2.bind('<Button-1>', self._on_button2_clicked)

        self._entry3 = Entry(self._root_window)
        self._entry3.grid(row = 2, column = 1)

        self._entry4 = Entry(self._root_window)
        self._entry4.grid(row = 3, column = 1)

        self._entry5 = Entry(self._root_window)
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
        self._root_window.mainloop()

        
    def _on_button2_clicked(self, event: Event):
        self._root_window.destroy()


    def _on_button1_clicked(self, event: Event):
        self.col = self._entry1.get()
        self.row = self._entry2.get()
        self.top_left = self._entry4.get().strip().lower()
        self.first_player = self._entry3.get().strip().lower()
        means = self._entry5.get().strip().lower()

        if self.col.strip().isdigit() and 4 <= int(self.col) <= 16 and int(self.col) % 2 == 0 and self.row.strip().isdigit() \
           and 4 <= int(self.row) <= 16 and int(self.row) % 2 == 0 and self.top_left == 'white' and (means == 'm' or means == 'l'):
 
            board = construct_board_with_pieces(construct_board(int(self.col), int(self.row)), 'white')
            app = OthelloApplication(self._construct_gamestate(board, self.first_player), means)
            self._root_window.destroy()
            
            
        elif self.col.strip().isdigit() and 4 <= int(self.col) <= 16 and int(self.col) % 2 == 0 and self.row.strip().isdigit() and 4 <= int(self.row) <= 16 \
             and int(self.row) % 2 == 0 and self.top_left == 'black' and (means == 'm' or means == 'l'):
            board = construct_board_with_pieces(construct_board(int(self.col), int(self.row)), 'black')
            
            app = OthelloApplication(self._construct_gamestate(board, self.first_player), means)
            self._root_window.destroy()

    def _construct_gamestate(self, board: [[]], first_player):
        if first_player == 'white':
            return GameState(board, WHITE)
        elif first_player == 'black':
            return GameState(board, BLACK)


if __name__ == '__main__':
    Othello = GreetingApplication()
    Othello.start()



