# Analysis template
analysis_template = """{% extends "base.html" %}

{% block content %}
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Data Analysis Dashboard</h1>
</div>

<!-- Statistics Cards -->
<div class="row mb-4">
    <div class="col-md-3">
        <div class="card stats-card">
            <div class="card-body text-center">
                <i class="fas fa-receipt fa-2x mb-2"></i>
                <h3>{{ "{:,}".format(total_transactions) }}</h3>
                <p>Total Transactions</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card stats-card">
            <div class="card-body text-center">
                <i class="fas fa-users fa-2x mb-2"></i>
                <h3>{{ "{:,}".format(total_customers) }}</h3>
                <p>Unique Customers</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card stats-card">
            <div class="card-body text-center">
                <i class="fas fa-box fa-2x mb-2"></i>
                <h3>{{ total_products }}</h3>
                <p>Products</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card stats-card">
            <div class="card-body text-center">
                <i class="fas fa-calendar fa-2x mb-2"></i>
                <p class="small mb-1">Date Range</p>
                <p class="small">{{ date_range }}</p>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-star me-2"></i>
                    Top 10 Products
                </h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-sm">
                        <thead>
                            <tr>
                                <th>Product</th>
                                <th>Frequency</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for product, count in top_items.items() %}
                            <tr>
                                <td>{{ product }}</td>
                                <td><span class="badge bg-primary">{{ count }}</span></td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-globe me-2"></i>
                    Top Countries
                </h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-sm">
                        <thead>
                            <tr>
                                <th>Country</th>
                                <th>Orders</th>
                                <th>Customers</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for country, stats in insights.country_stats.head(10).iterrows() %}
                            <tr>
                                <td>{{ country }}</td>
                                <td>{{ stats.InvoiceNo }}</td>
                                <td>{{ stats.CustomerID }}</td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
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
                    <i class="fas fa-chart-bar me-2"></i>
                    Customer Behavior Statistics
                </h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <h6>Average Customer Metrics:</h6>
                        <ul class="list-unstyled">
                            <li><strong>Orders per Customer:</strong> {{ "%.2f"|format(insights.customer_stats.loc['mean', 'Total_Orders']) }}</li>
                            <li><strong>Items per Customer:</strong> {{ "%.2f"|format(insights.customer_stats.loc['mean', 'Total_Items']) }}</li>
                            <li><strong>Average Order Value:</strong> ${{ "%.2f"|format(insights.customer_stats.loc['mean', 'Avg_Price']) }}</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h6>Customer Distribution:</h6>
                        <ul class="list-unstyled">
                            <li><strong>Max Orders by Customer:</strong> {{ "%.0f"|format(insights.customer_stats.loc['max', 'Total_Orders']) }}</li>
                            <li><strong>Standard Deviation:</strong> {{ "%.2f"|format(insights.customer_stats.loc['std', 'Total_Orders']) }}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-12">
        <div class="alert alert-success">
            <i class="fas fa-check-circle me-2"></i>
            Data analysis completed successfully! You can now proceed to 
            <a href="{{ url_for('market_basket') }}" class="alert-link">Market Basket Analysis</a> 
            to discover buying patterns and association rules.
        </div>
    </div>
</div>
{% endblock %}"""

# Market Basket Analysis template
market_basket_template = """{% extends "base.html" %}

{% block content %}
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Market Basket Analysis</h1>
</div>

<div class="row">
    <div class="col-md-6">
        <div class="card algorithm-card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-cogs me-2"></i>
                    Apriori Algorithm
                </h5>
            </div>
            <div class="card-body">
                <p class="card-text">The Apriori algorithm uses a bottom-up approach where frequent subsets are extended one item at a time.</p>
                
                <form id="aprioriForm">
                    <div class="row">
                        <div class="col-md-4">
                            <div class="mb-3">
                                <label class="form-label">Min Support</label>
                                <input type="number" class="form-control form-control-sm" name="min_support" value="0.01" step="0.001" min="0.001" max="1">
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="mb-3">
                                <label class="form-label">Min Confidence</label>
                                <input type="number" class="form-control form-control-sm" name="min_confidence" value="0.1" step="0.01" min="0.01" max="1">
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="mb-3">
                                <label class="form-label">Min Lift</label>
                                <input type="number" class="form-control form-control-sm" name="min_lift" value="1.0" step="0.1" min="0.1">
                            </div>
                        </div>
                    </div>
                    
                    <button type="submit" class="btn btn-primary">
                        <i class="fas fa-play me-2"></i>
                        Run Apriori
                    </button>
                </form>
            </div>
        </div>
    </div>
    
    <div class="col-md-6">
        <div class="card algorithm-card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-tree me-2"></i>
                    FP-Growth Algorithm
                </h5>
            </div>
            <div class="card-body">
                <p class="card-text">FP-Growth uses a tree structure to represent the database and mine frequent patterns without candidate generation.</p>
                
                <form id="fpgrowthForm">
                    <div class="row">
                        <div class="col-md-4">
                            <div class="mb-3">
                                <label class="form-label">Min Support</label>
                                <input type="number" class="form-control form-control-sm" name="min_support" value="0.01" step="0.001" min="0.001" max="1">
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="mb-3">
                                <label class="form-label">Min Confidence</label>
                                <input type="number" class="form-control form-control-sm" name="min_confidence" value="0.1" step="0.01" min="0.01" max="1">
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="mb-3">
                                <label class="form-label">Min Lift</label>
                                <input type="number" class="form-control form-control-sm" name="min_lift" value="1.0" step="0.1" min="0.1">
                            </div>
                        </div>
                    </div>
                    
                    <button type="submit" class="btn btn-success">
                        <i class="fas fa-play me-2"></i>
                        Run FP-Growth
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Loading spinner -->
<div id="loadingSpinner" class="text-center mt-4" style="display: none;">
    <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
    </div>
    <p class="mt-2">Analyzing patterns...</p>
</div>

<!-- Results section -->
<div id="resultsSection" class="mt-4" style="display: none;">
    <div class="card">
        <div class="card-header">
            <h5 class="mb-0">
                <i class="fas fa-search me-2"></i>
                Analysis Results
            </h5>
        </div>
        <div class="card-body">
            <div class="row mb-3">
                <div class="col-md-4">
                    <div class="card bg-light">
                        <div class="card-body text-center">
                            <h4 id="algorithmUsed" class="text-primary"></h4>
                            <p class="mb-0">Algorithm Used</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card bg-light">
                        <div class="card-body text-center">
                            <h4 id="numRules" class="text-success"></h4>
                            <p class="mb-0">Association Rules</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card bg-light">
                        <div class="card-body text-center">
                            <h4 id="numItemsets" class="text-info"></h4>
                            <p class="mb-0">Frequent Itemsets</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <h6>Top Association Rules:</h6>
            <div class="table-responsive">
                <table class="table table-striped rules-table">
                    <thead>
                        <tr>
                            <th>Rule</th>
                            <th>Support</th>
                            <th>Confidence</th>
                            <th>Lift</th>
                        </tr>
                    </thead>
                    <tbody id="rulesTableBody">
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- Information cards -->
<div class="row mt-4">
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h6 class="mb-0">Support</h6>
            </div>
            <div class="card-body">
                <p class="small">Measures how frequently an itemset appears in the dataset. Higher support indicates more popular item combinations.</p>
                <p class="small text-muted">Support(A) = Transactions containing A / Total transactions</p>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h6 class="mb-0">Confidence</h6>
            </div>
            <div class="card-body">
                <p class="small">Measures the likelihood of purchasing item B when item A is purchased. Higher confidence indicates stronger association.</p>
                <p class="small text-muted">Confidence(A→B) = Support(A∪B) / Support(A)</p>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h6 class="mb-0">Lift</h6>
            </div>
            <div class="card-body">
                <p class="small">Measures how much more likely item B is purchased when item A is purchased. Lift > 1 indicates positive correlation.</p>
                <p class="small text-muted">Lift(A→B) = Confidence(A→B) / Support(B)</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
$(document).ready(function() {
    $('#aprioriForm').on('submit', function(e) {
        e.preventDefault();
        runAnalysis('/run-apriori', $(this).serialize());
    });
    
    $('#fpgrowthForm').on('submit', function(e) {
        e.preventDefault();
        runAnalysis('/run-fpgrowth', $(this).serialize());
    });
    
    function runAnalysis(url, data) {
        $('#loadingSpinner').show();
        $('#resultsSection').hide();
        
        $.ajax({
            url: url,
            method: 'POST',
            data: data,
            success: function(response) {
                displayResults(response);
                $('#loadingSpinner').hide();
                $('#resultsSection').show();
            },
            error: function(xhr) {
                alert('Error: ' + xhr.responseJSON.error);
                $('#loadingSpinner').hide();
            }
        });
    }
    
    function displayResults(data) {
        $('#algorithmUsed').text(data.algorithm);
        $('#numRules').text(data.num_rules);
        $('#numItemsets').text(data.num_frequent_itemsets);
        
        var tbody = $('#rulesTableBody');
        tbody.empty();
        
        data.rules.forEach(function(rule) {
            tbody.append(
                '<tr>' +
                '<td><small>' + rule.rule + '</small></td>' +
                '<td><span class="badge bg-primary">' + rule.support + '</span></td>' +
                '<td><span class="badge bg-success">' + rule.confidence + '</span></td>' +
                '<td><span class="badge bg-warning">' + rule.lift + '</span></td>' +
                '</tr>'
            );
        });
    }
});
</script>
{% endblock %}"""

# Visualizations template
visualizations_template = """{% extends "base.html" %}

{% block content %}
<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Data Visualizations</h1>
</div>

<div class="row">
    {% if plots.top_items %}
    <div class="col-12 mb-4">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-chart-bar me-2"></i>
                    Most Popular Products
                </h5>
            </div>
            <div class="card-body">
                <div id="topItemsPlot"></div>
            </div>
        </div>
    </div>
    {% endif %}
    
    {% if plots.rules_scatter %}
    <div class="col-12 mb-4">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-scatter-chart me-2"></i>
                    Association Rules Analysis
                </h5>
            </div>
            <div class="card-body">
                <div id="rulesScatterPlot"></div>
            </div>
        </div>
    </div>
    {% endif %}
</div>

<div class="row">
    {% if plots.country_distribution %}
    <div class="col-md-6 mb-4">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-globe me-2"></i>
                    Customer Distribution by Country
                </h5>
            </div>
            <div class="card-body">
                <div id="countryDistributionPlot"></div>
            </div>
        </div>
    </div>
    {% endif %}
    
    {% if plots.monthly_trend %}
    <div class="col-md-6 mb-4">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <i class="fas fa-chart-line me-2"></i>
                    Monthly Transaction Trend
                </h5>
            </div>
            <div class="card-body">
                <div id="monthlyTrendPlot"></div>
            </div>
        </div>
    </div>
    {% endif %}
</div>

{% if not plots %}
<div class="alert alert-warning">
    <i class="fas fa-exclamation-triangle me-2"></i>
    No visualizations available. Please load and analyze data first.
</div>
{% endif %}

{% endblock %}

{% block scripts %}
<script>
$(document).ready(function() {
    {% if plots.top_items %}
    var topItemsData = {{ plots.top_items|safe }};
    Plotly.newPlot('topItemsPlot', topItemsData.data, topItemsData.layout, {responsive: true});
    {% endif %}
    
    {% if plots.rules_scatter %}
    var rulesScatterData = {{ plots.rules_scatter|safe }};
    Plotly.newPlot('rulesScatterPlot', rulesScatterData.data, rulesScatterData.layout, {responsive: true});
    {% endif %}
    
    {% if plots.country_distribution %}
    var countryData = {{ plots.country_distribution|safe }};
    Plotly.newPlot('countryDistributionPlot', countryData.data, countryData.layout, {responsive: true});
    {% endif %}
    
    {% if plots.monthly_trend %}
    var monthlyData = {{ plots.monthly_trend|safe }};
    Plotly.newPlot('monthlyTrendPlot', monthlyData.data, monthlyData.layout, {responsive: true});
    {% endif %}
});
</script>
{% endblock %}"""

# Write the templates
with open('templates/analysis.html', 'w') as f:
    f.write(analysis_template)

with open('templates/market_basket.html', 'w') as f:
    f.write(market_basket_template)

with open('templates/visualizations.html', 'w') as f:
    f.write(visualizations_template)

print("Additional templates created successfully!")