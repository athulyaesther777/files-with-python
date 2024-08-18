# optimize_performance.R

# Load necessary library
library(dplyr)

# Simulate a large dataset
set.seed(123)
data <- data.frame(
  id = 1:100000,
  value1 = rnorm(100000),
  value2 = runif(100000)
)

# Original Slow Code: Using a for loop to calculate a new column
system.time({
  data$new_value_slow <- NA
  for (i in 1:nrow(data)) {
    data$new_value_slow[i] <- data$value1[i] * data$value2[i]
  }
})

# Optimized Code: Using vectorized operations to calculate the new column
system.time({
  data <- data %>%
    mutate(new_value_fast = value1 * value2)
})

# Compare the first few rows of both methods to ensure they match
head(data[, c("new_value_slow", "new_value_fast")])
