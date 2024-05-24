import tkinter as tk # tk is our nickname


button_count = 0 # stores how many times the button has been pressed

def on_click(event):
    global button_count # allows to modify button_count inside our function

    button_count = button_count + 1 # add one to button count

    if button_count == 1:
        bob_the_button.configure(text = "Naughty! You did not obey!!")

    elif button_count == 2:
         bob_the_button.configure(text = "Seriously dude! I said do not click")

    elif button_count == 3:
        bob_the_button.configure(text="Aah! Next time, no more button")

    elif button_count == 4:
        bob_the_button.configure(text="If you press me again, I WILL disappear")

    else:
        bob_the_button.configure(text="")


window = tk.Tk() # the window we will use to add our graphics
window.title('The Mysterious Void')

# Create a canvas
my_canvas = tk.Canvas(window, width = 200, height = 200, bg = 'red')
my_canvas.pack()

background_image = tk.PhotoImage(file='weather.png')
background_label = tk.Label(window, image=background_image ) # places the background image on the window
background_label.place(relwidth=1, relheight=1) # make the label the same size as the window

entry = tk.Entry(window, font = 30)
entry.pack()

# Create a button
bob_the_button = tk.Button(window, text = "Do not press this button!") # attach the button to the window
bob_the_button.pack(padx = 10, pady = 10) # add some padding around the button


bob_the_button.bind("<ButtonRelease-1>", on_click)


window.mainloop() # makes everything work!
