import sqlite3

db_file = 'my_db.db'

#Write your code here
def init_and_print_names():
    # Yhdistä tietokantaan (luo se, jos ei ole olemassa)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Luo texttable-taulu, jos sitä ei ole
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS texttable (
            name TEXT NOT NULL
        )
    ''')
    
    # Lisää vaaditut nimet tauluun
    names = ['Matti', 'Ville', 'Kaisa', 'Mikko', 'Urpo', 'Kati', 'Joonas', 'Miisa']
    for name in names:
        cursor.execute('INSERT INTO texttable (name) VALUES (?)', (name,))
    
    # Hae ja tulosta nimet
    cursor.execute('SELECT name FROM texttable')
    for row in cursor.fetchall():
        print(row[0])
    
    # Tallenna muutokset ja sulje yhteys
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_and_print_names()