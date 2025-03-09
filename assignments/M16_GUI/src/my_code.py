from tkinter import *
import math

#Your code here!
# Luo pääikkuna
root = Tk()
root.title("Quadratic Roots Calculator")

# Luo syötekentät
Label(root, text="a:").pack()
entry_a = Entry(root)
entry_a.pack()

Label(root, text="b:").pack()
entry_b = Entry(root)
entry_b.pack()

Label(root, text="c:").pack()
entry_c = Entry(root)
entry_c.pack()

# Funktio juurien laskemiseen
def calculate_roots():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # Laske diskriminantti
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            # Ei reaalisia juuria
            label_root1.config(text="-")
            label_root2.config(text="-")
        else:
            # Laske juuret
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            # Näytä juuret kahden desimaalin tarkkuudella
            label_root1.config(text=f"{root1:.2f}")
            label_root2.config(text=f"{root2:.2f}")
    except (ValueError, ZeroDivisionError):
        # Virhe syötteissä tai a=0
        label_root1.config(text="-")
        label_root2.config(text="-")

# Luo painike ja tulosetikettit
btn = Button(root, text="Calculate", command=calculate_roots)
btn.pack(pady=10)

Label(root, text="Root 1:").pack()
label_root1 = Label(root, text="")
label_root1.pack()

Label(root, text="Root 2:").pack()
label_root2 = Label(root, text="")
label_root2.pack()

#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()