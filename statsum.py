import numpy as np
import RecordSpectra
from constants import *
N=361
RecordSpectra.RecordSpec(N)
file = open(r"C:\Users\USER\Desktop\Xe-O2 Level\Spectrum(theta)1.txt", 'r')
lines = file.readlines()
Stat = 0
T=300*0.695 #в см-1
for line in lines:
    fline = line.strip().split()
    spct = np.array([float(i) for i in fline])
    Stat += np.sum(np.exp(- spct / T))
file.close()
print(Stat * np.exp(-144 / T) / N * 71746)