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
    """Aloita N samanaikaista tehtävää suorittamassa f indekseillä 0 - N-1"""
    executor = cf.ThreadPoolExecutor(max_workers=N)
    futures = [executor.submit(f, i) for i in range(N)]
   
    return futures

def wait_threads(th_list):
    """Odota, että kaikki tehtävät luettelossa th_list valmistuvat ja palauta tulokset"""
    
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