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
`-- Sorting-Algorithms
    |-- Bubble_sort.py
    |-- Insertion_Sort.py
    |-- Merge_Sort.py
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
| Sorting | [Bubble sort](<Sorting-Algorithms/Bubble_sort.py>), [Insertion sort](<Sorting-Algorithms/Insertion_Sort.py>), [Merge sort](<Sorting-Algorithms/Merge_Sort.py>), [Selection sort - ascending](<Sorting-Algorithms/Selection-Sort/ascending_ord.py>), [Selection sort - descending](<Sorting-Algorithms/Selection-Sort/descending_ord.py>) |

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
| Bubble sort | `O(n^2)` worst case | `O(1)` |
| Insertion sort | `O(n^2)` worst case | `O(1)` |
| Merge sort | `O(n log n)` | `O(n)` |
| Selection sort | `O(n^2)` | `O(1)` |

Here, `d` is the number of digits, `n` is the input size, and `k` is the
number of distinct values or divisors as applicable.

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
python "Sorting-Algorithms\Selection-Sort\ascending_ord.py"
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
