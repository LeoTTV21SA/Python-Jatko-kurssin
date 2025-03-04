import threading
import time

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')

def start_threads(f, N):
    pass

def wait_threads(th_list):
    pass

#Test software under this if
if __name__ == "__main__":
    th_list=start_threads(heavy_computing, N)
    wait_threads(th_list)

