# Right rotate an array by K place
def right_rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is greater than n
    return arr[-k:] + arr[:-k]

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 10, -12, 0, 7, -18]
    k = 25
    rotated_arr = right_rotate_array(arr, k)
    print(rotated_arr)