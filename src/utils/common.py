import yaml
import os

def load_yaml():
    yaml_file_path=r"C:\Users\Hp\Desktop\Medical_Insurance_project\src\config.yaml"
    with open(yaml_file_path, 'r') as file:
      data = yaml.safe_load(file)
    return data

def create_folder(path):
    if isinstance(path, list):  # Check if path is a list
        for dirs in path:
            os.makedirs(dirs, exist_ok=True)  # Create each directory in the list
    else:
        os.makedirs(path, exist_ok=True)  # Create the single directory
