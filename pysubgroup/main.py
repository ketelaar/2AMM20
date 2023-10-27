"""
https://github.com/flemmerich/pysubgroup used to create the Subgroup Discovery process
"""

import pysubgroup as ps
import pandas as pd
import time

# Load the dataset
data = pd.read_csv("YearPredictionMSD-0.1.csv")

# Start timer
start_time = time.time()

# Create Subgroup Discovery task
target = ps.BinaryTarget('year', '2001')
search_space = ps.create_selectors(data, ignore=['year'])
task = ps.SubgroupDiscoveryTask(
    data,
    target,
    search_space,
    result_set_size=10,
    depth=2,
    qf=ps.WRAccQF())

# Execute the task
result = ps.SimpleSearch().execute(task)

# Return the Subgroups and execution time
print(result.to_dataframe().to_string())
print("Runtime:", time.time() - start_time, "seconds")
