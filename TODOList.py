import tkinter as tk
window = tk.Tk()
window.title("GUI")
# creating a function called say_hi()
def say_hi():
 tk. Label (window, text = "Hi").pack()
tk.Button(window, text = "Click Me!", command = say_hi).pack()
window.mainloop() 