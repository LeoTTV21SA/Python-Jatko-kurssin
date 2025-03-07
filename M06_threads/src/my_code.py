""""
import threading
import concurrent.futures as cf
import time

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')
        return idx, idx*idx

def start_threads(f, N):
    pass

def wait_threads(th_list):
    pass

#Test software under this if        
if __name__ == "__main__":
    N=10

    print('None started')
    th_list=start_threads(heavy_computing, N)
    print('Wait...')
    ret=wait_threads(th_list)
    print('All futures completed')
    print(ret)
"""
import threading
import concurrent.futures as cf
import time

# heavy_computing for test purposes!
# You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')
        return idx, idx*idx

def start_threads(f, N):
    """Inicia N tareas concurrentes ejecutando f con índices de 0 a N-1"""
    executor = cf.ThreadPoolExecutor(max_workers=N)
    futures = [executor.submit(f, i) for i in range(N)]
   
    return futures

def wait_threads(th_list):
    """Espera a que todas las tareas en th_list terminen y devuelve los resultados"""
    
    results = [future.result() for future in cf.as_completed(th_list)]
    
    sorted_results = sorted(results, key=lambda x: x[0])
   
    return [r[1] for r in sorted_results]

# Test software under this if        
if __name__ == "__main__":
    N = 10

    print('None started')
    th_list = start_threads(heavy_computing, N)
    print('Wait...')
    ret = wait_threads(th_list)
    print('All futures completed')
    print(ret)