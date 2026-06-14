# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("tips.csv")

# Display first few rows
print(df.head())

# Check dataset information
print(df.info())

# Summary statistics
print(df.describe())