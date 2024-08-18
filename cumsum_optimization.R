# cumsum_optimization.R

# Simulate a large numeric vector
set.seed(123)
data <- rnorm(1000000)

# Original Slow Code: Using a loop to calculate cumulative sum
system.time({
  cumsum_slow <- numeric(length(data))
  cumsum_slow[1] <- data[1]
  for (i in 2:length(data)) {
    cumsum_slow[i] <- cumsum_slow[i-1] + data[i]
  }
})

# Optimized Code: Using R's built-in cumsum function
system.time({
  cumsum_fast <- cumsum(data)
})

# Compare the first few cumulative sums from both methods to ensure they match
head(cumsum_slow)
head(cumsum_fast)
