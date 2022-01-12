import tkinter as tk
import random
import time

window = tk.Tk()
#Tentry = tk.Entry()
window.geometry("300x300")

label = tk.Label(
    text="Timer Calculator",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=100,
    height=2
)
entry = tk.Entry()

frame = tk.Frame(
    height=10
)


def stop():
    start_time = time.time()
    end_time = time.time()
    spend_time = time.time() - start_time

    result_1.config(
        text=spend_time
    )

 # def send_message():
 #     if lab_col.colors[6]:


#     var = entry.get()
#     print(var)
#     result_1.config(
#         text=var
#     )

# def timer_update():
#     #value = random.randint(1, 9), random.randint(1, 9)
#     stat = time.time()
#     end = time.time()
#     run_time = end - stat
#     value1 = time.run_time
#     #result_1.config(text=run_time)
#     window.after(2000, timer_update)

#
# button = tk.Button(
#     text="Click me!",
#     bg="blue",
#     fg="yellow",
#     width=10,
#     height=1,
#     command=timer_update
# )
#
# result = tk.Label(
#     text="0.0",
#     foreground="red",  # Set the text color to white
#     font=("Arial", 25)
# )

frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 25)
)

# stat = time.time()
# end = time.time()
# run_time = end - stat

for c in window.children:
    print(c)
    window.children[c].pack()

#
# def timer_update():
#     #value = random.randint(1, 9), random.randint(1, 9)
#     stat = time.time()
#     end = time.time()
#     run_time = end - stat
#     result_1.config(text=run_time)
#     window.after(2000, timer_update)
#
#
# def lab_col():
#     colors = ['lightyellow', 'lightgray', 'gray', 'pink', 'violet', 'brown', 'red', 'orange', 'yellow', 'green', 'cyan',
#               'blue', 'magenta', 'black', 'gray', 'lightgreen']
#     value = random.randint(0, len(colors) - 1)
#     label.config(background=colors[value])
#
#     window.after(2000, lab_col)
#
#
# window.after(2000, lab_col)
# window.after(2000, timer_update)

window.mainloop()
