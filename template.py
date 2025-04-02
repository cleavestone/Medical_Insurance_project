import os

def create_directories(directories):
    """Create multiple directories."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def create_files(files):
    """Create multiple files."""
    for file in files:
        with open(file, "w") as f:
            pass  # Create an empty file
        print(f"Created file: {file}")

def setup_project():
    base_dir = r"C:\Users\Hp\Desktop\Medical_Insurance_project"
    
    # Define folder structure
    directories = [
        f"{base_dir}/data/raw", f"{base_dir}/data/processed", f"{base_dir}/data/train", f"{base_dir}/data/test",
        f"{base_dir}/src/components", f"{base_dir}/src/pipelines", f"{base_dir}/src/utils",
        f"{base_dir}/models",
        f"{base_dir}/docker/scripts",
        f"{base_dir}/config/logging", f"{base_dir}/config/model",
        f"{base_dir}/tests/unit", f"{base_dir}/tests/integration",
        f"{base_dir}/docs"
    ]
    
    # Define essential files
    files = [
        f"{base_dir}/zenml_config.yaml", f"{base_dir}/mlflow_config.yaml", f"{base_dir}/docker-compose.yaml",
        f"{base_dir}/src/utils/logger.py", f"{base_dir}/src/utils/exception.py"
    ]
    
    # Create directories and files
    create_directories(directories)
    create_files(files)
    
    print("\n✅ MLOps Project Structure Set Up Successfully!")

if __name__ == "__main__":
    setup_project()
