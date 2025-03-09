"""
Example 1

% python3 my_code.py 
Enter mainloop()
>m
"Hello World!" have been printed 1 times!
>m
"Hello World!" have been printed 2 times!
>q
"q" not found from events list!
>x
Exit mainloop()

-----------------------------------------------------------------
Example 2

% python3 my_code.py
Enter mainloop()
>m
"Hello World!" have been printed 1 times!
>r
Number of empty rows:3



>m
"Hello World!" have been printed 2 times!
>r
Number of empty rows:1

>x
Exit mainloop()
"""


######################################
#
# Don't touch the main loop and related variables
events = {}
active_mainloop = True

def mainloop():
    init_mainloop()
    
    print('Enter mainloop()')
    while active_mainloop:
        k = input('>')
        if k != '':
            if k in events:
                f = events[k]
                f()
            else:
                print(f'"{k}" not found from events list!')
    print('Exit mainloop()')
######################################

# Event handling function
def event_exit():
    global active_mainloop
    active_mainloop = False

# Implement functions, variables etc to handle events here.
# Laskuri "Hello World!" -tulostuksille
hello_count = 0

def event_hello():
    global hello_count
    hello_count += 1
    print(f'"Hello World!" have been printed {hello_count} times!')

def event_rows():
    # Lue seuraava syöte ja tulosta tyhjiä rivejä
    try:
        n = int(input('***'))
        print(f'Number of empty rows:{n}' + '\n' * n)
    except ValueError:
        print('Invalid number!')

def init_mainloop():
    global events
    events = {}
    events['x'] = event_exit
    # Lisää tapahtumakäsittelijät events-sanakirjaan
    events['m'] = event_hello
    events['r'] = event_rows

######################################
#
# Don't modify lines below
if __name__ == "__main__":
    mainloop()
