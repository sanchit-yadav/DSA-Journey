# Basic Math

This folder contains introductory number-theory practice problems.

## 1. Palindrome Number

### Problem statement

Given an integer, determine whether it reads the same forwards and backwards.
Negative numbers are not considered palindromes.

Example: `121` is a palindrome, while `123` is not.

### Solution

See [palindrome.py](<palindrome.py>).

### Approach and complexity

Reverse the number digit by digit using modulo and integer division, then
compare the reversed value with the original value.

- Time: `O(d)`, where `d` is the number of digits
- Space: `O(1)`

## 2. Armstrong Number

### Problem statement

Given an integer, determine whether it equals the sum of each digit raised to
the power of the total number of digits.

Example: `153` is an Armstrong number because `1^3 + 5^3 + 3^3 = 153`.

### Solution

See [armstrong_number.py](<armstrong_number.py>).

### Approach and complexity

Count the digits, process each digit with modulo and integer division, and add
its power to a running total.

- Time: `O(d)`
- Space: `O(d)` because the string representation is used to count digits

## 3. Print Divisors

### Problem statement

Given a positive integer, return all of its positive divisors in ascending
order.

Example: the divisors of `12` are `[1, 2, 3, 4, 6, 12]`.

### Solution

See [print_divisors.py](<print_divisors.py>).

### Approach and complexity

Check candidates only up to the square root. Whenever a divisor is found, add
both members of its divisor pair, avoiding a duplicate for perfect squares.
Sort the collected divisors before returning them.

- Time: `O(sqrt(n) + k log k)`, where `k` is the number of divisors
- Space: `O(k)`
