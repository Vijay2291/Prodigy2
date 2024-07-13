import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/content/gender_submission.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Check column names to verify exact names available in the dataset
print("Column Names:")
print(df.columns)

# Adjust column names based on your dataset
# Replace 'PassengerId' and 'Survived' with the actual column names from your dataset
passenger_column = 'PassengerId'  # Replace with actual column name
survived_column = 'Survived'      # Replace with actual column name

# Initial exploration
print("\nDataset Dimensions:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values if needed

# Explore relationships between variables
plt.figure(figsize=(10, 6))
sns.countplot(x=survived_column, data=df)
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# Example: Histogram of 'PassengerId'
plt.figure(figsize=(10, 6))
sns.histplot(df[passenger_column], bins=20, kde=True)
plt.title('Distribution of PassengerId')
plt.xlabel('PassengerId')
plt.ylabel('Count')
plt.show()

# Correlation matrix (if applicable)
# Note: Correlation is typically used for numerical variables, adjust as per your dataset

