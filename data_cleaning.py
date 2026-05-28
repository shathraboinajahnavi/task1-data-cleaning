import pandas as pd

# Sample raw dataset
data = {
    "Name": ["John", "john", "Alice", None, "Bob"],
    "Age": [25, 25, None, 30, 22],
    "Date": ["01-01-2024", "01/01/2024", "2024-02-01", "2024/03/01", None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Standardize names
df["Name"] = df["Name"].str.title()

# Standardize date format
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

print("\nCleaned Data:")
print(df)
