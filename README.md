# DSA With Python

Daily practice solutions for learning data structures and algorithms with Python.

## Topics

| Topic | Problems |
| --- | --- |
| Basic Math | [Palindrome number](<Basic Math/palindrome.py>), [Armstrong number](<Basic Math/armstrong_number.py>), [Print divisors](<Basic Math/print_divisors.py>) |

## Complexity notes

| Problem | Time | Space |
| --- | --- | --- |
| Palindrome number | O(d) | O(1) |
| Armstrong number | O(d) | O(d) |
| Print divisors | O(sqrt(n) + k log k) | O(k) |

## Project conventions

- Use descriptive, lowercase `snake_case` filenames for new solutions.
- Put the main logic in a reusable function.
- Keep command-line input/output inside `if __name__ == "__main__":`.
- Keep a problem statement, approach, and complexity analysis in each topic
  folder's `README.md`.
- Add short comments for non-obvious algorithm steps.
- Do not commit generated files such as `__pycache__`; these are excluded by `.gitignore`.

## Running a solution

From the repository root:

```powershell
python "Basic Math\palindrome.py"
python "Basic Math\armstrong_number.py"
python "Basic Math\print_divisors.py"
```

## Uploading to GitHub

Create a new empty repository on GitHub, then run these commands from this folder:

```powershell
git init
git add .
git commit -m "Add basic math DSA practice"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

For future practice:

```powershell
git status
git add .
git commit -m "Add <problem name> solution"
git push
```
