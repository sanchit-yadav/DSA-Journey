def Bubble_sort(arr):
    n = len(arr)
    for i in range(n-2, -1, -1):
        is_swapped = False
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        if not is_swapped:
            break

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    Bubble_sort(arr)
    print("Sorted array:", arr)
