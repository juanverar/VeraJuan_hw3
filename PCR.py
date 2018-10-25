import numpy as np
import matplotlib.pylab as plt
import numpy.linalg
import urllib2
import time

#Descarga de los datos desde la pagina web.



descarga="http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat"
a="WDBC.dat"
down=urllib2.urlopen(descarga)
archivo=file(a,"w")
archivo.write(down.read())
archivo.close()
print 'Se descargo el archivo WDBC.dat'
