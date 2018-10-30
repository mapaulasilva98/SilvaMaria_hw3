import numpy as np
import matplotlib.pyplot as plt 
import math 


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

dt=sigx[1]-sigx[0]