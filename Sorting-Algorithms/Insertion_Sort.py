def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort(sample_array)
    print("Sorted array is:", sorted_array)