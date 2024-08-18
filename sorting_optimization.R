# sorting_optimization.R

# Simulate a large unsorted vector
set.seed(789)
data <- sample(1:100000, 100000, replace = TRUE)

# Original Slow Code: Using a custom bubble sort implementation
bubble_sort <- function(vec) {
  n <- length(vec)
  for (i in 1:(n-1)) {
    for (j in 1:(n-i)) {
      if (vec[j] > vec[j+1]) {
        temp <- vec[j]
        vec[j] <- vec[j+1]
        vec[j+1] <- temp
      }
    }
  }
  return(vec)
}

# Measure time taken by bubble sort
system.time({
  sorted_data_slow <- bubble_sort(data)
})

# Optimized Code: Using R's built-in sort function
system.time({
  sorted_data_fast <- sort(data)
})

# Compare the first few sorted values from both methods to ensure they match
head(sorted_data_slow)
head(sorted_data_fast)
