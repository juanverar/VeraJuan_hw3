import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack, ndimage
from matplotlib.colors import LogNorm
import matplotlib.cm as cm
from PIL import Image

#Convertir la imagen a un array
img=Image.open('arbol.png').convert('RGBA')
arbol=np.asarray(img)

#Aplicar Fourirer al arreglo
def fourier(imagen):
	return fftpack.fft2(imagen)

plt.figure()
plt.imshow(np.abs(fourier(arbol)), cmap=cm.Greys_r, norm = LogNorm())
plt.show()
print len(arbol[1])
#def filtro():
#	for i in range(len(arbol[0])):
		
#Aplicar la inversa de Fourier al arreglo flitrado.
def inversa(imagen):
	return fftpack.ifft2(imagen)
arbol1 = plt.rcParams['image.cmap'] ='gray'
plt.figure()
plt.imshow(np.abs(inversa(fourier(arbol))), cmap=cm.Greys_r, norm = LogNorm())
plt.show()
