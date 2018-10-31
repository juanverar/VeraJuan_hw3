import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack, ndimage
from matplotlib.colors import LogNorm
import matplotlib.cm as cm
from PIL import Image

#Convertir la imagen a un array
imagen=Image.open('arbol.png').convert('RGBA')
arbol=np.asarray(imagen)

#Aplicar Fourirer al arreglo
ff=fftpack.fft2(arbol)
#Centrar las frecuecncias que tengan valor de 0 en la mitad del arreglo

frec=np.fft.fftfreq(len(arbol),0.1)
plt.plot(frec,ff[1])
plt.show()


centrado=np.fft.fftshift(ff)


plt.figure()
plt.imshow(np.abs(centrado), cmap=cm.Greys_r, norm = LogNorm())
plt.show()

print len(arbol[1])
#def filtro():
#	for i in range(len(arbol[0])):
		
#Aplicar la inversa de Fourier al arreglo flitrado.
#def inversa(imagen):
#	return fftpack.ifft2(imagen)
#arbol1 = plt.rcParams['image.cmap'] ='gray'
#plt.figure()
#plt.imshow(np.abs(inversa(fourier(arbol))), cmap=cm.Greys_r, norm = LogNorm())
#plt.show()

