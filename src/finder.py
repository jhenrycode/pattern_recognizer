import numpy as np
import stumpy as stmp

def find_closest_matching_window(search_data, window_to_match):

    pattern_to_find = np.array(window_to_match)[:,1].astype(float)
    values_to_search = np.array(search_data)[:,1].astype(float)

    pattern_length = len(pattern_to_find)

    matrix_profile = stmp.stump(T_A=pattern_to_find, m=pattern_length, T_B=values_to_search, ignore_trivial=False, normalize=True)

    match_start_index = matrix_profile[0][1]
    match_end_index = match_start_index + pattern_length

    matching_window = search_data[match_start_index:match_end_index]

    return matching_window, match_start_index, match_end_index