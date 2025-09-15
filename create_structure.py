import os
from pathlib import Path

def create_directory_structure():
    # Define the directory structure
    structure = {
        "poc": {
            "services": {
                "api": ["app.py", "requirements.txt", "Dockerfile"],
                "forecast": ["app.py", "model.py", "requirements.txt", "Dockerfile"],
                "worker": ["worker.py", "requirements.txt", "Dockerfile"]
            },
            "k8s": [
                "namespace.yaml",
                "api-deployment.yaml", 
                "forecast-deployment.yaml",
                "worker-deployment.yaml",
                "redis.yaml"
            ]
        }
    }

    # Create directories and files
    for base_dir, contents in structure.items():
        if isinstance(contents, dict):
            # Handle nested directories (services)
            for service_dir, files in contents.items():
                service_path = Path(base_dir) / service_dir
                service_path.mkdir(parents=True, exist_ok=True)
                
                for file in files:
                    file_path = service_path / file
                    file_path.touch()
                    print(f"Created: {file_path}")
        
        elif isinstance(contents, list):
            # Handle flat directory with files (k8s)
            k8s_path = Path(base_dir)
            k8s_path.mkdir(parents=True, exist_ok=True)
            
            for file in contents:
                file_path = k8s_path / file
                file_path.touch()
                print(f"Created: {file_path}")

    print("\nDirectory structure created successfully!")

if __name__ == "__main__":
    create_directory_structure()