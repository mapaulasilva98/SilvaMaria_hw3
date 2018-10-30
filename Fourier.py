import numpy as np
import matplotlib.pyplot as plt 
import math 
from scipy import fftpack
from scipy.fftpack import fft,fftfreq,ifft
from scipy.interpolate import interp1d



# Almacene los datos de signal.dat y de incompletos.dat

datosSignal=np.genfromtxt("signal.dat", delimiter=",")

datosIncompletos=np.genfromtxt("incompletos.dat", delimiter=",")
 
# Haga una grafica de los datos de signal.dat y guarde dicha grafica sin mostrarla en ApellidoNombre_signal.pdf.


sigx=datosSignal[:,0]
sigy=datosSignal[:,1]


plt.figure()
plt.plot(sigx,sigy)
plt.xlabel("Tiempo")
plt.ylabel("y(t)")
plt.title("signal")
plt.savefig("SilvaMaria_signal.pdf")


#Haga la transformada de Fourier de los datos de la senal usando su implementacio propia de la transformada discreta de fourier.

# mi numero de puntos 
n= len(sigx)

# mi delta de tiempo 
dt=sigx[1]-sigx[0]

# mi frecuencia 
frec= fftfreq(n,dt)

# suma para mi transformada de fourier 

suma= np.linspace (0,0,n)


for i in range (n):
	for j in range (len(suma)):
		suma[i] = suma[i] + (sigy[j]*(math.e**((-1j)*2*np.pi*j*i/n)))


trans= abs(suma)/n

trans2= (suma)/n

#Haga una grafica de la transformada de Fourier y guarde dicha grafica sin mostrarla en ApellidoNombre_TF.pdf.

plt.figure()
plt.plot(frec, trans )
plt.title("Transformada de Fourier")
plt.xlabel("frecuencia")
plt.ylabel("transformada")
#plt.show()
plt.savefig("SilvaMaria_TF.pdf")


#Imprima un mensaje donde indique cuales son las frecuencias principales de su senal.

principales=[]

for i in range (len (frec)):
	if (trans[i]>0.5):
		principales.append(frec[i])


print ("Las frecuencias principales de mi senal son:", principales)


#Haga un filtro pasa bajos con frecuencia de corte fc igual a 1000 Hz.
#realice la transformada inversa y haga una grafica de la senal filtrada. 
#Guarde dicha grafica sin mostrarla en ApellidoNombre_filtrada.pdf.



for i in range (len (trans2)):
	if (abs(frec[i])<=1000):
		trans2[i]=trans2[i]
	else: 	
		trans2[i]=0

inversa=ifft(trans2)


plt.figure()
plt.title("Transformada filtrada ")
plt.xlabel("frecuencia")
plt.ylabel("Transformada")
plt.plot(sigx,inversa)
#plt.show()
plt.savefig("SilvaMaria_filtrada.pdf")



# Escriba un mensaje en la terminal explicando por que no puede hacer la transformada de Fourier de los datos de incompletos.dat


###########################################################################################

#Haga una interpolacion cuadratica y una cubica de sus datos incompletos.dat con 512 puntos. 
#Haga la trasformada de Fourier de cada una de las series de datos interpoladas.

incomx=datosIncompletos[:,0] # este es mi tiempo de toma de datos 
incomy=datosIncompletos[:,1] # estos son mis datos tomados 



x=np.linspace(min(incomx), max(incomx), 512)

dt2=incomx[1]-incomx[0]

frec2= fftfreq(len(x),dt2)

# cubica 

cubico_data = interp1d(incomx, incomy, kind='cubic', bounds_error=False)
cubico = cubico_data(x)



# Transformada de la cubica

sumar= np.linspace (0,0,len(x))


for i in range (len(x)):
	for j in range (len(sumar)):
		sumar[i] = sumar[i] + (cubico[j]*(math.e**((-1j)*2*np.pi*j*i/n)))



trans2= abs(sumar)/len(x)




# cuadratica 

cuadratico_data = interp1d(incomx, incomy, kind='quadratic', bounds_error=False)
cuadratico = cuadratico_data(x)


# transfromada cuadratica 

sumar2= np.linspace (0,0,len(x))


for i in range (len(x)):
	for j in range (len(sumar2)):
		sumar2[i] = sumar2[i] + (cuadratico[j]*(math.e**((-1j)*2*np.pi*j*i/n)))

trans3= abs(sumar2)/len(x)




plt.figure()
plt.plot(frec2, trans2, color="r")
plt.plot(frec2, trans3)
plt.show()





