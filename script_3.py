# Create the main Flask application
flask_app_code = """
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import pandas as pd
import os
from market_analysis import MarketBasketAnalyzer
import plotly
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Global analyzer object
analyzer = None

@app.route('/')
def index():
    \"\"\"Home page with project overview\"\"\"
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_data():
    \"\"\"Upload and load dataset\"\"\"
    global analyzer
    
    if request.method == 'POST':
        # For demo, we'll use the pre-created dataset
        data_file = 'ecommerce_transactions.csv'
        
        if os.path.exists(data_file):
            analyzer = MarketBasketAnalyzer(data_file)
            
            if analyzer.load_and_preprocess_data():
                analyzer.prepare_basket_data()
                flash('Dataset loaded successfully!', 'success')
                return redirect(url_for('analysis'))
            else:
                flash('Error loading dataset!', 'error')
        else:
            flash('Dataset file not found!', 'error')
    
    return render_template('upload.html')

@app.route('/analysis')
def analysis():
    \"\"\"Main analysis page\"\"\"
    global analyzer
    
    if analyzer is None:
        flash('Please upload a dataset first!', 'warning')
        return redirect(url_for('upload_data'))
    
    # Get basic statistics
    total_transactions = len(analyzer.df)
    total_customers = analyzer.df['CustomerID'].nunique()
    total_products = analyzer.df['Description'].nunique()
    date_range = f"{analyzer.df['InvoiceDate'].min().strftime('%Y-%m-%d')} to {analyzer.df['InvoiceDate'].max().strftime('%Y-%m-%d')}"
    
    # Get top items
    top_items = analyzer.get_top_items(10)
    
    # Get customer insights
    insights = analyzer.get_customer_insights()
    
    return render_template('analysis.html', 
                         total_transactions=total_transactions,
                         total_customers=total_customers,
                         total_products=total_products,
                         date_range=date_range,
                         top_items=top_items,
                         insights=insights)

@app.route('/market-basket')
def market_basket():
    \"\"\"Market basket analysis page\"\"\"
    global analyzer
    
    if analyzer is None:
        flash('Please upload a dataset first!', 'warning')
        return redirect(url_for('upload_data'))
    
    return render_template('market_basket.html')

@app.route('/run-apriori', methods=['POST'])
def run_apriori():
    \"\"\"Run Apriori algorithm\"\"\"
    global analyzer
    
    if analyzer is None:
        return jsonify({'error': 'No dataset loaded'}), 400
    
    # Get parameters from form
    min_support = float(request.form.get('min_support', 0.01))
    min_confidence = float(request.form.get('min_confidence', 0.1))
    min_lift = float(request.form.get('min_lift', 1.0))
    
    # Run analysis
    rules = analyzer.run_apriori_analysis(min_support, min_confidence, min_lift)
    
    if rules is None:
        return jsonify({'error': 'No rules found with given parameters'}), 400
    
    # Format results
    formatted_rules = analyzer.format_rules_for_display()
    
    return jsonify({
        'algorithm': 'Apriori',
        'num_rules': len(rules),
        'num_frequent_itemsets': len(analyzer.frequent_itemsets),
        'rules': formatted_rules
    })

@app.route('/run-fpgrowth', methods=['POST'])
def run_fpgrowth():
    \"\"\"Run FP-Growth algorithm\"\"\"
    global analyzer
    
    if analyzer is None:
        return jsonify({'error': 'No dataset loaded'}), 400
    
    # Get parameters from form
    min_support = float(request.form.get('min_support', 0.01))
    min_confidence = float(request.form.get('min_confidence', 0.1))
    min_lift = float(request.form.get('min_lift', 1.0))
    
    # Run analysis
    rules = analyzer.run_fpgrowth_analysis(min_support, min_confidence, min_lift)
    
    if rules is None:
        return jsonify({'error': 'No rules found with given parameters'}), 400
    
    # Format results
    formatted_rules = analyzer.format_rules_for_display()
    
    return jsonify({
        'algorithm': 'FP-Growth',
        'num_rules': len(rules),
        'num_frequent_itemsets': len(analyzer.frequent_itemsets),
        'rules': formatted_rules
    })

@app.route('/visualizations')
def visualizations():
    \"\"\"Visualizations page\"\"\"
    global analyzer
    
    if analyzer is None:
        flash('Please upload a dataset first!', 'warning')
        return redirect(url_for('upload_data'))
    
    # Create visualizations
    plots = analyzer.create_visualizations()
    
    return render_template('visualizations.html', plots=plots)

@app.route('/hdfs-simulation')
def hdfs_simulation():
    \"\"\"HDFS simulation page\"\"\"
    return render_template('hdfs.html')

@app.route('/hdfs-operation', methods=['POST'])
def hdfs_operation():
    \"\"\"Simulate HDFS operations\"\"\"
    global analyzer
    
    if analyzer is None:
        return jsonify({'error': 'No dataset loaded'}), 400
    
    operation = request.form.get('operation', 'store')
    result = analyzer.simulate_hdfs_operation(operation)
    
    return jsonify(result)

@app.route('/about')
def about():
    \"\"\"About page with technical details\"\"\"
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""

# Write the Flask app to file
with open('app.py', 'w') as f:
    f.write(flask_app_code)

print("Flask application created successfully!")