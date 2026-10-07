# DSA With Python

Daily practice solutions for learning data structures and algorithms with
Python. The repository is organized by subject and grows as new concepts are
covered.

## Project structure

```text
.
|-- Basics of Programming
|   |-- Basic Math
|   |   |-- armstrong_number.py
|   |   |-- palindrome.py
|   |   |-- print_divisors.py
|   |   `-- README.md
|   |-- Intro_to_hashing
|   |   `-- store_frequency_in_dictionary.py
|   `-- Recursion
|       |-- factorial.py
|       `-- Is_str_Palindrome.py
|-- List & Array Leetcode Problem
|   |-- A) Easy Level Problems
|   |   |-- Largest_element_in_array.py
|   |   |-- Linear_Search.py
|   |   |-- Max_Consecutive_One.py
|   |   |-- Merge_2_sorted_arr.py
|   |   |-- Missing_Number.py
|   |   |-- Move_zeros.py
|   |   |-- Remove_Duplicate.py
|   |   |-- Right_rotate_Array.py
|   |   `-- Second_Largest.py
|   |-- B) Medium Level Problems
|   |   |-- Buy_sell_Stock.py
|   |   |-- Longest_Consecutive_Seq.py
|   |   |-- ReArrange_By_Sign.py
|   |   |-- Rotate_Matrix.py
|   |   |-- Set_Matrix_Zeros.py
|   |   |-- Spiral_Order.py
|   |   |-- Subarray_max_sum.py
|   |   `-- Target_Sum.py
|   `-- C) Hard Level Problems
|       |-- 3Sum.py
|       `-- 4Sum.py
`-- Sorting-Algorithms
    |-- Bubble_sort.py
    |-- Insertion_Sort.py
    |-- Merge_Sort.py
    |-- Quick_Sort.py
    `-- Selection-Sort
        |-- ascending_ord.py
        `-- descending_ord.py
```

## Topics covered

| Area | Problems and implementations |
| --- | --- |
| Basic Math | [Palindrome number](<Basics of Programming/Basic Math/palindrome.py>), [Armstrong number](<Basics of Programming/Basic Math/armstrong_number.py>), [Print divisors](<Basics of Programming/Basic Math/print_divisors.py>) |
| Recursion | [Factorial](<Basics of Programming/Recursion/factorial.py>), [String palindrome](<Basics of Programming/Recursion/Is_str_Palindrome.py>) |
| Hashing | [Frequency counting with a dictionary](<Basics of Programming/Intro_to_hashing/store_frequency_in_dictionary.py>) |
| Lists and Arrays - Easy | [Largest element](<List & Array Leetcode Problem/A) Easy Level Problems/Largest_element_in_array.py>), [Linear search](<List & Array Leetcode Problem/A) Easy Level Problems/Linear_Search.py>), [Maximum consecutive ones](<List & Array Leetcode Problem/A) Easy Level Problems/Max_Consecutive_One.py>), [Merge two sorted arrays without duplicates](<List & Array Leetcode Problem/A) Easy Level Problems/Merge_2_sorted_arr.py>), [Missing number](<List & Array Leetcode Problem/A) Easy Level Problems/Missing_Number.py>), [Move zeros](<List & Array Leetcode Problem/A) Easy Level Problems/Move_zeros.py>), [Remove duplicates](<List & Array Leetcode Problem/A) Easy Level Problems/Remove_Duplicate.py>), [Right rotate array](<List & Array Leetcode Problem/A) Easy Level Problems/Right_rotate_Array.py>), [Second largest element](<List & Array Leetcode Problem/A) Easy Level Problems/Second_Largest.py>) |
| Lists and Arrays - Medium | [Best time to buy and sell stock](<List & Array Leetcode Problem/B) Medium Level Problems/Buy_sell_Stock.py>), [Longest consecutive sequence](<List & Array Leetcode Problem/B) Medium Level Problems/Longest_Consecutive_Seq.py>), [Rearrange by sign](<List & Array Leetcode Problem/B) Medium Level Problems/ReArrange_By_Sign.py>), [Rotate matrix 90-degree clockwise](<List & Array Leetcode Problem/B) Medium Level Problems/Rotate_Matrix.py>), [Set matrix zeroes](<List & Array Leetcode Problem/B) Medium Level Problems/Set_Matrix_Zeros.py>), [Spiral order traversal](<List & Array Leetcode Problem/B) Medium Level Problems/Spiral_Order.py>), [Maximum subarray sum](<List & Array Leetcode Problem/B) Medium Level Problems/Subarray_max_sum.py>), [Two Sum](<List & Array Leetcode Problem/B) Medium Level Problems/Target_Sum.py>) |
| Lists and Arrays - Hard | [3Sum](<List & Array Leetcode Problem/C) Hard Level Problems/3Sum.py>), [4Sum](<List & Array Leetcode Problem/C) Hard Level Problems/4Sum.py>) |
| Sorting | [Bubble sort](<Sorting-Algorithms/Bubble_sort.py>), [Insertion sort](<Sorting-Algorithms/Insertion_Sort.py>), [Merge sort](<Sorting-Algorithms/Merge_Sort.py>), [Quick sort](<Sorting-Algorithms/Quick_Sort.py>), [Selection sort - ascending](<Sorting-Algorithms/Selection-Sort/ascending_ord.py>), [Selection sort - descending](<Sorting-Algorithms/Selection-Sort/descending_ord.py>) |

Detailed notes for the Basic Math problems are available in the
[Basic Math README](<Basics of Programming/Basic Math/README.md>).

## Complexity overview

| Implementation | Time | Space |
| --- | --- | --- |
| Basic Math palindrome | `O(d)` | `O(1)` |
| Armstrong number | `O(d)` | `O(d)` |
| Print divisors | `O(sqrt(n) + k log k)` | `O(k)` |
| Recursive factorial | `O(n)` | `O(n)` |
| Recursive string palindrome | `O(n)` | `O(n)` |
| Frequency counting | `O(n)` average | `O(k)` |
| Largest element in an array | `O(n)` | `O(1)` |
| Linear search | `O(n)` | `O(1)` |
| Maximum consecutive ones | `O(n)` | `O(1)` |
| Merge two sorted arrays without duplicates | `O(n + m)` | `O(n + m)` |
| Missing number (current implementation) | `O(n^2)` | `O(1)` |
| Move zeros | `O(n)` | `O(1)` |
| Second largest element | `O(n)` | `O(1)` |
| Remove duplicates from a sorted array | `O(n)` | `O(1)` |
| Right rotate array | `O(n)` | `O(n)` |
| Maximum subarray sum | `O(n)` | `O(1)` |
| Two Sum | `O(n)` average | `O(n)` |
| Best time to buy and sell stock | `O(n)` | `O(1)` |
| Longest consecutive sequence | `O(n)` average | `O(n)` |
| Rearrange by sign | `O(n)` | `O(n)` |
| Rotate matrix 90 degrees clockwise | `O(n^2)` | `O(1)` |
| Set matrix zeroes | `O(mn)` | `O(m + n)` |
| Spiral order traversal | `O(mn)` | `O(mn)` including the returned list |
| 3Sum | `O(n^2)` after sorting | `O(1)` extra space |
| 4Sum | `O(n^3)` after sorting | `O(1)` extra space |
| Bubble sort | `O(n^2)` worst case | `O(1)` |
| Insertion sort | `O(n^2)` worst case | `O(1)` |
| Merge sort | `O(n log n)` | `O(n)` |
| Quick sort | `O(n log n)` average, `O(n^2)` worst case | `O(n log n)` for this implementation |
| Selection sort | `O(n^2)` | `O(1)` |

Here, `d` is the number of digits, `n` is the input size, and `k` is the
number of distinct values or divisors as applicable.

The remove-duplicates solution expects the input array to be sorted and
compacts unique values at the beginning of the same array. The second-largest
solution returns the second distinct largest value.

## Running a solution

Run commands from the repository root. Scripts that request input will prompt
for it; the sorting scripts use built-in example arrays.

```powershell
python "Basics of Programming\Basic Math\palindrome.py"
python "Basics of Programming\Recursion\factorial.py"
python "Basics of Programming\Recursion\Is_str_Palindrome.py"
python "Sorting-Algorithms\Bubble_sort.py"
python "Sorting-Algorithms\Insertion_Sort.py"
python "Sorting-Algorithms\Merge_Sort.py"
python "Sorting-Algorithms\Quick_Sort.py"
python "Sorting-Algorithms\Selection-Sort\ascending_ord.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Largest_element_in_array.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Linear_Search.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Max_Consecutive_One.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Merge_2_sorted_arr.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Missing_Number.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Move_zeros.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Second_Largest.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Remove_Duplicate.py"
python "List & Array Leetcode Problem\A) Easy Level Problems\Right_rotate_Array.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\Subarray_max_sum.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\Target_Sum.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\Buy_sell_Stock.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\Longest_Consecutive_Seq.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\ReArrange_By_Sign.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\Rotate_Matrix.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\Set_Matrix_Zeros.py"
python "List & Array Leetcode Problem\B) Medium Level Problems\Spiral_Order.py"
python "List & Array Leetcode Problem\C) Hard Level Problems\3Sum.py"
python "List & Array Leetcode Problem\C) Hard Level Problems\4Sum.py"
```

The hashing example builds a frequency dictionary from its `nums` list. It
currently has no print statement, so run it when inspecting or extending the
example:

```powershell
python "Basics of Programming\Intro_to_hashing\store_frequency_in_dictionary.py"
```

## Conventions

- Use descriptive, lowercase `snake_case` filenames for new solutions.
- Put reusable logic in functions where practical.
- Keep command-line input/output inside `if __name__ == "__main__":`.
- Add short comments only for non-obvious algorithm steps.
- Do not commit generated files such as `__pycache__`; these are excluded by
  `.gitignore`.
