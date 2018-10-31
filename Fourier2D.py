import numpy as np
import matplotlib.pyplot as plt 
import math 
from scipy.signal import convolve2d
from scipy.fftpack import fft2, fftshift, ifftshift, ifft2



##### CUARTO PUNTO #####

#Almacene la imagen arbol.png en una arreglo de numpy

arbol = plt.imread('arbol.png')
#print(arbol.shape)


#Usando los paquetes de scipy, realice la transformada de Fourier de la imagen. 
#Eligiendo una escala apropiada, haga una grafica de dicha transformada y guardela sin mostrarla en ApellidoNombre_FT2D.pdf.


transformada=fft2(arbol)

transformada_shift=fftshift(transformada)

transformada_shift_abs=abs(transformada_shift)


#ahora hago el logaritmo para graficarlo

loga_transformada=np.log(transformada_shift_abs)

plt.imshow(loga_transformada)
plt.title("transformada de Fourier")
#plt.show()
plt.xlabel("frecuencia")
plt.ylabel("y(t)")
plt.savefig("SilvaMaria_FT2D.pdf")


#Haga un filtro que le permita eliminar el ruido periodico de la imagen. Para esto haga pruebas de como debe modificar la transformada de Fourier
n, m = arbol.shape 
N, M = n//2, m//2
r=25
transformada_shift_filtrada = np.copy(transformada_shift)
'''
for i in range(n):
    for j in range(m):
       distancia = math.sqrt((i-N)**2 + (j-M)**2)
        if distancia > r: 
           M1[i][j]=0
        else:
            M1[i][j] = M1[i][j]
'''
            
for i in range(n):
    for j in range(m):
        distancia = math.sqrt((i-128)**2 + (j-128)**2)
        if  distancia > 25 and distancia < 30: 
            transformada_shift_filtrada[i][j]=0

            
for i in range(n):
    for j in range(m):
        distancia = math.sqrt((i-200)**2 + (j-200)**2)
        if distancia < 10: 
            transformada_shift_filtrada[i][j]=0
        
for i in range(n):
    for j in range(m):
        distancia = math.sqrt((i-70)**2 + (j-60)**2)
        if distancia < 10: 
            transformada_shift_filtrada[i][j]=0

#Grafique la transformada de Fourier despues del proceso de filtrado, esta vez en escala LogNorm y guarde dicha grafica sin mostrarla en ApellidoNombre_FT2D_filtrada.pdf.

plt.imshow(abs(np.log(transformada_shift_filtrada)))
plt.title("transformada de Fourier")
plt.savefig("SilvaMaria_FT2D_filtrada..pdf")



#Haga la transformada de Fourier inversa y grafique la imagen filtrada. 
#Verifique que su filtro elimina el ruido periodico y guarde dicha imagen sin mostrarla en ApellidoNombre_Imagen_filtrada.pdf.

imagenFiltrada = np.real(ifft2(ifftshift(transformada_shift_filtrada)))
plt.imshow(imagenFiltrada)
plt.title("transformada de Fourier")
plt.savefig("SilvaMaria_Imagen_filtrada.pdf")





