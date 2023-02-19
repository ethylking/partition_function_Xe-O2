from potential import *
import os
import time
import subprocess

def RecordSpec(N):
    Theta = np.linspace(-1, 1, N) #cos(theta)
    os.chdir(r'C:\Users\USER\Desktop\Xe-O2 Level')
    spec=open(r"C:\Users\USER\Desktop\Xe-O2 Level\Spectrum(theta)1.txt",'w')
    for theta in Theta:
        print(theta)
        PES(10**4, r=-1, th = theta )
        file = open(r"C:\Users\USER\Desktop\Xe-O2 Level\Level.input.txt",'r')
        f=file.readlines() # заменить нужно с 9 строки по 10008 включительно для N=10**4
        file.close()
        surf = open(r"C:\Users\USER\Desktop\Xe-O2 Level\Potential.txt",'r')
        s = surf.readlines()
        surf.close()
        f[9:10009] = s[::]
        file = open(r"C:\Users\USER\Desktop\Xe-O2 Level\Level.input.txt",'w')
        file.writelines(f)
        file.close()
        # os.startfile(r'C:\Users\USER\Desktop\Xe-O2 Level\Level.bat')
        os.system(r'start Level.bat')
        time.sleep(3)
        file=open(r"C:\Users\USER\Desktop\Xe-O2 Level\fort.7",'r')
        f=file.readlines() #спектр находится с 3-ей позиции до конца
        file.close()
        for i in f[3:]:
            spec.writelines(i.strip().split()[2]+' ')
        spec.write('\n')

    spec.close()
