import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


import csv

def fix_csv_columns(input_file, output_file, number_of_column_I_want):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)
            data = [row for row in reader]

            # Detect the number of columns in the CSV file
            num_columns = len(data[0])

            # Check if the number of columns is not 6
            if num_columns != number_of_column_I_want:
                # Split and reformat the data
                for i in range(len(data)):
                    row = data[i]
                    if len(row) == 1:
                        # Split the single column using semicolon as the delimiter
                        row = row[0].split(';')
                        # Pad the row with empty strings to ensure it has 6 columns
                        row += [''] * (number_of_column_I_want - len(row))
                    data[i] = row

                # Write the corrected data to the output file
                with open(output_file, 'w', newline='') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerows(data)
                print(f'File {input_file} has been corrected and saved as {output_file}')
            else:
                print(f'File {input_file} already has {number_of_column_I_want} columns and does not need modification.')

    except FileNotFoundError:
        print(f'File {input_file} not found.')
        
        
#modify the incorrect data(from incorrect column nuber to correct column number)
data_folder = '/data_sata/VED_Group/VED_Group/ljy/Remaing_Useful_Life/PHM/Raw_data_docker'
for root, dirs, files in os.walk(data_folder):
    for file in files:
        if file.startswith('acc') and file.endswith('csv'):
            filepath = os.path.join(root, file)
            fix_csv_columns(filepath, filepath, 6)
        elif file.startswith('temp') and file.endswith('csv'):
            filepath = os.path.join(root, file)
            fix_csv_columns(filepath, filepath, 5)
            
    
