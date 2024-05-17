import tkinter as tk # tk is our nickname

button_count = 0 # stores how many times the button has been pressed

def on_click(event):
    global button_count # allows to modify button_count inside our function

    button_count = button_count + 1 # add one to button count


window = tk.Tk() # the window we will use to add our graphics
window.title('The Mysterious Void')

# Create a canvas
my_canvas = tk.Canvas(width = 200, height = 200, bg = '#f09618')
my_canvas.pack()

# Create a button
bob_the_button = tk.Button(window, text = "Do not press this button!") # attach the button to the window
bob_the_button.pack(padx = 10, pady = 10) #


window.mainloop() # makes everything work!