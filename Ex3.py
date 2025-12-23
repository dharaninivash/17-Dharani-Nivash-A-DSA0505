import pandas as pd

data = {
    "JOB_TITLE":[
        "President","Administration Vice President","Administration Assistant",
        "Finance Manager","Accountant","Accounting Manager","Public Accountant"
    ]
}
df = pd.DataFrame(data)

print(df.sort_values(by="JOB_TITLE", ascending=False))
