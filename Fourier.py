import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

#3.1 Guardar los datos en variables individuales
y = np.loadtxt("signal.dat",delimiter= ",",usecols=(1,))
x = np.loadtxt("signal.dat",delimiter= ",",usecols=(0,))
x1 = np.loadtxt("incompletos.dat",delimiter= ",",usecols=(0,))
y1 = np.loadtxt("incompletos.dat",delimiter= ",",usecols=(1,))

#3.2  Graficar ambas señales.
#Grafica de signal.dat
plt.figure()
plt.plot(x,y)
plt.title('Original signal')
plt.grid()
plt.savefig('VeraJuan_signal.pdf')

#3.3 Aplicacion de transformada de fourier

def Fourier



