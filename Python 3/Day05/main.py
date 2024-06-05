import tkinter as tk


def increase():
    global number
    number = number + 1
    label.config(text=str(number))
    # label.configure(text=str(number))


def decrease():
    global number
    number = number - 1
    label.config(text=str(number))
    # label.configure(text=str(number))


root = tk.Tk()
root.geometry("300x300")
root.title("My App")

number = 0

label = tk.Label(root, text=str(number), font=("Helvetica", 20))
label.place(relx=0.5, rely=0.5, anchor="center")

button1 = tk.Button(root, text="+1", font=("Helvetica", 20), command=increase)
button1.place(relx=0.5, rely=0.8, anchor="center")

button2 = tk.Button(root, text="-1", font=("Helvetica", 20), command=decrease)
button2.place(relx=0.5, rely=0.2, anchor="center")

root.mainloop()
