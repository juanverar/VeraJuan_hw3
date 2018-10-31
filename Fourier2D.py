import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm
import matplotlib.cm as cm


#4.1 Convertir la imagen a un array
imagen=plt.imread('arbol.png')

#4.2 Aplicar Fourirer al arreglo y graficar
ff=fftpack.fft2(imagen)
#Centrar las frecuecncias que tengan valor de 0 en la mitad del arreglo.
centrado=fftpack.fftshift(ff)

#4.3 Aplicar filtro a la imagen para eliminar ruido periodico.
plt.figure()
plt.imshow(np.abs(centrado), cmap=cm.autumn, norm = LogNorm())
plt.title('Grafica de la transformada')
plt.colorbar()
plt.savefig('VeraJuan_FT2D.pdf')

#A partir de prueba y error se determina el minimo y maximo, con estos valores se apica el filtro sobre la transformada centrada.

def filtro():
	for i in range(np.shape(centrado)[0]):
		for j in range(np.shape(centrado)[0]):
			if(centrado[i][j]<4400 and centrado[i][j]>2100):
				centrado[i][j]=0
	return centrado
#Aplicar la inversa de Fourier al arreglo flitrado.
imagen2=filtro()
nueva=fftpack.ifftshift(imagen2)
iff=fftpack.ifft2(nueva)

#4.4 Grafica de la transformada filtrada.
plt.figure()
plt.imshow(np.log(np.abs(imagen2)), cmap=cm.autumn, norm = LogNorm())
plt.title('Grafica de la transformada filtrada')
plt.colorbar()
plt.savefig('VeraJuan_FT2D_filtrada.pdf')

#4.5 Grafica de la imagen filtrada aplicada la inversa de la transformada.
plt.figure()
plt.imshow(np.abs(iff), cmap='gray', norm = LogNorm())
plt.title('Grafica de la imagen filtrada')
plt.savefig('VeraJuan_Imagen_filtrada.pdf')
