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


'''
plt.figure()
plt.plot(vectoresPropios[0],x)
plt.plot(x,vectoresPropios[1], color="r")
plt.show()
'''


# producto punto de mis autovaloes con mis autovectores especiales 

valoresB=[]


for i in range(len(vectoresPropios[0])):
	valoresB.append(np.dot(valoresPropios[i],vectoresPropios[i]))



# producto punto de mis autovaloes con mis autovectores especiales 

valoresC=[]


for i in range(len(vectoresPropios[1])):
	valoresC.append(np.dot(valoresPropios[i],vectoresPropios[i]))

'''

plt.figure()
for i in range(len(matrizDatos)):
	if(matrizDatos[i,0]==0):
		 plt.plot(valoresB[i],valoresC[i], color="r")

	else :
		 plt.plot(valoresB[i],valoresC[i])

plt.show()

'''
