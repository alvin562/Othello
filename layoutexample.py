# layout_example.py
#
# ICS 32 Spring 2014
# Code Example
#
# This is an example that demonstrates how to use Tkinter's grid layout
# manager to control the positioning of widgets in a window.  Also included
# is the use of a nested layout with a Frame widget.
#
# The overall design of our application mirrors the design of a few recent
# code examples, in which there is an application class -- this time called
# SimpleLayoutApplication -- that represents an instance of our application.
#
# As an exercise to help you to understand how the grid layout works, try
# this: adjust one or more of the values (sticky, padding, row or column
# weight, etc.), make a guess about how you think the layout will change,
# then run the program to see if your guess was right.  If it wasn't,
# make sure you understand why.

import tkinter


# This is a font that we'll use on all of the buttons, so we'll define it
# as a global constant.
DEFAULT_FONT = ('Helvetica', 20)


class SimpleLayoutApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()


        self._button1 = tkinter.Button(
            master = self._root_window, text = 'Button 1', font = DEFAULT_FONT)

        self._button1.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._button2 = tkinter.Button(
            master = self._root_window, text = 'Button 2', font = DEFAULT_FONT)

        self._button2.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)


        self._canvas = tkinter.Canvas(
            master = self._root_window, background = '#600000')

        self._canvas.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        # A Frame widget is one whose job is to contain other widgets.
        # It can have its own layout, separate from the one that places
        # it into its own master.  In this case, we use a Frame so that
        # we can separately align a column of buttons along the right-hand
        # edge of the window, regardless of the layout of the widgets
        # to their left.
        self._button_frame = tkinter.Frame(
            master = self._root_window, background = '#006000')

        self._button_frame.grid(
            row = 0, column = 2, rowspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)

        for button_number in range(1, 6):
            numbered_button = tkinter.Button(
                master = self._button_frame, text = '{}'.format(button_number),
                font = DEFAULT_FONT)

            numbered_button.grid(
                row = button_number - 1, column = 0, padx = 0, pady = 0)


        # This is how you set weights on rows and columns, which controls
        # how the sizes of grid cells change as the size of the window
        # changes -- and, correspondingly, how the size and positioning of
        # the widgets in those grid cells change.
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 3)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 0)


    def start(self):
        self._root_window.mainloop()



if __name__ == '__main__':
    SimpleLayoutApplication().start()
