import pandas as pd

# Load dataset
df = pd.read_csv("creditcard.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFraud Distribution:")
print(df['Class'].value_counts())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned file
df.to_csv("cleaned_creditcard.csv", index=False)

print("\nCleaned dataset saved successfully!")