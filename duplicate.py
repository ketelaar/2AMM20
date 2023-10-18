import pandas as pd
import sys

duplication_factor = int(sys.argv[1])

df = pd.read_csv("agaricus-lepiota.csv")

new_df = pd.concat([df] * duplication_factor)

new_df.to_csv(f"mushrooms-{duplication_factor}.csv", index=False)
