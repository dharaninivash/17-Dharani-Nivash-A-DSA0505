import pandas as pd  # <- mandatory

# Sample data
data = {
    "Product": ["A", "B", "C"],
    "Region": ["North", "South", "East"],
    "Sale_amt": [100, 200, 150]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)
