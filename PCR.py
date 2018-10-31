import numpy as np
import matplotlib.pylab as plt
import numpy.linalg
import urllib2
import time

#2.1  Descarga de los datos desde la pagina web.

descarga="http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat"
a="WDBC.txt"
down=urllib2.urlopen(descarga)
archivo=file(a,"w")
archivo.write(down.read())
archivo.close()
print 'Se descargo el archivo WDBC.dat'
A=np.genfromtxt('WDBC.txt',delimiter=",")
AL=np.genfromtxt('WDBC.txt',delimiter=",",dtype=str)
print A



for i in range(len(A[0])):
	A=np.genfromtxt('WDBC.txt',delimiter=",",dtype=str, usecols=(i))

#Convertir las letras de la columna 2 en variables numericas M=0 y B=1.

copy=np.copy(A[:,1:])
def cambiostr():
	for i in range(0,len(copy[:,0])):
		if AL[i,1]=='B':
			copy[i,0]=1.0
		if Al[i,1]=='M':
			copy[i,0]=0.0
cambiostr()


