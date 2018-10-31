import numpy as np
import matplotlib.pylab as plt
import numpy.linalg
import urllib2
import time

#2.1  Descarga de los datos desde la pagina web.

descarga="http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat"
a="WDBC.dat"
down=urllib2.urlopen(descarga)
archivo=file(a,"w")
archivo.write(down.read())
archivo.close()
print 'Se descargo el archivo WDBC.dat'

A=np.genfromtxt('WDBC.dat',delimiter=",")
AL=np.genfromtxt('WDBC.dat', dtype = str, delimiter=",", usecols=(1))



#for i in range(len(A[0])):
#	A=np.genfromtxt('WDBC.txt',delimiter=",",dtype=str, usecols=(i))

#2.2 Implementacion de matriz de covarianza
def matrizCov(dat):
	n=np.shape(dat)[0]
	var=np.shape(dat)[1]
	matrix=np.ones([var,var])
	for i in range(var):
		for j in range(var):
			mean1=np.mean(dat[:,i])
			mean2=np.mean(dat[:,j])
			matrix[i,j]=np.sum((dat[:,i]-mean1)*(dat[:,j]-mean2))/(n-1)
	return matrix

cov=matrizCov(A[:,2:,])
print cov


#2.3 Calculo de los autovectores y autovalores

val,vec = np.linalg.eig(cov)

for i in range(len(val)):
	print 'Para el autovalor=', val[i],'se tiene el autovector=',vec[i]

