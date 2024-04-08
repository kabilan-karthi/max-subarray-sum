def max_subarray_sum(arr):
    """
    Finds the maximum subarray sum in a given array.

    Parameters:
    arr: The array to search.

    Returns:
    The maximum subarray sum.
    """

    # Initialize the current and maximum subarray sums to the first element in the array.
    current_sum = arr[0]
    max_sum = arr[0]

    # Iterate over the remaining elements in the array.
    for i in range(1, len(arr)):
        # Update the current subarray sum.
        current_sum = max(arr[i], current_sum + arr[i])

        # Update the maximum subarray sum if necessary.
        max_sum = max(max_sum, current_sum)

    # Return the maximum subarray sum.
    return max_sum
