import numpy as np
import matplotlib.pyplot as plt 
import math 
from scipy.signal import convolve2d
from scipy.fftpack import fft2, fftshift


##### CUARTO PUNTO #####

#Almacene la imagen arbol.png en una arreglo de numpy

arbol = plt.imread('arbol.png')


'''
Usando los paquetes de scipy, realice la transformada de Fourier de la imagen. 
Eligiendo una escala apropiada, haga una grafica de dicha transformada y guardela sin mostrarla en ApellidoNombre_FT2D.pdf.
'''

transformada=fft2(arbol)

transformada_shift=fftshift(transformada)

transformada_shift_abs=abs(transformada_shift)


#ahora hago el logaritmo para graficarlo

loga_transfromada=np.log(transformada_shift_abs)

plt.imshow(loga_transfromada)
plt.title("transformada de Fourier")
#plt.show()
plt.xlabel("frecuencia")
plt.ylabel("y(t)")
plt.savefig("SilvaMaria_FT2D.pdf")
