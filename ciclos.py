import numpy as np
import matplotlib.pyplot as plt
import sys

g=np.genfromtxt(sys.argv[1], delimiter=";", skip_header=1, dtype='string', usecols=(0,1,2,4,5,7,9))
g_new=g[0:9357,:]
N=len(g_new[:,0])

for i in range(2, len(g_new[0,:])):
    for j in range(0, N):
        g_new[j,i]=g_new[j,i].replace(',','.')

date=g_new[:,0]
hour=g_new[:,1]
NH_pre=g_new[:,3].astype(np.float)

for i in range(N):
    if NH_pre[i] > -200.0:
        indmax=i

CO=g_new[:,2].astype(np.float)
NH=NH_pre[0:indmax+1]
BEN=g_new[:,4].astype(np.float)
NOX=g_new[:,5].astype(np.float)
NO2=g_new[:,6].astype(np.float)

def clean(arr):
    for i in range(len(arr)):
        if arr[i]== -200.0:
            arr[i]=0.
    return arr

COc=clean(CO)
NHc=clean(NH)
BENc=clean(BEN)
NOXc=clean(NOX)
NO2c=clean(NO2)

def fourier(arr):
    n=len(arr)
    fourier=np.zeros(n, dtype=complex)
    for i in range(n):
        for j in range(n):
            fourier[i]+=arr[j]*(np.exp(-2*np.pi*1j*i*j/n))
    real=np.real(fourier)
    imag=np.imag(fourier)
    return real, imag

def graf(real, imag, comp):
    n=len(real)
    time=np.linspace(0,n-1,n)

    fig=plt.figure()
    ax=plt.axes()
    plt.xlabel('Time')
    plt.ylabel('Fourier Transform')
    plt.plot(time, real, label='Real')
    plt.plot(time, imag, label='Imaginario')
    plt.legend()
    plt.savefig(str(comp)+'.pdf', format='pdf')
    plt.close()

realCO, imagCO = fourier(COc)
#realNH, imagNH = fourier(NHc)
#realBEN, imagBEN = fourier(BENc)
#realNOX, imagNOX = fourier(NOXc)
#realNO2, imagNO2 = fourier(NO2c)

graf(realCO, imagCO, 'CO')
#graf(realNH, imagNH, 'NHMC')
#graf(realBEN, imagBEN, 'BEN')
#graf(realNOX, imagNOX, 'NOX')
#graf(realNO2, imagNO2, 'NO2')

"""
fig=plt.figure()
ax=plt.axes()
plt.plot(CO)
plt.plot(NH)
plt.plot(BEN)
plt.plot(NOX)
plt.plot(NO2)
plt.show()"""

f=open('periodos.dat', 'w')
#f.write("{} \n".format(corr[i]))
f.close()
