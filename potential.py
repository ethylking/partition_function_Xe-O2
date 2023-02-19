from functions import *


def PES(N,r=-1, th=-1):
    Pot = []
    file = open(r'C:\Users\USER\Desktop\Xe-O2 Level\Potential.txt', 'w')
    if r==-1:
        R=np.linspace(3.43523,8,N)
        for rad in R:
            # print(rad)
            if rad / rm <= x1:
                V = V10
            elif rad / rm > x2:
                V = V30
            else:
                V = V20
            file.write(f'{rad}\t{V(rad,th)*8.06554}\n')
            # Pot+=[V(rad,pi/2)*8.06554]
    else:
        Th=np.linspace(0,pi,N)
        for i in range(N):
            if r/rm <= x1:
                file.write(f'{Th[i]}\t{V10(r,Th[i])*8.06554}\n')
            elif r/rm <= x2:
                print(1)
                file.write(f'{Th[i]}\t{V20(r, Th[i]) * 8.06554}\n')
            else:
                file.write(f'{Th[i]}\t{V30(r,Th[i])*8.06554}\n')
    file.close()

            # Pot+=[V10(r,Th[i])*8.06554]#в см-1
    return Pot





