#!/usr/bin/env python3
""" This module contains data analyses and visualizations of CSV data using pandas and matplotlib """

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# 1: Load and Explore the Dataset


def load_and_explore_data():
    try:
        # Load the Iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = iris.target
        df['species'] = df['species'].map(
            {0: 'setosa', 1: 'versicolor', 2: 'virginica'})

        # Display first few rows
        print("First 5 rows of the dataset:")
        print(df.head())
        print("\n")

        # Explore structure
        print("Dataset information:")
        print(df.info())
        print("\n")

        # Check for missing values
        print("Missing values per column:")
        print(df.isnull().sum())
        print("\n")

        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# 2: Basic Data Analysis


def perform_data_analysis(df):
    if df is None:
        return

    print("Basic statistics of numerical columns:")
    print(df.describe())
    print("\n")

    # Group by species and compute mean
    print("Mean measurements by species:")
    print(df.groupby('species').mean())
    print("\n")

    # Additional analysis
    print("Correlation between features:")
    print(df.corr(numeric_only=True))
    print("\n")

# 3: Data Visualization


def create_visualizations(df):
    if df is None:
        return

    plt.figure(figsize=(15, 10))

    # 1. Line chart (simulating time series with index)
    plt.subplot(2, 2, 1)
    df['sepal length (cm)'].plot(
        kind='line', title='Sepal Length Trend (by index)')
    plt.xlabel('Index')
    plt.ylabel('Sepal Length (cm)')

    # 2. Bar chart (average petal length by species)
    plt.subplot(2, 2, 2)
    df.groupby('species')['petal length (cm)'].mean().plot(
        kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
    plt.title('Average Petal Length by Species')
    plt.ylabel('Petal Length (cm)')

    # 3. Histogram (sepal width distribution)
    plt.subplot(2, 2, 3)
    df['sepal width (cm)'].plot(
        kind='hist', bins=15, color='purple', alpha=0.7)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')

    # 4. Scatter plot (sepal length vs petal length)
    plt.subplot(2, 2, 4)
    colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    for species, group in df.groupby('species'):
        plt.scatter(group['sepal length (cm)'], group['petal length (cm)'],
                    label=species, alpha=0.7)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()

    plt.tight_layout()
    plt.savefig('iris_visualizations.png')
    plt.show()


def main():
    print("=== Iris Dataset Analysis ===")
    print("Task 1: Loading and exploring the dataset\n")
    df = load_and_explore_data()

    print("\nTask 2: Performing basic data analysis\n")
    perform_data_analysis(df)

    print("\nTask 3: Creating visualizations\n")
    create_visualizations(df)

    print("\nAnalysis complete. Visualizations saved as PNG files.")


if __name__ == "__main__":
    main()`
