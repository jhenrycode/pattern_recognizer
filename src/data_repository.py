import csv
import os
import json
import glob
import datetime

def get_file_data(file_path, skip_first=True):
    
    rows = []
    with open(file_path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        if(skip_first):
            try:
                next(reader)
            except StopIteration:
                return rows

        for row in reader:
            rows.append(row)

    return rows
