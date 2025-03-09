from tkinter import *

#Your code here!
# Luo pääikkuna
root = Tk()
root.title("Button Test")

# Määritä globaalit widgetit
lbl = Label(root, text="Button not pressed!")
lbl.pack(pady=10)

# Funktio, joka muuttaa etiketin tekstin
def button_click():
    lbl.config(text="Button pressed!")

btn = Button(root, text="Click Me", command=button_click)
btn.pack(pady=10)

#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()