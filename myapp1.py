# 0: Plan out the layout of the app
# 1: Create the window for the app
#    -Add title and geometry
# 2: Declare size Place labels, buttons, entry fields, etc. on the window
#    -Use grids to place them
# 3: Place labels, buttons, entry fields, etc. on the window
# 4: Connect buttons/entries to one another through functions
# 5: Use .mainloop() to run window

import tkinter as tk

window = tk.Tk()

window.title("My APP")

window.geometry("400x400")

# LABEL
title = tk.Label(text="Hello world. Welcome to CS50 and my app", font=("Times New Roman", 20))
title.grid(column=0, row=0)

# Button
button1 = tk.Button(text="Click me!", font=("Times New Roman", 20), bg="red")
button1.grid(column=0, row=1)

# Entry field
entry_field = tk.Entry()
entry_field.grid(column=0, row=2)

window.mainloop()