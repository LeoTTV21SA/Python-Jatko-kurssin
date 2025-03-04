import threading
import concurrent.futures as cf
import time


def external_function():
    #Implement
    pass

def external_count():
    #Implement
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
    for i in range(50):
        idx, val=f(i)
        f_values[idx]=val
    #END
    
    return f_values


#Test software under this if        
if __name__ == "__main__":
    ret=init_values(computing5s)
    print(ret)
