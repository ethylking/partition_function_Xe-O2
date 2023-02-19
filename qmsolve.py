import qmsolve
import numpy as np
import time
from numba import vectorize
import numbers
@vectorize(["float32(float32, float32)"], target='parallel')
def VectorAdd(a,b):
    return a+b

def main():
    N=320000000*2

    A=np.ones(N,dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    t1=time.perf_counter()
    C=VectorAdd(A,B)
    t2=time.perf_counter()
    print("C[:5] = "+str(C[:5]))
    print("C[:-5] = " + str(C[:-5]))
    print("Time ", t2-t1)

if __name__ == '__main__':
    main()