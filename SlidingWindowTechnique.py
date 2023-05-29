from array import array


def maxSum(arr, k):
    n = len(arr)
    if n<k:
        print("Invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    # Compute the sums of remaining windows by removing first element of previous window and adding last element of the current window.
    for i in range(n-k):
        window_sum= window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum,max_sum)
    return max_sum

# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))