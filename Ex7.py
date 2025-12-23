import pandas as pd

data = {
    "Item":["TV","TV","Phone","Phone"],
    "Sale_amt":[1000,1500,500,700]
}
df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values="Sale_amt", index="Item",
                       aggfunc=["max","min"])
print(pivot)
