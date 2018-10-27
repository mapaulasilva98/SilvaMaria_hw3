import numpy as np
import matplotlib as plt 
import math 

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

 
print (matrizCovari)






print (np.cov(matrizAct))



















