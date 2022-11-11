import numpy as np
import matplotlib.pyplot as plt
from data_repository import get_file_data

def print_all_data():
    data = get_file_data('../data/semi_repeating_data.csv')

    np_array = np.array(data)

    labels = np_array[:,0]
    values = np_array[:,1].astype(float)

    plt.figure(figsize=(20, 10))
    plt.plot(values, label='values')
    plt.show()

def print_window(window_data, file_name):
    values = np.array(window_data)[:,1].astype(float)

    plt.figure(figsize=(20, 10))
    plt.plot(values, label='values')
    plt.savefig(file_name)