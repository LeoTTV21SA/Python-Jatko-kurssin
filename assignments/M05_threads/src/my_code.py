
import threading
import time

# heavy_computing for test purposes!
# You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')

def start_threads(f, N):
    """Aloita N säiettä suorittamassa funktiota f indekseillä 0 - N-1"""
    th_list = []
    # Luo ja aloita jokainen lanka
    for i in range(N):
        t = threading.Thread(target=f, args=(i,))
        th_list.append(t)
        t.start()  # Aloita lanka välittömästi
    return th_list

def wait_threads(th_list):
    """Odota, että kaikki th_list:n viestiketjut päättyvät"""
    for t in th_list:
        t.join()  # Odota, että jokainen säiettä on valmis

# Test software under this if
if __name__ == "__main__":
    N = 10
    th_list = start_threads(heavy_computing, N)
    wait_threads(th_list)

