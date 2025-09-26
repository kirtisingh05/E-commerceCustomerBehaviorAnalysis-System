#!/usr/bin/env python3
"""
E-commerce Customer Behavior Analysis System
Run script for easy application startup
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if required packages are installed"""
    required_packages = ['flask', 'pandas', 'mlxtend', 'plotly', 'numpy']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("📦 Installing missing packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
    else:
        print("✅ All required packages are already installed!")

def main():
    print("🚀 Starting E-commerce Customer Behavior Analysis System")
    print("=" * 60)

    # Check requirements
    check_requirements()

    # Check if dataset exists
    if os.path.exists('ecommerce_transactions.csv'):
        print("✅ Sample dataset found")
    else:
        print("⚠️  Sample dataset not found - will be created on first run")

    print("🌐 Starting Flask application...")
    print("📊 Open your browser and navigate to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 60)

    # Start the Flask app
    os.system('python app.py')

if __name__ == "__main__":
    main()
