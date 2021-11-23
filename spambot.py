import time
from tkinter import font
import pyautogui
import tkinter as tk

root = tk.Tk()
root.configure(background='pink')
root.resizable(False, False)

whattospam_label = tk.Label(root, text= 'What to spam?', font=('Calibri', 16), bg= 'pink')
whattospam_label.grid(column=0, row=0, padx= 15, sticky=tk.W, pady=5)

whattospam = tk.Entry(root, width= 25)
whattospam.grid(column=0, row=1, padx= 15, pady= 12, sticky=tk.W)

howmuch_label = tk.Label(root, text= 'How much to spam?', font=('Calibri', 16), bg= 'pink')
howmuch_label.grid(column=0, row=3, padx= 15, sticky=tk.W, pady= 5)

howmuch = tk.Entry(root, width= 25)
howmuch.grid(column=0, row=4, padx= 15, pady= 5, sticky=tk.W)

def spam():  
    root.update()
    time.sleep(3)
    for i in range (int(howmuch.get())):
        pyautogui.typewrite(str(whattospam.get()))
        root.update()
        time.sleep(0.5)
        pyautogui.press('Enter')

button_main = tk.Button(root, text='Spam It!', font=('Calibri', 16), command=spam)
button_main.grid(column=4, row= 4, padx= 2, sticky=tk.N)

window_width = 375
window_height = 210
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x_cordinate = int((screenwidth/2) - (window_width/2))
y_cordinate = int((screenheight/2.5) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

root.title('Spambot')
root.mainloop()
