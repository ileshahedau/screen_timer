import tkinter as tk

root = tk.Tk()
root.title("Screen Time Tracker")

total_time = 0

def add_time():
    global total_time
    try:
        time = int(entry.get())
        total_time += time
        label.config(text="Total Time: " + str(total_time) + " mins")
    except:
        label.config(text="Enter valid number")

def check_time():
    if total_time < 60:
        label.config(text="Good 👍")
    else:
        label.config(text="Too much ⚠️")

entry = tk.Entry(root)
entry.pack(pady=10)

btn1 = tk.Button(root, text="Add Time", command=add_time)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Check", command=check_time)
btn2.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=20)

root.mainloop()