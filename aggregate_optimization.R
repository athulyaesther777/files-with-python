# aggregate_optimization.R

# Load necessary library
library(dplyr)

# Simulate a large dataset with groups
set.seed(456)
data <- data.frame(
  group = sample(1:100, 100000, replace = TRUE),
  value = rnorm(100000)
)

# Original Slow Code: Using a for loop to calculate group-wise sums
system.time({
  group_sums_slow <- data.frame(group = unique(data$group), sum_value = NA)
  for (i in seq_along(group_sums_slow$group)) {
    group_sums_slow$sum_value[i] <- sum(data$value[data$group == group_sums_slow$group[i]])
  }
})

# Optimized Code: Using dplyr's group_by and summarise functions
system.time({
  group_sums_fast <- data %>%
    group_by(group) %>%
    summarise(sum_value = sum(value))
})

# Compare the first few rows of both methods to ensure they match
head(group_sums_slow)
head(group_sums_fast)
