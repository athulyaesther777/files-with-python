# data_aggregation_optimization.R

# Simulate a large dataset
set.seed(202)
data <- data.frame(
  group = sample(letters[1:5], 1000000, replace = TRUE),
  value = rnorm(1000000)
)

# Original Slow Code: Using a loop to calculate group-wise sums
system.time({
  unique_groups <- unique(data$group)
  group_sums_slow <- numeric(length(unique_groups))
  names(group_sums_slow) <- unique_groups
  
  for (g in unique_groups) {
    group_sums_slow[g] <- sum(data$value[data$group == g])
  }
})

# Optimized Code: Using tapply() to calculate group-wise sums
system.time({
  group_sums_fast <- tapply(data$value, data$group, sum)
})

# Compare the results to ensure they match
print(group_sums_slow)
print(group_sums_fast)
