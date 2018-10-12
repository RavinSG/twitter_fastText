import pandas as pd


pd.set_option('display.max_columns', 500)
df = pd.read_csv("Similarities/analyze.csv")
df.rename(columns={ df.columns[0]: "ID" }, inplace=True)
df.set_index("ID", inplace=True)
df["Human Score"] = df["Human Score"]/10

df.insert(4, '100D_dif', df["Human Score"] - df["100D"])
df.insert(6, '200D_dif', df["Human Score"] - df["200D"])
df.insert(8, '300D_dif', df["Human Score"] - df["300D"])
print(df.head())

print(df['100D_dif'].apply(lambda x: x*x).sum())
print(df['200D_dif'].apply(lambda x: x*x).sum())
print(df['300D_dif'].apply(lambda x: x*x).sum())

df.to_csv("Similarities/results.csv")