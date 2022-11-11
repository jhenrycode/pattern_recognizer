from data_repository import get_file_data
from transformer import tranform_strings_to_floats
from extractor import get_data_window
from finder import find_closest_matching_window
from plot import print_window

MINUTES_PER_RECORD = 60

file_data = get_file_data('../data/semi_repeating_data.csv')

transformed_data = tranform_strings_to_floats(file_data)

window_to_match, search_data  = get_data_window(transformed_data, MINUTES_PER_RECORD*24, MINUTES_PER_RECORD, MINUTES_PER_RECORD*24)

matching_window, match_start_index, match_end_index = find_closest_matching_window(search_data, window_to_match)

print_window(window_to_match, './window_to_match.png')
print_window(matching_window, './matching_window.png')

future_end_index = min(match_end_index + MINUTES_PER_RECORD*24, len(search_data))
the_future = search_data[match_end_index:future_end_index]
print_window(the_future, './the_future.png')