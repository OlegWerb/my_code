import tkinter as tk
import random
import time


start_time = 0
colors = ['yellow', 'red', 'green']
wrong = 0



window = tk.Tk()
#Tentry = tk.Entry()
window.geometry("400x400")


def send_message():
    global wrong
    if label["background"] == "red":
        spend_time = round(time.time() - start_time, 3)
        result.config(text=f"Your reaction: {spend_time} s.")
        var = entry.get()
        result_3.config(
            text=f"{var}, {spend_time} s.")

    else:
        wrong_click = "Try again"
        result.config(text=wrong_click)
        wrong = wrong + 1
        label_wrong.config(text=f"Mistake: {wrong}")
        label.config(background="grey")
        window.update()
        time.sleep(1)


# def send_message2():
#     var = entry.get()
#     print(var)
#     result_3.config(
#         text=var
#     )




label = tk.Label(
    text="Timer Calculator",
    foreground="white",
    background="black",
    width=100,
    height=4
)

label3 = tk.Label(
    text="Please write your name and surname",
    foreground="red",
    background="white",
    width=100,
    height=2
)

entry = tk.Entry(
    width=30
)

frame = tk.Frame(
    height=10
)

label2 = tk.Label(
    text="If the title is red, click the button",
    foreground="black",
    background="white",
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

result = tk.Label(

    foreground="green",  # Set the text color to white
    font=("Arial", 25)
)


label_wrong = tk.Label(
    text="Wrong click: 0",
    foreground="red",
    font=("Arial", 25)

                       )

result_1 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 25)
)

result_3 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 25)
)


def timer_update():
    colors = ['yellow', 'red', 'green']
    value = random.randint(0, len(colors) - 1)
    label.config(background=colors[value])
    global start_time
    if label["background"] == "red":
        start_time = time.time()



    window.after(2000, timer_update )

window.after(2000, timer_update )



for c in window.children:
    # print(c)
    window.children[c].pack()


window.mainloop()