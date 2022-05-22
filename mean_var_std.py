import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.") 

    else:
        calculations = {}

        flatten_list = np.array(list)
        flatten_list_mean = np.mean(flatten_list)
        flatten_list_var = np.var(flatten_list)
        flatten_list_std = np.std(flatten_list)
        flatten_list_max = np.max(flatten_list)
        flatten_list_min = np.min(flatten_list)
        flatten_list_sum = np.sum(flatten_list)

        #3*3 Matrix
        matrix = np.reshape(flatten_list,(3,3))

        axis0_mean = np.mean(matrix,axis=0)
        axis0_var = np.var(matrix,axis=0)
        axis0_std = np.std(matrix,axis=0)
        axis0_max = np.max(matrix,axis=0)
        axis0_min = np.min(matrix,axis=0)
        axis0_sum = np.sum(matrix,axis=0)

        axis1_mean = np.mean(matrix,axis=1)
        axis1_var = np.var(matrix,axis=1)
        axis1_std = np.std(matrix,axis=1)
        axis1_max = np.max(matrix,axis=1)
        axis1_min = np.min(matrix,axis=1)
        axis1_sum = np.sum(matrix,axis=1)

        calculations ={
        'mean': [axis0_mean.tolist(), axis1_mean.tolist(), flatten_list_mean],
        'variance': [axis0_var.tolist(), axis1_var.tolist(), flatten_list_var],
        'standard deviation':[axis0_std.tolist(), axis1_std.tolist(), flatten_list_std],
        'max': [axis0_max.tolist(), axis1_max.tolist(), flatten_list_max],
        'min':[axis0_min.tolist(), axis1_min.tolist(), flatten_list_min],
        'sum':[axis0_sum.tolist(), axis1_sum.tolist(), flatten_list_sum],
        }

        return calculations