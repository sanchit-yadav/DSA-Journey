# Right rotate an array by one place
def Right_rotate(arr):
    if not arr:
        return arr  # Return the empty array as is
    last_element = arr[-1]  # Store the last element
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]  # Shift elements to the right
    arr[0] = last_element  # Place the last element at the first position
    return arr  # Return the rotated array

# Example usage:
if __name__ == "__main__":
    array = [1, 2, 3, -4, 5, 6, 7, 8, 22, 90, -55]
    print("Original array:", array)
    rotated_array = Right_rotate(array)
    print("Array after right rotation:", rotated_array)