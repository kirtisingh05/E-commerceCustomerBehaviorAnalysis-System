# Create the templates directory and HTML files
import os

# Create templates directory
os.makedirs('templates', exist_ok=True)
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)

# Base template
base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}E-commerce Customer Behavior Analysis{% endblock %}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- Plotly -->
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
    <style>
        .sidebar {
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .sidebar a {
            color: white;
            text-decoration: none;
            padding: 10px 15px;
            display: block;
            transition: background-color 0.3s;
        }
        .sidebar a:hover {
            background-color: rgba(255,255,255,0.1);
            color: white;
        }
        .main-content {
            padding: 20px;
        }
        .card {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border: none;
            margin-bottom: 20px;
        }
        .stats-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }
        .rules-table {
            font-size: 0.9em;
        }
        .algorithm-card {
            border-left: 4px solid #007bff;
        }
        .footer {
            background-color: #343a40;
            color: white;
            padding: 20px 0;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <!-- Sidebar -->
            <nav class="col-md-2 d-none d-md-block sidebar">
                <div class="sidebar-sticky pt-3">
                    <h4 class="px-3 mb-4">
                        <i class="fas fa-chart-line me-2"></i>
                        MBA System
                    </h4>
                    
                    <ul class="nav flex-column">
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('index') }}">
                                <i class="fas fa-home me-2"></i>
                                Home
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('upload_data') }}">
                                <i class="fas fa-upload me-2"></i>
                                Load Dataset
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('analysis') }}">
                                <i class="fas fa-analytics me-2"></i>
                                Data Analysis
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('market_basket') }}">
                                <i class="fas fa-shopping-basket me-2"></i>
                                Market Basket Analysis
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('visualizations') }}">
                                <i class="fas fa-chart-bar me-2"></i>
                                Visualizations
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('hdfs_simulation') }}">
                                <i class="fas fa-database me-2"></i>
                                HDFS Simulation
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{{ url_for('about') }}">
                                <i class="fas fa-info-circle me-2"></i>
                                About
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>

            <!-- Main content -->
            <main class="col-md-10 ms-sm-auto px-md-4">
                <div class="main-content">
                    <!-- Flash messages -->
                    {% with messages = get_flashed_messages(with_categories=true) %}
                        {% if messages %}
                            {% for category, message in messages %}
                                <div class="alert alert-{{ 'danger' if category == 'error' else category }} alert-dismissible fade show" role="alert">
                                    {{ message }}
                                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                                </div>
                            {% endfor %}
                        {% endif %}
                    {% endwith %}
                    
                    {% block content %}{% endblock %}
                </div>
            </main>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer text-center">
        <div class="container">
            <p>&copy; 2024 E-commerce Customer Behavior Analysis System. Built with Flask & Python.</p>
            <p class="small">Implementing Apriori & FP-Growth Algorithms for Market Basket Analysis</p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    
    {% block scripts %}{% endblock %}
</body>
</html>"""

# Index template
index_template = """{% extends "base.html" %}

{% block content %}
<div class="jumbotron bg-primary text-white p-5 rounded mb-4">
    <div class="container">
        <h1 class="display-4">E-commerce Customer Behavior Analysis</h1>
        <p class="lead">Comprehensive Market Basket Analysis using Big Data Mining Techniques</p>
        <hr class="my-4">
        <p>Discover hidden patterns in customer purchasing behavior using advanced data mining algorithms including Apriori and FP-Growth.</p>
        <a class="btn btn-light btn-lg" href="{{ url_for('upload_data') }}" role="button">
            <i class="fas fa-play me-2"></i>Get Started
        </a>
    </div>
</div>

<div class="row">
    <div class="col-md-4">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">
                    <i class="fas fa-algorithm text-primary me-2"></i>
                    Advanced Algorithms
                </h5>
                <p class="card-text">Implement both Apriori and FP-Growth algorithms for frequent pattern mining and association rule generation.</p>
                <ul class="list-unstyled">
                    <li><i class="fas fa-check text-success me-2"></i>Apriori Algorithm</li>
                    <li><i class="fas fa-check text-success me-2"></i>FP-Growth Algorithm</li>
                    <li><i class="fas fa-check text-success me-2"></i>Association Rules</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="col-md-4">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">
                    <i class="fas fa-database text-success me-2"></i>
                    Big Data Integration
                </h5>
                <p class="card-text">Simulate Hadoop HDFS operations for storing and retrieving large-scale e-commerce transaction data.</p>
                <ul class="list-unstyled">
                    <li><i class="fas fa-check text-success me-2"></i>HDFS Simulation</li>
                    <li><i class="fas fa-check text-success me-2"></i>Scalable Processing</li>
                    <li><i class="fas fa-check text-success me-2"></i>Data Pipeline</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="col-md-4">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">
                    <i class="fas fa-chart-line text-warning me-2"></i>
                    Interactive Visualizations
                </h5>
                <p class="card-text">Rich visualizations and dashboards to understand customer behavior patterns and business insights.</p>
                <ul class="list-unstyled">
                    <li><i class="fas fa-check text-success me-2"></i>Interactive Charts</li>
                    <li><i class="fas fa-check text-success me-2"></i>Real-time Analytics</li>
                    <li><i class="fas fa-check text-success me-2"></i>Business Intelligence</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-12">
        <div class="card">
            <div class="card-header bg-dark text-white">
                <h5 class="mb-0">
                    <i class="fas fa-info-circle me-2"></i>
                    Project Features
                </h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <h6>Data Mining Techniques:</h6>
                        <ul>
                            <li>Frequent Pattern Mining</li>
                            <li>Association Rules Discovery</li>
                            <li>Support, Confidence, and Lift Metrics</li>
                            <li>Customer Segmentation</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h6>Technology Stack:</h6>
                        <ul>
                            <li>Python Flask Framework</li>
                            <li>MLxtend Library for Mining</li>
                            <li>Plotly for Visualizations</li>
                            <li>Bootstrap for UI/UX</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}"""

# Upload template
upload_template = """{% extends "base.html" %}

{% block content %}
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Load Dataset</h1>
</div>

<div class="row">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-upload me-2"></i>
                    Dataset Loading
                </h5>
            </div>
            <div class="card-body">
                <form method="POST" class="mb-3">
                    <div class="mb-3">
                        <label class="form-label">E-commerce Transaction Data</label>
                        <p class="text-muted">This demo uses a pre-generated sample dataset with realistic e-commerce transactions.</p>
                        <div class="alert alert-info">
                            <i class="fas fa-info-circle me-2"></i>
                            The sample dataset contains transactions with products like laptops, smartphones, accessories, and office supplies with realistic buying patterns.
                        </div>
                    </div>
                    
                    <button type="submit" class="btn btn-primary">
                        <i class="fas fa-database me-2"></i>
                        Load Sample Dataset
                    </button>
                </form>
            </div>
        </div>
    </div>
    
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h6 class="mb-0">Dataset Requirements</h6>
            </div>
            <div class="card-body">
                <p class="small">The dataset should contain the following columns:</p>
                <ul class="small">
                    <li><strong>InvoiceNo:</strong> Transaction ID</li>
                    <li><strong>StockCode:</strong> Product code</li>
                    <li><strong>Description:</strong> Product name</li>
                    <li><strong>Quantity:</strong> Items purchased</li>
                    <li><strong>InvoiceDate:</strong> Transaction date</li>
                    <li><strong>UnitPrice:</strong> Price per unit</li>
                    <li><strong>CustomerID:</strong> Customer identifier</li>
                    <li><strong>Country:</strong> Customer location</li>
                </ul>
            </div>
        </div>
        
        <div class="card mt-3">
            <div class="card-header">
                <h6 class="mb-0">HDFS Integration</h6>
            </div>
            <div class="card-body">
                <p class="small">Once loaded, the dataset can be:</p>
                <ul class="small">
                    <li>Stored in Hadoop HDFS</li>
                    <li>Processed using MapReduce</li>
                    <li>Analyzed with Spark</li>
                    <li>Visualized in real-time</li>
                </ul>
            </div>
        </div>
    </div>
</div>
{% endblock %}"""

# Write the templates
with open('templates/base.html', 'w') as f:
    f.write(base_template)

with open('templates/index.html', 'w') as f:
    f.write(index_template)

with open('templates/upload.html', 'w') as f:
    f.write(upload_template)

print("Base templates created successfully!")