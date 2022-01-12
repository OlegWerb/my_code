import tkinter as tk
import random
import time


a = 0
b = 0

window = tk.Tk()
#Tentry = tk.Entry()
window.geometry("300x300")



start_time = time.time()
end_time = time.time()
spend_time = time.time() - start_time

def send_message():
    var = spend_time
    print(var)
    result_1.config(
        text=var
    )

label = tk.Label(
    text="Timer Calculator",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=100,
    height=4
)

label2 = tk.Label(
    text="If the title is red, click the button",
    foreground="black",  # Set the text color to white
    background="white",  # Set the background color to black
    width=100,
    height=2
)

frame = tk.Frame(
    height=10
)


button = tk.Button(
    text="Click me!",
    bg="white",
    fg="red",
    font= "bold",
    width=15,
    height=1,
    command=send_message
)

result_1 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 25)
)
result = tk.Label(

    foreground="red",  # Set the text color to white
    font=("Arial", 25)
)


def lab_col():
    colors = ['yellow', 'red', 'green']
    value = random.randint(0, len(colors) - 1)
    label.config(background=colors[value])
    global start_time
    colors[1]
    global end_time
    spend_time = time.time() - start_time
    result.config(
        text=spend_time
    )

    window.after(2000, lab_col)

window.after(2000, lab_col)



for c in window.children:
    print(c)
    window.children[c].pack()

window.mainloop()