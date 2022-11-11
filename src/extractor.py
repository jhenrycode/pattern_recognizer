
def get_data_window(transformed_data, window_size_minutes, minutes_per_record, window_minutes_offest_from_end):

    window_record_count = int(window_size_minutes / minutes_per_record)
    window_start_record_offset = int(window_minutes_offest_from_end / minutes_per_record)
    start_record_index = int(len(transformed_data) - window_start_record_offset)
    end_index = int(start_record_index + window_record_count)

    window = transformed_data[start_record_index:end_index]

    search_data = transformed_data[0:start_record_index] + transformed_data[end_index:-1]

    return window, search_data