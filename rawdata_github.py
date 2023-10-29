import subprocess

# Define the GitHub repository URL
repository_url = "https://github.com/Lucky-Loek/ieee-phm-2012-data-challenge-dataset.git"

# Define the local path where you want to store the data
local_path = "/data_sata/VED_Group/VED_Group/ljy/Remaing_Useful_Life/PHM/Raw_data_docker"

# Use the git clone command to download the data
try:
    subprocess.run(["git", "clone", repository_url, local_path], check=True)
    print("Data downloaded successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
