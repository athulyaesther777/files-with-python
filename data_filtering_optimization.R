# data_filtering_optimization.R

# Simulate a large dataset
set.seed(101)
data <- data.frame(
  id = 1:1000000,
  value = rnorm(1000000)
)

# Define a threshold for filtering
threshold <- 1.5

# Original Slow Code: Using a loop to filter data
system.time({
  filtered_data_slow <- data[FALSE, ]  # Create an empty data frame with the same structure
  for (i in 1:nrow(data)) {
    if (data$value[i] > threshold) {
      filtered_data_slow <- rbind(filtered_data_slow, data[i, ])
    }
  }
})

# Optimized Code: Using vectorized subsetting
system.time({
  filtered_data_fast <- data[data$value > threshold, ]
})

# Compare the first few rows of both filtered datasets to ensure they match
head(filtered_data_slow)
head(filtered_data_fast)
