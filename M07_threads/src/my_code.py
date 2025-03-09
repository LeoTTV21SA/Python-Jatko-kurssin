import threading
import concurrent.futures as cf
import time

_counter = 0
_counter_lock = threading.Lock()
def external_function():
    #Implement
    global _counter
    with _counter_lock:
        _counter += 1
    pass

def external_count():
    #Implement
    global _counter
    with _counter_lock:
        return _counter
    pass

#Sample function for test purposes
def computing5s(thr_id):
    time.sleep(5)
    external_function()
            
    return thr_id, thr_id*thr_id

def init_values(f):
    f_values={}
    
    #Between BEGIN and END there is too slow solution.
    #Rewrite the solution to utilize parallelism
    #
    #BEGIN
    # Käytä ThreadPoolExecutor rinnakkaisuuden toteuttamiseen
    with cf.ThreadPoolExecutor() as executor:
        # Luo lista tulevista tuloksista kutsumalla f-funktiota rinnakkain
        futures = [executor.submit(f, i) for i in range(50)]
        # Kerää tulokset sitä mukaa kun ne valmistuvat
        for future in cf.as_completed(futures):
            idx, val = future.result()
            f_values[idx] = val
    #END
    
    return f_values


#Test software under this if        
if __name__ == "__main__":
    ret=init_values(computing5s)
    print(ret)
    print('count = ', external_count())