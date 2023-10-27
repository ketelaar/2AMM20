""""
https://github.com/antoniolopezmc/subgroups used to create all types of Subgroup Discovery processes
"""

from subgroups.algorithms import QFinder, SDMap, SDMapStar, BSD, CBSD, CPBSD, VLSD
from subgroups.quality_measures import WRAcc, WRAccOptimisticEstimate1
from pandas.api.types import is_string_dtype
import subgroups.tests as st
import pandas as pd
import time

# Verify installation
# st.run_all_tests()

# Start timer
start_time = time.time()

# SDMap
data = pd.read_csv("YearPredictionMSD.csv")[pd.read_csv("YearPredictionMSD.csv").columns[:23]].head(1)
print("nr of rows:", data.shape[0])
target = ('year', '2001')
data = data.astype(str)  # change all columns to str dtype

# for column in data.columns:
#     print(is_string_dtype(data[column]))

model = SDMap(quality_measure=WRAcc(), minimum_quality_measure_value=-1, minimum_n=0,
              write_results_in_file=True, file_path="results.txt")
model.fit(data, target)

print("Selected subgroups:", model.selected_subgroups)  # Number of selected subgroups,
print("Unselected subgroups: ",
      model.unselected_subgroups)  # Number of unselected subgroups due to not meeting the minimum quality threshold
print("Visited nodes: ", model.visited_nodes)  # Number of nodes (subgroups) visited from the search space

# BSD
# data = pd.read_csv("mushrooms.csv")[pd.read_csv("mushrooms.csv").columns[-2:]].head(1)
# print(type(data))
# print("nr of rows:", data.shape[0])
# target = ('poisonous', 'p')
# data = data.astype(str)  # change all columns to str dtype
#
# bsd_model = BSD(min_support=0, quality_measure=WRAcc(), optimistic_estimate=WRAccOptimisticEstimate1(),
#                 num_subgroups=8, max_depth=100, write_results_in_file=True, file_path="./results_BSD.txt")
# bsd_model.fit(data, target)
#
# print("Selected subgroups: ", bsd_model.selected_subgroups)  # Number of selected subgroups
# print("Unselected subgroups: ", bsd_model.unselected_subgroups)  # Number of unselected subgroups
# print("Visited subgroups: ", bsd_model.visited_subgroups)  # Number of generated subgroups

# # CBSD
# data = pd.read_csv("mushrooms.csv").head(1)
# print(type(data))
# print("nr of rows:", data.shape[0])
# target = ('poisonous', 'p')
# data = data.astype(str)  # change all columns to str dtype
#
# cbsd_model = CBSD(min_support=0, quality_measure=WRAcc(), optimistic_estimate=WRAccOptimisticEstimate1(),
#                   num_subgroups=8, max_depth=100, write_results_in_file=True, file_path="./results_CBSD.txt")
# cbsd_model.fit(data, target)
#
# print("Selected subgroups: ", cbsd_model.selected_subgroups)  # Number of selected subgroups
# print("Unselected subgroups: ", cbsd_model.unselected_subgroups)  # Number of unselected subgroups
# print("Visited subgroups: ", cbsd_model.visited_subgroups)  # Number of generated subgroups

# # CPBSD
# data = pd.read_csv("mushrooms.csv").head(1)
# print(type(data))
# print("nr of rows:", data.shape[0])
# target = ('poisonous', 'p')
# data = data.astype(str)  # change all columns to str dtype
#
# cpbsd_model = CPBSD(min_support=0, quality_measure=WRAcc(), optimistic_estimate=WRAccOptimisticEstimate1(),
#                     num_subgroups=8, max_depth=100, write_results_in_file=True, file_path="./results_CPBSD.txt")
# cpbsd_model.fit(data, target)
#
# print("Selected subgroups: ", cpbsd_model.selected_subgroups)  # Number of selected subgroups
# print("Unselected subgroups: ", cpbsd_model.unselected_subgroups)  # Number of unselected subgroups
# print("Visited subgroups: ", cpbsd_model.visited_subgroups)  # Number of generated subgroups

# QFinder
# data = pd.read_csv("mushrooms.csv")[pd.read_csv("mushrooms.csv").columns[-23:]].head(1)
# print(type(data))
# print("nr of rows:", data.shape[0])
# target = ('poisonous', 'p')
# data = data.astype(str)  # change all columns to str dtype
#
# model = QFinder(num_subgroups=5, write_results_in_file=True, file_path='results.txt', write_stats_in_file=True,
#                 stats_path="stats.html")
# model.fit(data, target)
#
# print("Selected subgroups: ", model.selected_subgroups)  # Number of selected subgroups
# print("Unselected subgroups: ",
#       model.unselected_subgroups)  # Number of unselected subgroups due to not meeting the minimum quality threshold
# print("Visited nodes: ", model.visited_subgroups)  # Number of nodes (subgroups) visited from the search space

# SDMapStar
# data = pd.read_csv("mushrooms.csv")[pd.read_csv("mushrooms.csv").columns[-15:]].head(1)
# print(type(data))
# print("nr of rows:", data.shape[0])
# target = ('poisonous', 'p')
# data = data.astype(str)  # change all columns to str dtype
#
# model = SDMapStar(WRAcc(), WRAccOptimisticEstimate1(), 0.01, num_subgroups=3, minimum_n=0, write_results_in_file=True,
#                   file_path="./results.txt")
# model.fit(data, target)
#
# print("Pruned subgroups: ", model.pruned_subgroups)  # Number of subgroups pruned by the threshold of the best subgroups
# print("Conditional pruned branches: ",
#       model.conditional_pruned_branches)  # Number of branches pruned from some conditional FPTree by the threshold
# # of the best subgroups
# print("Selected subgroups: ", model.selected_subgroups)  # Number of selected subgroups
# print("Unselected subgroups: ",
#       model.unselected_subgroups)  # Number of unselected subgroups due to not meeting the minimum quality threshold
# print("Visited nodes: ", model.visited_nodes)  # Number of nodes (subgroups) visited from the search space

# VLSD
# data = pd.read_csv("mushrooms.csv")[pd.read_csv("mushrooms.csv").columns[-15:]].head(1)
# print(type(data))
# print("nr of rows:", data.shape[0])
# target = ('poisonous', 'p')
# data = data.astype(str)  # change all columns to str dtype
#
# model = VLSD(quality_measure=WRAcc(), q_minimum_threshold=-1, optimistic_estimate=WRAccOptimisticEstimate1(),
#              oe_minimum_threshold=-1, sort_criterion_in_s1=VLSD.SORT_CRITERION_NO_ORDER,
#              sort_criterion_in_other_sizes=VLSD.SORT_CRITERION_NO_ORDER,
#              vertical_lists_implementation=VLSD.VERTICAL_LISTS_WITH_BITSETS, write_results_in_file=True,
#              file_path="./results.txt")
# model.fit(data, target)
#
# print("Selected subgroups: ", model.selected_subgroups)  # Number of selected subgroups
# print("Unselected subgroups: ",
#       model.unselected_subgroups)  # Number of unselected subgroups due to not meeting the minimum quality threshold
# print("Visited nodes: ", model.visited_nodes)  # Number of nodes (subgroups) visited from the search space

# Return the execution time
print("Runtime:", time.time() - start_time, "seconds")
