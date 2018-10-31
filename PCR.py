import numpy as np
import matplotlib.pyplot as plt 
import math 

from numpy.linalg import *
from scipy.linalg import expm,inv

###### SEGUNDO PUNTO #######

###### PARTE A #####

datos= open("WDBC.dat.txt", "r")

datosArr = datos.read().split('\n')

#Matriz donde se van a almacenar los datos, la matriz que utilizare para hacer la metriz de covarianza
matrizDatos = np.zeros((569,31))

#Se pasan los datos a la matriz creada
for i in range(len(matrizDatos)):
	#Se hace split por comas (,) para meter cada dato en una columna de la fila
	lineaActual = datosArr[i].split(',')
	for j in range(len(matrizDatos[1])):
		#Se hace lineaActual[j+2] para no leer ni el ID ni la M o B
		if (j==0):
			#Aqui voy a decir si es igual a M = 0 y si es igual a B = 1
			if(lineaActual[j+1]=="M"):
				lineaActual[j+1]=0
			else:
				lineaActual[j+1]=1	
		matrizDatos[i][j] = lineaActual[j+1]


##### PARTE B #####

#Realizare la matriz de covarianza


# matriz actualizada sin la primera columna
matrizAct=matrizDatos[:,1:]

#print (matrizAct)


# matriz de unos 

unos=np.ones((569,569))

#print (unos)

# hago la multimplicacion 

#matriz donde voy a guardar el resultado 

matrizResul=np.zeros((569,30))

for i in range(len(unos)):
	for j in range(len(matrizAct[0])):
 		for k in range(len(matrizAct)):
 			matrizResul[i][j] += unos[i][k] * matrizAct[k][j] * 1/569
 
#print(matrizResul)

# ahota a la matriz actual la matriz resultado 

for i in range(len(matrizResul)):
	for j in range(len(matrizResul[1])):
		matrizResul[i][j] = matrizAct[i][j] - matrizResul[i][j]

#print(matrizResul)


# hago la transpuesta de mi metriz 
transpuesta= np.transpose(matrizResul)

#print (transpuesta)

# ahora multiplico mi matriz reultado por su matriz trasnpuesta 

matrizPorTrans=np.zeros((30,30))


for i in range(len(transpuesta)):
	for j in range(len(matrizResul[0])):
 		for k in range(len(matrizResul)):
 			matrizPorTrans[i][j] += transpuesta[i][k] * matrizResul[k][j]

#print (matrizPorTrans)

#finalmente obtengo la mtriz transpuesta

matrizCovari=np.zeros((30,30))

for i in range (len(matrizPorTrans)):
	for j in range (len(matrizPorTrans[0])):
		matrizCovari[i][j]=matrizPorTrans[i][j]*1/569

 
#print (matrizCovari)

#print (matrizCovari.shape)


#print (np.cov(matrizAct))


##### PARTE C #####

# calcular los autovalores y los autovectores de la matriz de covarianza 

valoresPropios = np.linalg.eig(matrizCovari)[0] 


vectoresPropios= np.linalg.eig(matrizCovari)[1] 



############################### intento #############################

cova=np.cov(matrizAct) 

valoresPropios2=np.linalg.eig(cova)[0]





# autovalor asociado a cada autovector 

for i in range (len(valoresPropios)):
	print ("El autovalor", valoresPropios[i], "tiene asociado el autovector", vectoresPropios[i])




# Los parametros mas importantes con base a las componentes de los autovalores 


valorMayor=0
valorMayor2=0



for i in range(len(valoresPropios)):
    temp = valoresPropios[i]
    if (valoresPropios[i] > valorMayor):
        valorMayor = temp
        

for i in range(len(valoresPropios)):
    temp = valoresPropios[i]
    if(valoresPropios[i] > valorMayor2 and valoresPropios[i] != valorMayor):
        valorMayor2 = temp


print ("Los valores mas importante de las componentes de los autovalores son:", valorMayor ,"y", valorMayor2 )

 

# para este punto debo separar las matrices de los malignos y beningnos y despues realizar producto punto con con mi autovectores importante 

prematrizMalignos=np.zeros((569,31))
prematrizBenignos=np.zeros((569,31))


indiceUnos = 0
indiceCeros = 0

for i in range(len(matrizDatos)):
    if (matrizDatos[i][0] == 0):
        prematrizMalignos[indiceCeros] = matrizDatos[i]
        indiceCeros=indiceCeros+1
    else:
        prematrizBenignos[indiceUnos] = matrizDatos[i]
        indiceUnos=indiceUnos+1

matrizMalignos=prematrizMalignos[:,1:]
matrizBenignos=prematrizBenignos[:,1:]

print (matrizMalignos.shape)


# ahora hago producto punto de cada una de mis metrices para obtener lo que tengo que plotear al final 


valoresXm=[]


for i in range(len(vectoresPropios[0])):
	valoresXm.append(np.dot(vectoresPropios[0],matrizMalignos[i]))

valoresXmArray = np.asarray(valoresXm) ####################### DATOS PARA PLOTEAR 


##################################################################################################

valoresYm=[]


for i in range(len(vectoresPropios[1])):
	valoresYm.append(np.dot(vectoresPropios[1],matrizMalignos[i]))


valoresYmArray = np.asarray(valoresYm) ######################## DATOS PARA PLOTEAR

##################################################################################################

valoresXb=[]


for i in range(len(vectoresPropios[0])):
	valoresXb.append(np.dot(vectoresPropios[0],matrizBenignos[i]))

valoresXbArray = np.asarray(valoresXb)

print (valoresXbArray)

##################################################################################################

valoresYb=[]


for i in range(len(vectoresPropios[1])):
	valoresYb.append(np.dot(vectoresPropios[1],matrizBenignos[i]))


valoresYbArray = np.asarray(valoresYb)

print (valoresYbArray)

##################################################################################################


 

plt.figure()
plt.scatter(valoresXmArray,valoresYmArray, color = "r", label="Malignos")
plt.scatter(valoresXbArray,valoresYbArray, color= "green", label="Benignos")
plt.title("Malignos VS Beningnos")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.ylim(-600,100)
plt.legend()
plt.savefig("SilvaMaria_PCA.pdf")
plt.show()


#Imprima un mensaje diciendo si el metodo de PCA es util para hacer esta clasificacion,
#si no sirve o si puede ayudar al diagnostico para ciertos pacientes, argumentando claramente su posicion.


print("Este metodo de clasificacion es efectivo, pues aunque los datos se lleguen a mezclar un puco en cierto punto, la tendencia se nota")
print("pues hay se llega a un sector en donde es indudable que en este caso el tumor va a ser maligno. esto significa que los vectores")
print("seleccionados que son los mas importantes, cumplen con la funcion de diferenciar los pacientes con tumores malignos y benignos")




