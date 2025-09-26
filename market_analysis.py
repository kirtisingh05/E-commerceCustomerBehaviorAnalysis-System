
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
from mlxtend.preprocessing import TransactionEncoder
import plotly.express as px
import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder
import json

class MarketBasketAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = None
        self.basket_data = None
        self.frequent_itemsets = None
        self.rules = None

    def load_and_preprocess_data(self):
        """Load and preprocess the e-commerce transaction data"""
        try:
            self.df = pd.read_csv(self.data_file)

            # Convert InvoiceDate to datetime
            self.df['InvoiceDate'] = pd.to_datetime(self.df['InvoiceDate'])

            # Remove cancelled transactions (if InvoiceNo starts with 'C')
            self.df = self.df[~self.df['InvoiceNo'].astype(str).str.startswith('C')]

            # Remove negative quantities
            self.df = self.df[self.df['Quantity'] > 0]

            # Remove missing customer IDs
            self.df = self.df.dropna(subset=['CustomerID'])

            print(f"Data loaded successfully: {len(self.df)} transactions")
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False

    def prepare_basket_data(self):
        """Prepare data in basket format for market basket analysis"""
        # Group by InvoiceNo and create a list of items per transaction
        basket_data = self.df.groupby('InvoiceNo')['Description'].apply(list).tolist()

        # Use TransactionEncoder to convert to binary matrix
        te = TransactionEncoder()
        te_ary = te.fit(basket_data).transform(basket_data)
        self.basket_data = pd.DataFrame(te_ary, columns=te.columns_)

        print(f"Basket data prepared: {len(self.basket_data)} transactions, {len(self.basket_data.columns)} items")
        return self.basket_data

    def run_apriori_analysis(self, min_support=0.01, min_confidence=0.1, min_lift=1.0):
        """Run Apriori algorithm for frequent pattern mining"""
        try:
            # Find frequent itemsets using Apriori
            self.frequent_itemsets = apriori(self.basket_data, min_support=min_support, use_colnames=True)

            if len(self.frequent_itemsets) == 0:
                print(f"No frequent itemsets found with minimum support {min_support}")
                return None

            # Generate association rules
            self.rules = association_rules(self.frequent_itemsets, 
                                         metric="confidence", 
                                         min_threshold=min_confidence)

            # Filter by lift
            self.rules = self.rules[self.rules['lift'] >= min_lift]

            # Sort by confidence and lift
            self.rules = self.rules.sort_values(['confidence', 'lift'], ascending=False)

            print(f"Apriori analysis completed: {len(self.frequent_itemsets)} frequent itemsets, {len(self.rules)} rules")
            return self.rules

        except Exception as e:
            print(f"Error in Apriori analysis: {str(e)}")
            return None

    def run_fpgrowth_analysis(self, min_support=0.01, min_confidence=0.1, min_lift=1.0):
        """Run FP-Growth algorithm for frequent pattern mining"""
        try:
            # Find frequent itemsets using FP-Growth
            self.frequent_itemsets = fpgrowth(self.basket_data, min_support=min_support, use_colnames=True)

            if len(self.frequent_itemsets) == 0:
                print(f"No frequent itemsets found with minimum support {min_support}")
                return None

            # Generate association rules
            self.rules = association_rules(self.frequent_itemsets, 
                                         metric="confidence", 
                                         min_threshold=min_confidence)

            # Filter by lift
            self.rules = self.rules[self.rules['lift'] >= min_lift]

            # Sort by confidence and lift
            self.rules = self.rules.sort_values(['confidence', 'lift'], ascending=False)

            print(f"FP-Growth analysis completed: {len(self.frequent_itemsets)} frequent itemsets, {len(self.rules)} rules")
            return self.rules

        except Exception as e:
            print(f"Error in FP-Growth analysis: {str(e)}")
            return None

    def get_top_items(self, n=10):
        """Get top N most frequently bought items"""
        item_frequency = self.df['Description'].value_counts().head(n)
        return item_frequency

    def get_customer_insights(self):
        """Get customer behavior insights"""
        insights = {}

        # Customer transaction summary
        customer_stats = self.df.groupby('CustomerID').agg({
            'InvoiceNo': 'nunique',
            'Description': 'count',
            'Quantity': 'sum',
            'UnitPrice': 'mean'
        }).rename(columns={
            'InvoiceNo': 'Total_Orders',
            'Description': 'Total_Items',
            'Quantity': 'Total_Quantity',
            'UnitPrice': 'Avg_Price'
        })

        insights['customer_stats'] = customer_stats.describe()

        # Top customers by orders
        insights['top_customers'] = customer_stats.sort_values('Total_Orders', ascending=False).head(10)

        # Country analysis
        insights['country_stats'] = self.df.groupby('Country').agg({
            'InvoiceNo': 'nunique',
            'CustomerID': 'nunique',
            'Quantity': 'sum'
        }).sort_values('InvoiceNo', ascending=False)

        return insights

    def create_visualizations(self):
        """Create visualizations for the analysis"""
        plots = {}

        # 1. Top items bar chart
        top_items = self.get_top_items(15)
        fig1 = px.bar(x=top_items.index, y=top_items.values, 
                     title="Top 15 Most Frequently Bought Items",
                     labels={'x': 'Items', 'y': 'Frequency'})
        fig1.update_xaxis(tickangle=45)
        plots['top_items'] = json.dumps(fig1, cls=PlotlyJSONEncoder)

        # 2. Rules scatter plot
        if self.rules is not None and len(self.rules) > 0:
            fig2 = px.scatter(self.rules, x='support', y='confidence', 
                             size='lift', hover_data=['antecedents', 'consequents'],
                             title="Association Rules: Support vs Confidence",
                             labels={'support': 'Support', 'confidence': 'Confidence'})
            plots['rules_scatter'] = json.dumps(fig2, cls=PlotlyJSONEncoder)

        # 3. Country distribution
        country_counts = self.df['Country'].value_counts().head(10)
        fig3 = px.pie(values=country_counts.values, names=country_counts.index,
                     title="Customer Distribution by Country")
        plots['country_distribution'] = json.dumps(fig3, cls=PlotlyJSONEncoder)

        # 4. Monthly sales trend
        self.df['Month'] = self.df['InvoiceDate'].dt.to_period('M')
        monthly_sales = self.df.groupby('Month').agg({
            'InvoiceNo': 'nunique',
            'Quantity': 'sum'
        })
        fig4 = px.line(x=monthly_sales.index.astype(str), y=monthly_sales['InvoiceNo'],
                      title="Monthly Transaction Trend",
                      labels={'x': 'Month', 'y': 'Number of Transactions'})
        plots['monthly_trend'] = json.dumps(fig4, cls=PlotlyJSONEncoder)

        return plots

    def format_rules_for_display(self):
        """Format association rules for web display"""
        if self.rules is None or len(self.rules) == 0:
            return []

        formatted_rules = []
        for idx, rule in self.rules.head(20).iterrows():
            antecedents = list(rule['antecedents'])
            consequents = list(rule['consequents'])

            formatted_rules.append({
                'rule': f"If customer buys {', '.join(antecedents)} → then likely to buy {', '.join(consequents)}",
                'support': f"{rule['support']:.3f}",
                'confidence': f"{rule['confidence']:.3f}",
                'lift': f"{rule['lift']:.3f}",
                'antecedents': antecedents,
                'consequents': consequents
            })

        return formatted_rules

    def simulate_hdfs_operation(self, operation="store"):
        """Simulate Hadoop HDFS operations"""
        if operation == "store":
            # Simulate storing data to HDFS
            return {
                'status': 'success',
                'message': f'Data successfully stored to HDFS: /user/ecommerce/transactions/{self.data_file}',
                'path': f'/user/ecommerce/transactions/{self.data_file}',
                'size': f'{len(self.df)} records'
            }
        elif operation == "retrieve":
            # Simulate retrieving data from HDFS
            return {
                'status': 'success',
                'message': f'Data successfully retrieved from HDFS',
                'records': len(self.df),
                'size': f'{len(self.df)} records'
            }
