import pandas as pd
import sys

duplication_factor = int(sys.argv[1])

# read the .data as a csv, since it is in that format anyway
df = pd.read_csv("agaricus-lepiota.data")

# concate the dataframe duplication_factor times with itself
new_df = pd.concat([df] * duplication_factor)

new_df.to_csv(f"mushrooms-{duplication_factor}.csv", index=False)
