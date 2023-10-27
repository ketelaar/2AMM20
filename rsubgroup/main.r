# https://cran.r-project.org/web/packages/rsubgroup/rsubgroup.pdf used to
# create the Subgroup Discovery process

# Import rsubgroup
library(rsubgroup)

# Start timer
start.time <- Sys.time()

# Create Subgroup Discovery task
result <- DiscoverSubgroups(
  balancescale, as.target("Class Name", "L"), new("SDTaskConfig",
                attributes=c("Left-Weight","Left-Distance", "Right-Weight",
                             "Right-Distance")))

# Return the subgroups
ToDataFrame(result)

# Return execution time
time.taken <- round(Sys.time() - start.time, 2)
time.taken
