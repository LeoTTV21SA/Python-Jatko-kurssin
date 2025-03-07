"""
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
    """
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
    """Inicia N hilos ejecutando la función f con índices de 0 a N-1"""
    th_list = []
    # Crear y empezar cada hilo
    for i in range(N):
        t = threading.Thread(target=f, args=(i,))
        th_list.append(t)
        t.start()  # Iniciar el hilo inmediatamente
    return th_list

def wait_threads(th_list):
    """Espera a que todos los hilos en th_list terminen"""
    for t in th_list:
        t.join()  # Esperar a que cada hilo complete

# Test software under this if
if __name__ == "__main__":
    N = 10
    th_list = start_threads(heavy_computing, N)
    wait_threads(th_list)

