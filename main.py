"""
Create window frames

Create buttons of clickable squares, make those separate class
so we can give it attributes and actions

"""

from tkinter import *
import settings
import utils
from cell import Cell

root = Tk() # Name of our main overall window

# Override the settings of the window
root.configure(bg="black")
# Size of window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")

# Sets it so window is not resizable
root.resizable(False, False)


top_frame = Frame(
    root,
    bg ="black", #change later to black
    width=1440,
    height=utils.height_prct(25)
)
# Uses x & Y axis, Top left is 0,0. Down is +720. Right is +1440
top_frame.place(x = 0, y = 0) # starts at 0,0

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper Game",
    font=(", 48")
)
game_title.place(
    x=utils.width_prct(25), y=0
)

left_frame = Frame(
    root,
    bg = "black", # change to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

# game frame
center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height= utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

# use .grid() method instead of place() to neatly pack cells together
# in 1 frame. takes location as column and row instead of x and y
# now use nest for loop to create grid of button cells


"""
Per GPT " You created X amount of Cell objects assigned variable c.
However, the variable "c" will only refer to the last object 
that was created, because on each iteration of the loops, the value of c 
is overwritten with a reference to a new Cell object.
It is important to note that this code does not give each of the Cell 
objects a unique name. Instead, they are all referred to by the same 
variable name, c. This can make it difficult to keep track of the objects
and manipulate them individually. It is generally a good idea to give 
each object a unique name or identifier, so that you can easily
distinguish between them and manipulate them individually if necessary.
"""

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            row=y, column=x

        )
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
    )

Cell.randomize_mines()


"""
c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.grid(
    column=0, row=0
)
"""

# Run the Window
root.mainloop()
