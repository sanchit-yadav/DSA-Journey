def selection_sort(arr):
    """
    Sorts an array in descending order using the selection sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list in descending order.
    """
    n = len(arr)
    
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        
        # Iterate through the unsorted elements
        for j in range(i + 1, n):
            # Update min_index if a smaller element is found
            if arr[j] > arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:
if __name__ == "__main__":
    sample_array = [7, 8, 22, 25, 101, -11, 78, -5, 0, 46, -2]
    sorted_array = selection_sort(sample_array)
    print("Sorted array:", sorted_array)