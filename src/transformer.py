import numpy as np

def tranform_strings_to_floats(input_data):

    np_array = np.array(input_data)

    label_data = np_array[:,0]
    value_data = np_array[:,1].astype(float)

    return_value = zip(label_data, value_data)

    return list(return_value)