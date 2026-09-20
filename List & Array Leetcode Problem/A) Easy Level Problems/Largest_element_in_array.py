def largest(arr):
    if not arr:
        return None  # Return None for empty array
    max_element = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > max_element:
            max_element = num  # Update max_element if a larger number is found
    return max_element  # Return the largest element found

# Example usage:
if __name__ == "__main__":
    array = [1,8,7,56,90]
    print("The largest element in the array is:", largest(array))