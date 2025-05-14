"""
iris_analysis.py
A complete data analysis and visualization workflow using:
- pandas for data manipulation
- matplotlib/seaborn for visualization
- Iris dataset for demonstration
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set style for better looking plots
sns.set(style="whitegrid")
plt.style.use('seaborn-v0_8')

# =============================================
# Task 1: Load and Explore the Dataset
# =============================================

def load_and_explore_data():
    """Load and perform initial exploration of the Iris dataset"""
    try:
        # Load dataset
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        # Initial exploration
        print("=== Dataset First Look ===")
        print(df.head())
        
        print("\n=== Dataset Structure ===")
        print(f"Shape: {df.shape}")
        print("\nData Types:")
        print(df.dtypes)
        
        print("\n=== Missing Values ===")
        print(df.isnull().sum())
        
        return df
    
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# =============================================
# Task 2: Basic Data Analysis
# =============================================

def perform_analysis(df):
    """Perform statistical analysis on the dataset"""
    if df is None:
        return
    
    print("\n=== Basic Statistics ===")
    print(df.describe())
    
    print("\n=== Statistics by Species ===")
    print(df.groupby('species').mean())
    
    print("\n=== Interesting Findings ===")
    print("1. Setosa has significantly smaller petal dimensions than other species")
    print("2. Versicolor and Virginica have overlapping but distinct measurements")
    print("3. Sepal width has the smallest variance across species")

# =============================================
# Task 3: Data Visualization
# =============================================

def create_visualizations(df):
    """Create required visualizations"""
    if df is None:
        return
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Iris Dataset Visualizations', fontsize=16)
    
    # 1. Line Chart (using index as pseudo-time)
    df['sepal length (cm)'].plot(ax=axes[0, 0], title='Sepal Length Trend')
    axes[0, 0].set_ylabel('Sepal Length (cm)')
    
    # 2. Bar Chart
    df.groupby('species')['petal length (cm)'].mean().plot(
        kind='bar', ax=axes[0, 1], color=['skyblue', 'salmon', 'lightgreen'])
    axes[0, 1].set_title('Average Petal Length by Species')
    axes[0, 1].set_ylabel('Length (cm)')
    
    # 3. Histogram
    df['sepal width (cm)'].plot(
        kind='hist', ax=axes[1, 0], bins=15, color='purple', alpha=0.7)
    axes[1, 0].set_title('Sepal Width Distribution')
    axes[1, 0].set_xlabel('Width (cm)')
    
    # 4. Scatter Plot
    sns.scatterplot(
        data=df, x='sepal length (cm)', y='petal length (cm)', 
        hue='species', ax=axes[1, 1], palette='viridis')
    axes[1, 1].set_title('Sepal vs Petal Length')
    
    plt.tight_layout()
    plt.savefig('iris_visualizations.png')
    plt.show()

# =============================================
# Main Execution
# =============================================

if __name__ == "__main__":
    print("Iris Dataset Analysis")
    print("=====================\n")
    
    # Task 1
    iris_df = load_and_explore_data()
    
    # Task 2
    perform_analysis(iris_df)
    
    # Task 3
    create_visualizations(iris_df)
    
    print("\nAnalysis complete. Visualizations saved as 'iris_visualizations.png'")
