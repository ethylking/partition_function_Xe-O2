from functions import *
import time
import os

N=3*10**5
n=20 #threads number
if __name__ == '__main__':
    T = 300 * 1.380649 * 10 ** (-16)
    pool=multiprocessing.Pool()
    # os.system('cls')
    S=0
    sigma = []
    for i in tqdm(range(int(N/n))):
        result=pool.map(Zint,[8 for i in range(n)])
        # os.system('cls')
        for i in range(n):
            S=S+result[i][0]*result[i][1]   #шаг к статсумме
            sigma+=[result[i][0]*result[i][1]]
    S=S/N
    sterr=0
    for i in range(N):
        if i % 100 == 0:
            print(i)
        sterr+=(sigma[i]-S)**2
    sterr=sterr/(N*(N-1))
    S=S/(2*pi*h)**5*(1.6*10**(-31))**(5/2)
    sterr=sterr**0.5/(2*pi*h)**5*(1.6*10**(-31))**(5/2)
    print(S,sterr)


