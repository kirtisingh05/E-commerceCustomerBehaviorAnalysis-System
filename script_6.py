# HDFS Simulation template
hdfs_template = """{% extends "base.html" %}

{% block content %}
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Hadoop HDFS Simulation</h1>
</div>

<div class="row">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-database me-2"></i>
                    Big Data Storage Operations
                </h5>
            </div>
            <div class="card-body">
                <p class="mb-4">Simulate Hadoop Distributed File System (HDFS) operations for storing and retrieving large-scale e-commerce transaction data.</p>
                
                <div class="row">
                    <div class="col-md-6">
                        <div class="card bg-light">
                            <div class="card-body">
                                <h6><i class="fas fa-upload me-2"></i>Store to HDFS</h6>
                                <p class="small">Upload transaction data to Hadoop Distributed File System for distributed processing.</p>
                                <button class="btn btn-primary btn-sm" onclick="performHDFSOperation('store')">
                                    <i class="fas fa-cloud-upload-alt me-1"></i>Store Data
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card bg-light">
                            <div class="card-body">
                                <h6><i class="fas fa-download me-2"></i>Retrieve from HDFS</h6>
                                <p class="small">Retrieve transaction data from HDFS for analysis and processing.</p>
                                <button class="btn btn-success btn-sm" onclick="performHDFSOperation('retrieve')">
                                    <i class="fas fa-cloud-download-alt me-1"></i>Retrieve Data
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="card mt-4">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-terminal me-2"></i>
                    Operation Log
                </h5>
            </div>
            <div class="card-body">
                <div id="operationLog" class="border p-3" style="background-color: #f8f9fa; min-height: 200px; font-family: monospace;">
                    <div class="text-muted">HDFS operations will be logged here...</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h6 class="mb-0">HDFS Architecture</h6>
            </div>
            <div class="card-body">
                <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8IS0tIE5hbWVOb2RlIC0tPgogIDxyZWN0IHg9IjEwMCIgeT0iMjAiIHdpZHRoPSIxMDAiIGhlaWdodD0iNDAiIGZpbGw9IiNmZjcwNDMiLz4KICA8dGV4dCB4PSIxNTAiIHk9IjQ1IiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTIiIGZpbGw9IndoaXRlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5OYW1lTm9kZTwvdGV4dD4KICA8IS0tIERhdGFOb2RlcyAtLT4KICA8cmVjdCB4PSIyMCIgeT0iMTAwIiB3aWR0aD0iODAiIGhlaWdodD0iNDAiIGZpbGw9IiM0Y2FmNTAiLz4KICA8dGV4dCB4PSI2MCIgeT0iMTI1IiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IndoaXRlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5EYXRhTm9kZSAxPC90ZXh0PgogIDxyZWN0IHg9IjExMCIgeT0iMTAwIiB3aWR0aD0iODAiIGhlaWdodD0iNDAiIGZpbGw9IiM0Y2FmNTAiLz4KICA8dGV4dCB4PSIxNTAiIHk9IjEyNSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEwIiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RGF0YU5vZGUgMjwvdGV4dD4KICA8cmVjdCB4PSIyMDAiIHk9IjEwMCIgd2lkdGg9IjgwIiBoZWlnaHQ9IjQwIiBmaWxsPSIjNGNhZjUwIi8+CiAgPHRleHQgeD0iMjQwIiB5PSIxMjUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkRhdGFOb2RlIDM8L3RleHQ+CiAgPCEtLSBDb25uZWN0aW9ucyAtLT4KICA8bGluZSB4MT0iMTUwIiB5MT0iNjAiIHgyPSI2MCIgeTI9IjEwMCIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8bGluZSB4MT0iMTUwIiB5MT0iNjAiIHgyPSIxNTAiIHkyPSIxMDAiIHN0cm9rZT0iIzMzMyIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPGxpbmUgeDE9IjE1MCIgeTE9IjYwIiB4Mj0iMjQwIiB5Mj0iMTAwIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMiIvPgo8L3N2Zz4=" alt="HDFS Architecture" class="img-fluid">
                <p class="small mt-2">HDFS consists of a NameNode that manages metadata and DataNodes that store actual data blocks.</p>
            </div>
        </div>
        
        <div class="card mt-3">
            <div class="card-header">
                <h6 class="mb-0">Key Features</h6>
            </div>
            <div class="card-body">
                <ul class="small">
                    <li><strong>Fault Tolerance:</strong> Data replication across nodes</li>
                    <li><strong>Scalability:</strong> Handle petabytes of data</li>
                    <li><strong>High Throughput:</strong> Optimized for batch processing</li>
                    <li><strong>Distributed:</strong> Data stored across cluster</li>
                </ul>
            </div>
        </div>
        
        <div class="card mt-3">
            <div class="card-header">
                <h6 class="mb-0">Commands Simulated</h6>
            </div>
            <div class="card-body">
                <code class="small">
                    hdfs dfs -put local_file /hdfs_path<br>
                    hdfs dfs -get /hdfs_path local_file<br>
                    hdfs dfs -ls /hdfs_path<br>
                    hdfs dfs -mkdir /hdfs_directory
                </code>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
function performHDFSOperation(operation) {
    var logDiv = $('#operationLog');
    var timestamp = new Date().toLocaleTimeString();
    
    // Add loading message
    logDiv.append('<div class="text-info">[' + timestamp + '] Starting HDFS ' + operation + ' operation...</div>');
    
    $.ajax({
        url: '/hdfs-operation',
        method: 'POST',
        data: {operation: operation},
        success: function(response) {
            logDiv.append('<div class="text-success">[' + new Date().toLocaleTimeString() + '] ' + response.message + '</div>');
            if (response.path) {
                logDiv.append('<div class="text-muted">[INFO] Path: ' + response.path + '</div>');
            }
            if (response.size) {
                logDiv.append('<div class="text-muted">[INFO] Size: ' + response.size + '</div>');
            }
        },
        error: function(xhr) {
            logDiv.append('<div class="text-danger">[' + new Date().toLocaleTimeString() + '] Error: ' + xhr.responseJSON.error + '</div>');
        }
    });
}

$(document).ready(function() {
    // Welcome message
    var logDiv = $('#operationLog');
    logDiv.html('<div class="text-muted">[SYSTEM] HDFS Simulation Ready</div>');
    logDiv.append('<div class="text-muted">[SYSTEM] Click buttons above to simulate HDFS operations</div>');
});
</script>
{% endblock %}"""

# About template
about_template = """{% extends "base.html" %}

{% block content %}
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">About This Project</h1>
</div>

<div class="row">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-info-circle me-2"></i>
                    E-commerce Customer Behavior Analysis System
                </h5>
            </div>
            <div class="card-body">
                <p>This comprehensive system demonstrates <strong>Big Data Mining</strong> techniques for analyzing e-commerce customer behavior using advanced algorithms and modern web technologies.</p>
                
                <h6 class="mt-4">Key Features:</h6>
                <div class="row">
                    <div class="col-md-6">
                        <ul>
                            <li><strong>Market Basket Analysis</strong> using Apriori and FP-Growth algorithms</li>
                            <li><strong>Association Rules Mining</strong> to discover buying patterns</li>
                            <li><strong>Interactive Visualizations</strong> with Plotly.js</li>
                            <li><strong>Customer Behavior Analytics</strong></li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <ul>
                            <li><strong>HDFS Integration Simulation</strong> for big data storage</li>
                            <li><strong>Real-time Analysis</strong> with configurable parameters</li>
                            <li><strong>Responsive Web Interface</strong> with Bootstrap</li>
                            <li><strong>Educational Content</strong> explaining concepts</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="card mt-4">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-cogs me-2"></i>
                    Technical Implementation
                </h5>
            </div>
            <div class="card-body">
                <h6>Algorithms Implemented:</h6>
                <div class="row">
                    <div class="col-md-6">
                        <div class="card bg-light">
                            <div class="card-body">
                                <h6 class="card-title"><i class="fas fa-list me-2"></i>Apriori Algorithm</h6>
                                <p class="small card-text">
                                    A classic algorithm for frequent item set mining that uses a bottom-up approach. 
                                    It generates candidate itemsets and uses the downward closure property to prune the search space.
                                </p>
                                <p class="small"><strong>Time Complexity:</strong> O(2^n) in worst case</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card bg-light">
                            <div class="card-body">
                                <h6 class="card-title"><i class="fas fa-tree me-2"></i>FP-Growth Algorithm</h6>
                                <p class="small card-text">
                                    An efficient algorithm that uses a compact tree structure (FP-tree) to represent the database 
                                    and mine frequent patterns without generating candidate itemsets.
                                </p>
                                <p class="small"><strong>Time Complexity:</strong> O(n^2) typically faster than Apriori</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <h6 class="mt-4">Technology Stack:</h6>
                <div class="table-responsive">
                    <table class="table table-sm">
                        <thead>
                            <tr>
                                <th>Component</th>
                                <th>Technology</th>
                                <th>Purpose</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Backend Framework</td>
                                <td>Python Flask</td>
                                <td>Web application server and API</td>
                            </tr>
                            <tr>
                                <td>Data Mining</td>
                                <td>MLxtend Library</td>
                                <td>Apriori and FP-Growth implementation</td>
                            </tr>
                            <tr>
                                <td>Data Processing</td>
                                <td>Pandas & NumPy</td>
                                <td>Data manipulation and analysis</td>
                            </tr>
                            <tr>
                                <td>Visualizations</td>
                                <td>Plotly.js</td>
                                <td>Interactive charts and graphs</td>
                            </tr>
                            <tr>
                                <td>Frontend</td>
                                <td>Bootstrap 5 + JavaScript</td>
                                <td>Responsive UI and user interactions</td>
                            </tr>
                            <tr>
                                <td>Big Data Simulation</td>
                                <td>Python subprocess</td>
                                <td>HDFS operations simulation</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h6 class="mb-0">Project Statistics</h6>
            </div>
            <div class="card-body">
                <ul class="list-unstyled">
                    <li><strong>Lines of Code:</strong> 1000+</li>
                    <li><strong>HTML Templates:</strong> 7</li>
                    <li><strong>Python Modules:</strong> 2</li>
                    <li><strong>JavaScript Functions:</strong> 15+</li>
                    <li><strong>CSS Styles:</strong> Custom responsive design</li>
                </ul>
            </div>
        </div>
        
        <div class="card mt-3">
            <div class="card-header">
                <h6 class="mb-0">Educational Value</h6>
            </div>
            <div class="card-body">
                <p class="small">This project demonstrates:</p>
                <ul class="small">
                    <li>Data mining concepts in practice</li>
                    <li>Big data processing simulation</li>
                    <li>Web application development</li>
                    <li>Algorithm comparison and analysis</li>
                    <li>Business intelligence applications</li>
                </ul>
            </div>
        </div>
        
        <div class="card mt-3">
            <div class="card-header">
                <h6 class="mb-0">Use Cases</h6>
            </div>
            <div class="card-body">
                <ul class="small">
                    <li><strong>Retail:</strong> Product recommendation systems</li>
                    <li><strong>E-commerce:</strong> Cross-selling strategies</li>
                    <li><strong>Marketing:</strong> Customer segmentation</li>
                    <li><strong>Inventory:</strong> Stock optimization</li>
                    <li><strong>Research:</strong> Consumer behavior studies</li>
                </ul>
            </div>
        </div>
        
        <div class="card mt-3">
            <div class="card-header">
                <h6 class="mb-0">Metrics Explained</h6>
            </div>
            <div class="card-body">
                <div class="small">
                    <p><strong>Support:</strong> Frequency of itemset occurrence</p>
                    <p><strong>Confidence:</strong> Conditional probability of rules</p>
                    <p><strong>Lift:</strong> Strength of association between items</p>
                    <p class="text-muted">Higher values indicate stronger patterns</p>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-lightbulb me-2"></i>
                    Business Applications
                </h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-3">
                        <div class="text-center">
                            <i class="fas fa-shopping-cart fa-2x text-primary mb-2"></i>
                            <h6>Product Recommendations</h6>
                            <p class="small">Suggest complementary products based on purchase history</p>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="text-center">
                            <i class="fas fa-store fa-2x text-success mb-2"></i>
                            <h6>Store Layout Optimization</h6>
                            <p class="small">Position frequently bought items together for increased sales</p>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="text-center">
                            <i class="fas fa-tags fa-2x text-warning mb-2"></i>
                            <h6>Promotional Strategies</h6>
                            <p class="small">Create bundle offers and targeted promotions</p>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="text-center">
                            <i class="fas fa-chart-line fa-2x text-info mb-2"></i>
                            <h6>Inventory Management</h6>
                            <p class="small">Optimize stock levels based on buying patterns</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}"""

# Write the final templates
with open('templates/hdfs.html', 'w') as f:
    f.write(hdfs_template)

with open('templates/about.html', 'w') as f:
    f.write(about_template)

# Create requirements.txt
requirements = """Flask==3.1.2
pandas>=2.0.0
numpy>=1.20.0
mlxtend>=0.23.0
plotly>=5.0.0
scikit-learn>=1.0.0"""

with open('requirements.txt', 'w') as f:
    f.write(requirements)

print("Final templates and requirements.txt created successfully!")