import pandas as pd  # <- This is necessary

# Sample DataFrame
df = pd.DataFrame({
    "Product": ["A", "B", "A", "B"],
    "Region": ["North", "North", "South", "South"],
    "Sale_amt": [100, 200, 150, 250]
})

# Pivot table
pivot = pd.pivot_table(df, values="Sale_amt", index="Product", columns="Region", aggfunc="sum")

print(pivot)
