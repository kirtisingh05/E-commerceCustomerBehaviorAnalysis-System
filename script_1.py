# Install required packages for our Flask app
import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

# Install required packages
packages = [
    'flask',
    'mlxtend',
    'plotly',
    'pandas',
    'numpy'
]

for package in packages:
    try:
        __import__(package)
        print(f"{package} is already installed")
    except ImportError:
        print(f"Installing {package}...")
        install_package(package)

print("All packages are ready!")