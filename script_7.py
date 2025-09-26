# Create comprehensive README.md
readme_content = """# E-commerce Customer Behavior Analysis System

A comprehensive web-based system for analyzing e-commerce customer behavior using **Big Data Mining** techniques, implementing **Apriori** and **FP-Growth** algorithms for Market Basket Analysis.

## 🚀 Features

### Core Functionality
- **Market Basket Analysis** using industry-standard algorithms
- **Apriori Algorithm** implementation with configurable parameters
- **FP-Growth Algorithm** for efficient frequent pattern mining
- **Association Rules Mining** to discover buying patterns
- **Interactive Web Interface** with real-time analysis

### Big Data Integration
- **Hadoop HDFS Simulation** for distributed data storage
- **Scalable Data Processing** pipeline
- **MapReduce** workflow simulation
- **Big Data concepts** demonstration

### Visualization & Analytics
- **Interactive Charts** using Plotly.js
- **Customer Behavior Dashboard**
- **Real-time Analysis Results**
- **Business Intelligence Metrics**

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Web browser (Chrome, Firefox, Safari, etc.)

## 🛠️ Installation

1. **Clone or Download** the project files to your local directory

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**:
   ```bash
   python -c "import flask, mlxtend, pandas, plotly; print('All packages installed successfully!')"
   ```

## 🎯 Quick Start

1. **Start the Application**:
   ```bash
   python app.py
   ```
   
2. **Open Your Browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Follow the Workflow**:
   - Click "Get Started" on the home page
   - Load the sample dataset
   - Explore data analysis
   - Run market basket analysis
   - View visualizations

## 📊 Project Structure

```
ecommerce-analysis/
├── app.py                  # Main Flask application
├── market_analysis.py      # Market basket analysis algorithms
├── requirements.txt        # Python dependencies
├── ecommerce_transactions.csv  # Sample dataset
├── templates/              # HTML templates
│   ├── base.html          # Base template with navigation
│   ├── index.html         # Home page
│   ├── upload.html        # Dataset loading
│   ├── analysis.html      # Data analysis dashboard
│   ├── market_basket.html # Algorithm interface
│   ├── visualizations.html # Interactive charts
│   ├── hdfs.html          # Big data simulation
│   └── about.html         # Technical documentation
└── static/                # CSS, JS, and assets (auto-created)
```

## 🔬 Technical Implementation

### Algorithms

#### Apriori Algorithm
- **Principle**: Uses downward closure property
- **Approach**: Bottom-up frequent itemset generation
- **Time Complexity**: O(2^n) worst case
- **Use Case**: Educational and small to medium datasets

#### FP-Growth Algorithm
- **Principle**: Frequent Pattern tree structure
- **Approach**: Divide and conquer without candidate generation
- **Time Complexity**: O(n^2) typically faster than Apriori
- **Use Case**: Large datasets and production environments

### Key Metrics

- **Support**: `support(A) = |T(A)| / |T|`
- **Confidence**: `confidence(A→B) = support(A∪B) / support(A)`
- **Lift**: `lift(A→B) = confidence(A→B) / support(B)`

Where:
- `|T(A)|` = transactions containing itemset A
- `|T|` = total number of transactions

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python Flask | Web server and REST API |
| **Data Mining** | MLxtend | Algorithm implementation |
| **Data Processing** | Pandas, NumPy | Data manipulation |
| **Visualization** | Plotly.js | Interactive charts |
| **Frontend** | Bootstrap 5 | Responsive UI design |
| **Big Data** | Python subprocess | HDFS simulation |

## 📈 Usage Guide

### 1. Data Loading
- The system includes a pre-generated sample dataset
- Contains realistic e-commerce transactions with product associations
- Supports CSV format with required columns

### 2. Data Analysis
- View comprehensive statistics
- Analyze customer behavior patterns
- Explore product popularity and trends

### 3. Market Basket Analysis
- Configure algorithm parameters:
  - **Minimum Support**: 0.001 to 1.0 (default: 0.01)
  - **Minimum Confidence**: 0.01 to 1.0 (default: 0.1)
  - **Minimum Lift**: 0.1+ (default: 1.0)
- Compare Apriori vs FP-Growth performance
- Analyze association rules

### 4. Visualizations
- Interactive bar charts for product frequency
- Scatter plots for rule analysis
- Geographic distribution charts
- Time series trends

### 5. HDFS Simulation
- Simulate big data storage operations
- Understand distributed file system concepts
- Practice Hadoop command-line operations

## 🎓 Educational Content

### Concepts Covered
1. **Frequent Pattern Mining**
2. **Association Rule Learning**
3. **Big Data Processing**
4. **Distributed Computing**
5. **Web Application Development**

### Learning Outcomes
- Understand market basket analysis principles
- Compare different mining algorithms
- Apply big data concepts
- Develop full-stack applications
- Analyze business intelligence metrics

## 🔧 Configuration

### Algorithm Parameters

#### Support Threshold
- **Low values (0.001-0.01)**: Find rare but potentially valuable patterns
- **Medium values (0.01-0.1)**: Balanced approach for most use cases
- **High values (0.1+)**: Only very common patterns

#### Confidence Threshold
- **Low values (0.1-0.3)**: Exploratory analysis
- **Medium values (0.3-0.7)**: Business insights
- **High values (0.7+)**: Strong associations only

#### Lift Threshold
- **Lift = 1**: No correlation
- **Lift > 1**: Positive correlation (recommended)
- **Lift < 1**: Negative correlation

## 📊 Sample Dataset

The included dataset contains:
- **13,000+ transactions** across multiple customers
- **26 different products** including electronics, accessories, and office supplies
- **Realistic associations** like "Laptop + Mouse + Keyboard"
- **Geographic distribution** across multiple countries
- **Time-based patterns** spanning over a year

## 🚀 Deployment

### Local Development
```bash
# Clone the project
git clone <repository-url>
cd ecommerce-analysis

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Production Deployment
For production deployment, consider:
- Using WSGI server like Gunicorn
- Configuring reverse proxy (Nginx)
- Setting up environment variables
- Implementing proper logging
- Adding database backend for persistence

## 🛡️ Best Practices

### Performance Optimization
- Use appropriate support thresholds
- Consider FP-Growth for large datasets
- Implement data sampling for very large datasets
- Cache frequent computation results

### Data Quality
- Clean transaction data before analysis
- Remove cancelled transactions
- Handle missing values appropriately
- Validate data consistency

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is created for educational purposes. Feel free to use and modify for learning and non-commercial purposes.

## 🆘 Troubleshooting

### Common Issues

#### Module Not Found Error
```bash
pip install -r requirements.txt
```

#### Port Already in Use
```bash
# Change port in app.py or kill existing process
lsof -ti:5000 | xargs kill
```

#### Memory Issues with Large Datasets
- Reduce dataset size
- Increase minimum support threshold
- Use data sampling techniques

### Getting Help
1. Check the About page for technical details
2. Review algorithm parameters
3. Ensure all dependencies are installed
4. Verify Python version compatibility

## 🏆 Project Highlights

- **Complete Implementation** of both major MBA algorithms
- **Educational Focus** with detailed explanations
- **Industry-Standard Libraries** and best practices
- **Interactive Interface** for hands-on learning
- **Big Data Concepts** integration
- **Professional UI/UX** design
- **Comprehensive Documentation**

---

**Built with ❤️ for learning Big Data Mining and Web Development**

*This project demonstrates practical implementation of data mining concepts in a modern web application, perfect for students and professionals learning about customer behavior analysis and big data processing.*
"""

# Create run script for easier startup
run_script = """#!/usr/bin/env python3
\"\"\"
E-commerce Customer Behavior Analysis System
Run script for easy application startup
\"\"\"

import os
import sys
import subprocess

def check_requirements():
    \"\"\"Check if required packages are installed\"\"\"
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
"""

# Write files
with open('README.md', 'w') as f:
    f.write(readme_content)

with open('run.py', 'w') as f:
    f.write(run_script)

# Make run script executable (for Unix systems)
import stat
os.chmod('run.py', stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)

print("README.md and run.py created successfully!")
print("\n" + "="*60)
print("🎉 PROJECT SETUP COMPLETE!")
print("="*60)
print("\nTo start the application:")
print("1. Option 1: python run.py")
print("2. Option 2: python app.py") 
print("\nThen open http://localhost:5000 in your browser")
print("\n📚 Check README.md for detailed documentation")