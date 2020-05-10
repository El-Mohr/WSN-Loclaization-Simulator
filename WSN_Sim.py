################ Localization Simple Simulator ######################


##Needed Libraries
import numpy as np
import math as mth
import matplotlib.pyplot as plt


##Parameters to be assigned

#Network Parameters
np.random.seed(1337)
max_size = 100 #Max size of x and y coordinates in Meters

rand_nodes = 1 #Enables random nodes or user defined nodes 
nodes_num = 20 #Nnumber of static nodes
nodes = np.array([ [50,50] ]) #User Defined Anchors positions

rand_anchors = 1 #Enables random anchors or user defined anchors 
anchors_num = 4 #Number of Anchors
anchors = np.array([ [0,0], [0,max_size], [max_size, 0], [max_size,max_size] ]) #User Defined Anchors positions

#Path Loss Parameters
PL0 = -36.029 #Reference Path Loss in dB
PL_exponent = 2.386 #Path loss Exponent
d0 = 1 #Reference Distance in Meters
PL_noise_mean = 0 #Noise Mean
PL_noise_std_deviation = 0.5 #Noise Standard Deviation in dB
PL_noise_en = 1 #Activates Path Loss Noise

#Angle of Arrival Parameters
AoA_noise_mean = 0 #Noise Mean
AoA_noise_std_deviation = 8 #Noise Standard Deviation in degrees
AoA_noise_en = 1 #Activates Angle of Arrival Noise

#Time of Arrival Parameters
ToA_noise_mean = 0 #Noise Mean
ToA_noise_std_deviation = 5 #Noise Standard Deviation in ns
ToA_noise_en = 1 #Activates Angle of Arrival Noise
light_speed = 299792458


##Main Code
#loop to generate more data

header = 'anc1_x,anc1_y,anc2_x,anc2_y,anc3_x,anc3_y,anc4_x,anc4_y,anc1_RSS,anc2_RSS,anc3_RSS,anc4_RSS,anc1_AoA,anc2_AoA,anc3_AoA,anc4_AoA,anc1_ToA,anc2_ToA,anc3_ToA,anc4_ToA,sensor_x,sensor_y'

for loopcnt in range(500):

    #Anchors
    if rand_anchors==1:
    	anchors = np.random.randint(0, max_size, (anchors_num,2)) #Nodes Positions 
    else: 
    	anchors_num = int(anchors.shape[0]) #Number of Anchors
    
    anchors_max = max_size
    anchors_min = 0
    anchors_normalized = np.zeros ((anchors_num,2))
    for i in range(0, anchors_num):
    	for j in range(0, 2):
    		anchors_normalized [i][j] = (anchors [i][j] - anchors_min) / (anchors_max - anchors_min)
    		
    # print("Anchors")
    # print(anchors_normalized)
    
    
    #Nodes
    if rand_nodes==1:
    	nodes = np.random.randint(0, max_size, (nodes_num,2)) #Nodes Positions 
    else: 
    	nodes_num = int(nodes.size/2) #Number of Anchors
    
    nodes_max = max_size
    nodes_min = 0
    nodes_normalized = np.zeros ((nodes_num,2))
    for i in range(0, nodes_num):
        for j in range(0, 2):
            nodes_normalized [i][j] = (nodes [i][j] - nodes_min) / (nodes_max - nodes_min)
    		
    # print("Nodes")
    # print(nodes_normalized)
    
    
    #Distances
    distances = np.zeros ((nodes_num,anchors_num))
    
    for i in range(0, nodes_num):
        for j in range(0, anchors_num):
            distances [i][j] = (mth.sqrt( (anchors [j,0] - nodes [i,0])**2 + (anchors [j, 1] - nodes[i,1])**2 ))
    
    		
    distance_max = mth.sqrt(2)* max_size
    distance_min = 0
    distance_normalized = np.zeros ((nodes_num,anchors_num))
    for i in range(0, nodes_num):
        for j in range(0, anchors_num):
            distance_normalized [i][j] = (distances [i][j] - distance_min) / (distance_max - distance_min)
    		
    		
    # print("Distances")
    # print(distance_normalized)
    
    		
    #Recieved Signal Strength
    PL_noise = np.random.normal(PL_noise_mean, PL_noise_std_deviation, (nodes_num,anchors_num))  #Path Loss Noise
    PL = np.zeros ((nodes_num,anchors_num)) #Path Loss
    for i in range(0, nodes_num):
        for j in range(0, anchors_num):
            try:
                PL [i][j] = PL0 + 10*PL_exponent*mth.log10(distances[i][j]/d0) + PL_noise_en*PL_noise [i][j]
            except:
                print(f'distance= {distances[i][j]/d0}, using -100db for path loss')
                PL [i][j] = PL0 + 10*PL_exponent*(-2) + PL_noise_en*PL_noise [i][j]
    
    PL_max = PL0 + 10*PL_exponent*mth.log10(distance_max/d0) + 5*PL_noise_std_deviation
    PL_min = PL0 + 10*PL_exponent*mth.log10(0.01) - 5*PL_noise_std_deviation
    PL_normalized = np.zeros ((nodes_num,anchors_num))
    for i in range(0, nodes_num):
    	for j in range(0, anchors_num):
    		PL_normalized [i][j] = (PL [i][j] - PL_min) / (PL_max - PL_min)
    		if (PL_normalized [i][j] < 0):
    			PL_normalized [i][j] = 0
    				
    # print("Path Loss")		
    # print(PL_normalized)
    
    
    #Angle of Arrival
    AoA_noise = np.random.normal(AoA_noise_mean, AoA_noise_std_deviation, (nodes_num,anchors_num))  #Angle of Arrival Noise
    AoA = np.zeros ((nodes_num,anchors_num)) #Angle of Arrival in degrees
    for i in range(0, nodes_num):
        for j in range(0, anchors_num):
            AoA [i][j] =  (mth.degrees(mth.atan((anchors [j, 1] - nodes[i,1])/(anchors [j,0] - nodes [i,0])))+180+180*~((anchors [j,0] - nodes [i,0])<0)  + AoA_noise_en*AoA_noise [i][j])%360
            if mth.isnan(AoA [i][j]):
                AoA [i][j] = 0
    AoA_max = 360
    AoA_min = 0
    AoA_normalized = np.zeros ((nodes_num,anchors_num))
    for i in range(0, nodes_num):
        for j in range(0, anchors_num):
            AoA_normalized [i][j] = (AoA [i][j] - AoA_min) / (AoA_max - AoA_min)

    # print("AoA")		
    # print(AoA_normalized)
    
    
    
    #Propagation Delay (Time of Arrival)
    ToA_noise = np.random.normal(ToA_noise_mean, ToA_noise_std_deviation, (nodes_num,anchors_num))  #Time of Arrival Noise
    ToA = np.zeros ((nodes_num,anchors_num)) #Time of Arrival in ns
    for i in range(0, nodes_num):
        for j in range(0, anchors_num):
            ToA [i][j] =  (distances [i][j] / light_speed) *10**9  + ToA_noise_en*ToA_noise[i][j]
    
    		
    ToA_max = (distance_max / light_speed) *10**9  + 5*ToA_noise_std_deviation
    ToA_min = 0
    ToA_normalized = np.zeros ((nodes_num,anchors_num))
    for i in range(0, nodes_num):
    	for j in range(0, anchors_num):
    		ToA_normalized [i][j] = (ToA [i][j] - ToA_min) / (ToA_max - ToA_min)
    		if (ToA_normalized [i][j] < 0):
    			ToA_normalized [i][j] = 0
    
    # print("ToA")		
    # print(ToA_normalized)		
    
    
    #Final Matrix to CSV
    anchors_flat=anchors_normalized.flatten()
    
    anchors_repeated=np.zeros ((nodes_num,anchors_num*2)) #anchors repeated by number of nodes
    for i in range(0, nodes_num):
    	anchors_repeated [i] =  anchors_flat
    	
    # print("repeated")		
    # print(anchors_repeated)
    	
    concatenated_matrix=np.concatenate((anchors_repeated,PL_normalized, AoA_normalized, ToA_normalized, nodes_normalized), axis=1)
    
    if loopcnt == 0:
        with open('data_set.csv', 'wb') as file:
            np.savetxt(file, concatenated_matrix, delimiter=',', header=header)
    else:
        with open('data_set.csv', 'ab') as file:
            np.savetxt(file, concatenated_matrix, delimiter=',')
    
    print("Generated Env # ", loopcnt+1)		
    #print(concatenated_matrix)
    
    
#    for i in range(0, anchors_num):
#    	plt.plot (anchors[i][0], anchors[i][1], 'r o')
#    for i in range(0, nodes_num):
#    	plt.plot (nodes[i][0], nodes[i][1], 'b o')
#    plt.show()


#Notes: We may use Max range and dimensions as #3-D too, also noise options