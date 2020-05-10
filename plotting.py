import matplotlib.pyplot as plt
import pandas as pd

data_set_pd = pd.read_csv('results.csv')
data_set = data_set_pd.values

data_set_pd = pd.read_csv('NN_result_combined.csv')
data_set_nn = data_set_pd.values


#range of rows in csv file
row_start = 0
row_end = 20

true_loc = data_set[row_start:row_end,0:2]
rssi = data_set[row_start:row_end,2:4]
toa = data_set[row_start:row_end,4:6]
aoa = data_set[row_start:row_end,6:8]
avg = data_set[row_start:row_end,8:10]

rssi_nn = data_set_nn[row_start:row_end,2:4]
toa_nn = data_set_nn[row_start:row_end,4:6]
aoa_nn = data_set_nn[row_start:row_end,6:8]
all_nn = data_set_nn[row_start:row_end,8:10]



################################### Ploting #####################################

############################# Traditional ###################################


################################# RSSI ####################################
plt.subplot(221)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
rssi_p = plt.plot (rssi[:, 0],rssi[:, 1], 'C1 +', label='RSSI')
plt.title('RSSI')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()


################################ TOA ########################################
plt.subplot(222)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
toa_p = plt.plot (toa[:, 0], toa[:, 1], 'C2 *', label='TOA')
plt.title('TOA')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()


################################ AOA ########################################
plt.subplot(223)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
toa_p = plt.plot (aoa[:, 0], aoa[:, 1], 'C3 s', label='AOA')
plt.title('AOA')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()

############################### Combined ##############################
plt.subplot(224)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
avg_p = plt.plot (avg[:, 0], avg[:, 1], 'C4 d', label='Combined')
plt.title('Combined')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()


plt.show()


############################### NN ################################


##################################### RSSI_NN####################################
plt.subplot(221)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
rssi_nn_p = plt.plot (rssi_nn[:, 0],rssi_nn[:, 1], 'C1 +', label='RSSI_NN')
plt.title('RSSI_NN')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()


############################### TOA_NN #####################################
plt.subplot(222)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
toa_nn_p = plt.plot (toa_nn[:, 0], toa_nn[:, 1], 'C2 *', label='TOA_NN')
plt.title('TOA_NN')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()

###################################### AOA_NN ###############################
plt.subplot(223)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
aoa_nn_p = plt.plot (aoa_nn[:, 0], aoa_nn[:, 1], 'C3 s', label='AOA_NN')
plt.title('AOA_NN')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()


############################### Combined_NN ##############################
plt.subplot(224)
true_p = plt.plot (true_loc[:, 0], true_loc[:, 1], 'r o', label='True locations')
avg_p = plt.plot (all_nn[:, 0], all_nn[:, 1], 'C4 d', label='Combined_NN')
plt.title('Combined_NN')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.ylim(0, 120)
plt.xlim(0, 120)
plt.legend()


plt.show()