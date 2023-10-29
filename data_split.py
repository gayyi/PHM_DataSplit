import os
import pandas as pd

# Function to check if a file is a CSV file
def is_csv_file(filename):
    return filename.lower().endswith('.csv')

# Function to split data into packets and save them
import os
import pandas as pd

def split_and_save_data(df, output_dir, output_file_prefix):
    num_packets = len(df) // 1024
    for i in range(num_packets):
        start_idx = i * 1024
        end_idx = (i + 1) * 1024
        packet_data_time = df.iloc[start_idx:end_idx, :3]
        packet_data_hori = df.iloc[start_idx:end_idx, 4]
        packet_data_vert = df.iloc[start_idx:end_idx, 5]
        merged_hori = pd.concat([packet_data_time, packet_data_hori], axis=1)
        merged_vert = pd.concat([packet_data_time, packet_data_vert], axis=1)

        if 'ChannelSet1' in output_dir:
            set_data = merged_hori
        elif 'ChannelSet2' in output_dir:
            set_data = merged_vert

        # 构建保存文件的路径
        output_file_path = os.path.join(output_dir, f'{output_file_prefix}_packet_{i}.py')

        if os.path.exists(output_file_path):
            # 如果文件存在，以追加模式打开文件并追加数据包
            with open(output_file_path, "a") as file:
                file.write(f'data_{output_file_prefix}_packet_{i} = {set_data.to_dict(orient="list")}\n')
        else:
            # 如果文件不存在，创建文件并写入数据包
            with open(output_file_path, 'w') as file:
                file.write(f'data_{output_file_prefix}_packet_{i} = {set_data.to_dict(orient="list")}\n')

        

# Define the base directory and output directory
base_directory = r"/data_sata/VED_Group/VED_Group/ljy/Remaing_Useful_Life/PHM/Raw_data_docker"
output_directory = r'/data_sata/VED_Group/VED_Group/ljy/Remaing_Useful_Life/PHM/Split_data_docker'  

# Create output directories for each working condition and channel set
for condition in ['WorkingCondition1', 'WorkingCondition2', 'WorkingCondition3']:
    for channel_set in ['ChannelSet1', 'ChannelSet2']:
        os.makedirs(os.path.join(output_directory, condition, channel_set), exist_ok=True)

# Process and organize data for each subset (subset1 and subset2)
subset_dir = os.path.join(base_directory, 'Full_Test_Set')

# Iterate through the CSV files in each working condition directory
for root, dirs, files in os.walk(subset_dir):
    for dir in dirs:
        if dir.startswith('Bearing1') or dir.startswith('Bearing2') or dir.startswith('Bearing3'):
            working_condition_path = os.path.join(subset_dir, dir)
            # Read the subdirectories in the working condition
            for dirpath, csvdirs, filenames in os.walk(working_condition_path):
                for file in filenames:
                
                    if file.endswith('.csv') & file.startswith('acc'):
                        # Retrieve CSV files in the current directory
                        csv_files = [os.path.join(dirpath, file) for file in filenames if is_csv_file(file)]

                        # Process and organize data for each working condition and channel set
                        
        if dir.startswith('Bearing1'):
            #try:
            print("############## Bearing1 start ##############", dir)
            for i in range (2):
                #print("channel_start, channel_end:",channel_start, channel_end)
                split_and_save_data(pd.concat([pd.read_csv(csv) for csv in csv_files]),
                                    os.path.join(output_directory, 'WorkingCondition1', f'ChannelSet{i+1}'),
                                    f'Acceleration_Set{i+1}_Condition1')
            #except FileNotFoundError: os.path.exist(output_path, exitst_ok= True)
                #print({os.path.join(output_directory, 'WorkingCondition1', f'ChannelSet{channel_start + 1}'),
                                    #f'Acceleration_Set{channel_start + 1}_Condition1'})
        elif dir.startswith('Bearing2'):
            print("############## Bearing2 start ##############", dir)
            for i in range(2):
                split_and_save_data(pd.concat([pd.read_csv(csv) for csv in csv_files]),
                                    os.path.join(output_directory, 'WorkingCondition2', f'ChannelSet{i + 1}'),
                                    f'Acceleration_Set{i + 1}_Condition2')
        elif dir.startswith('Bearing3'):
            print("############## Bearing3 start start ##############", dir)
            for i in range(2):
                split_and_save_data(pd.concat([pd.read_csv(csv) for csv in csv_files]),
                                    os.path.join(output_directory, 'WorkingCondition3', f'ChannelSet{i + 1}'),
                                    f'Acceleration_Set{i + 1}_Condition3')
    
    print("############## over ##############")