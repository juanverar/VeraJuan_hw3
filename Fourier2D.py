import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack, ndimage
from matplotlib.colors import LogNorm
import matplotlib.cm as cm
import cv2



img=cv.LoadImage("arbol.png")
arbol=np.asarray(img)

def fourier(imagen):
	return fftpack.fft2(imagen)

plt.figure()
plt.imshow(np.abs(fourier(arbol)), cmap=cm.Greys_r, norm = LogNorm())
plt.show()

#def Corte(imagen):
#	f = np.abs(fourier(imagen))
#	row = f.shape[0]
#	centro = int(row/2)
#	return f[centro, :]

plt.figure()
plt.plot(Corte(arbol))
plt.show()

