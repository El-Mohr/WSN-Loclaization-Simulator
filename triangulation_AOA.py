from __future__ import division
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as mth


#Parameters
max_size = 100 #Max size of x and y coordinates in Meters
anchors_num=4 #Number of anchors to be accounted (3 or 4)
row_start = 0 #range of rows in csv file
row_end = 50 #range of rows in csv file
AoA_max = 360
AoA_min = 0
anchors_max = max_size
anchors_min = 0	
nodes_max = max_size
nodes_min = 0	

#load data
data_set_pd = pd.read_csv('M_test_set_rand_a_noise.csv')
data_set =data_set_pd.values
anchors_normalized=data_set[row_start:row_end,0:2*anchors_num]
AoA_normalized = data_set[row_start:row_end,12:12+anchors_num]
nodes_normalized=data_set[row_start:row_end,20:22]




nodes_num=np.shape(AoA_normalized)[0]
AoA = np.zeros ((nodes_num,anchors_num))
for i in range(0, nodes_num):
	for j in range(0, anchors_num):
		AoA [i][j] =  AoA_normalized[i][j]*(AoA_max - AoA_min)+AoA_min

anchors = np.zeros ((nodes_num,2*anchors_num))
for i in range(0, nodes_num):
	for j in range(0, 2*anchors_num):		
		anchors [i][j] =  anchors_normalized[i][j]*(anchors_max - anchors_min)+anchors_min

nodes = np.zeros ((nodes_num,2))
for i in range(0, nodes_num):
	for j in range(0, 2):		
		nodes [i][j] =  nodes_normalized[i][j]*(nodes_max - nodes_min)+nodes_min
		
		
#Triangulation
Positions_triangulation = np.zeros ((nodes_num,2)) #Positions retrieved from AoA using triangulations
for i in range(0, nodes_num):
	a=np.array([])
	b=np.array([])				
	for j in range(0, anchors_num):
		a = np.append(a,[1,-mth.tan(mth.radians(AoA[i][j]))])
		b = np.append(b,[anchors[i][j*2+1]-anchors[i][j*2]*mth.tan(mth.radians(AoA[i][j]))])			
	a=np.reshape(a, (anchors_num,-1)) 
	x = np.linalg.lstsq(a, b)[0]
	Positions_triangulation[i]=np.flip(x,0)
	
print("Solution")		
print(Positions_triangulation)	
print("nodes")		
print(nodes)

square_error = (nodes - Positions_triangulation)**2    
mse = np.mean(square_error)
print("Mean Square Error")		
print(mse)	
		
# for i in range(0, anchors_num):
# 	plt.plot (anchors[0][i*2], anchors[0][i*2+1], 'r o')
# for i in range(0, nodes_num):
# 	plt.plot (nodes[i][0], nodes[i][1], 'b o')
# 	plt.plot (Positions_triangulation[i][0], Positions_triangulation[i][1], 'g x')
# plt.show()

with open('results.csv', 'ab') as file:
		np.savetxt(file, Positions_triangulation, delimiter=',')