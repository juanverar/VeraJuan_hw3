import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
import math
from scipy.interpolate import interp1d

#3.1 Guardar los datos en variables individuales
y = np.loadtxt("signal.dat",delimiter= ",",usecols=(1,))
x = np.loadtxt("signal.dat",delimiter= ",",usecols=(0,))
x1 = np.loadtxt("incompletos.dat",delimiter= ",",usecols=(0,))
y1 = np.loadtxt("incompletos.dat",delimiter= ",",usecols=(1,))

#3.2  Graficar ambas senales.
#Grafica de signal.dat
plt.figure()
plt.plot(x,y)
plt.title('Original signal')
plt.grid()
plt.savefig('VeraJuan_signal.pdf')

#3.3 Aplicacion de transformada de fourier
#Numero de puntos,dt y frecuencia
N=len(x)
dt=x[1]-x[0]
f=fftfreq(N,dt)
suma=np.linspace(0,0,N)


for i in range(N):
	for j in range(N):
		suma[i]= suma[i]+(y[j]*np.exp((-1j)*2*np.pi*i*j/N))

#3.4 Grafica de la transformada
plt.figure()
plt.plot(f,(np.abs(suma)/N))
plt.title('Trasformada de Fourier')
plt.grid()
plt.savefig('VeraJuan_TF.pdf')

#3.5 Frecuencias principales de la senal.
fprin=[]
for i in range(len(f)/2):
	if((np.abs(suma[i])/N)>0.5):
		fprin.append(np.abs(f[i]))
print 'Las frecuencias principales de la senal son=', fprin

#3.6 Filtro pasa bajos f=1000Hz
tf=suma/N
def pasabajos():
	for i in range(len(suma/N)):
		if (np.abs(f[i])>1000):
			tf[i]= 0
	return tf

inv=ifft(pasabajos())
plt.figure()
plt.plot(x,inv)
plt.title('Transformada al ser filtrada')
plt.grid()
plt.savefig('VeraJuan_filtrada.pdf')
