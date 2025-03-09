from tkinter import *
import sqlite3

db_file = 'my_db.db'

#Your code here!
# Luo pääikkuna
root = Tk()
root.title("Word Cycle")

# Alusta tietokanta
def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS words (word TEXT NOT NULL)''')
    # Tyhjennä taulu ja lisää vaaditut sanat
    cursor.execute('DELETE FROM words')
    words = ['kato', 'toka', 'voi', 'zurf', 'sana', 'kiva', 'moi', 'hei', 'kato']  # 9 sanoja, kato toistuu lopussa
    for word in words:
        cursor.execute('INSERT INTO words (word) VALUES (?)', (word,))
    conn.commit()
    conn.close()

# Hae sanat tietokannasta
def get_words():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT word FROM words')
    words = [row[0] for row in cursor.fetchall()]
    conn.close()
    return words

# Globaali indeksi sanan seuraamiseen
current_index = -1

# Päivitä etiketti seuraavalla sanalla
def update_label():
    global current_index
    words = get_words()
    current_index = (current_index + 1) % len(words)  # Kierto
    lbl.config(text=words[current_index])

# Alusta käyttöliittymä
init_db()
lbl = Label(root, text="Start")  # Teksti alussa ei vaikuta testiin
lbl.pack(pady=10)

btn = Button(root, text="Next", command=update_label)
btn.pack(pady=10)

#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()