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
AA=A[:,2:,]


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

#for i in range(len(val)):
#	print 'Para el autovalor=', val[i],'se tiene el autovector=',vec[i]

#2.4 Determinar cuales son los parametros mas importantes en base a lo obtenido antes.

tipo=A[:,0]
M=[]
listM=[]
B=[]
listB=[]
#Determinar cual dato corresponde a cada una de las dos opciones.
for i in range(len(AL)):
	if AL[i]=='M':
		M.append(i)
	if AL[i]=='B':
		B.append(i)
#Llenar dos arreglos con los datos correspondientes
for i in range(len(M)):
	listM.append(AA[M[i]])
	listB.append(AA[B[i]])

#Multiplicacion de los datos en sus dos categorias con sus respectivos autovectores.

Malignos=np.matmul(listM,vec)
Benignos=np.matmul(listB,vec)

#Se plotean los datos segun su clasificacion y se muestran con diferentes colores en la grafica.

plt.scatter(Benignos[:,0],Benignos[:,1],color='g',label="Benignos",marker='+')
plt.scatter(Malignos[:,0],Malignos[:,1],color='r',label="Malignos",marker='+')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA aplicado a diagnostico de pacientes con cancer.')
plt.legend()
plt.grid()
plt.savefig('VeraJuan_PCA.pdf')


