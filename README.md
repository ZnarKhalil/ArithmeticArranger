# Arithmetic Arranger

This repository is a solution for the [FreeCodeCamp Scientific Computing with Python - Arithmetic Formatter](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter) problem.
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. This Python project provides a function that receives a list of strings representing arithmetic problems and returns the problems arranged vertically and side-by-side.

## Functionality

The `arithmetic_arranger` function formats arithmetic problems and can optionally display the answers.

### Examples

```python
from arithmetic_arranger import arithmetic_arranger

# Example 1
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))
# Output:
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

# Example 2
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems, True))
# Output:
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
```

## Error Handling

The function provides meaningful error messages for various scenarios:

- Too many problems: "Error: Too many problems."
- Incorrect operator: "Error: Operator must be '+' or '-'."
- Non-digit characters in operands: "Error: Numbers must only contain digits."
- Numbers exceeding four digits: "Error: Numbers cannot be more than four digits."

## Testing

Unit tests are located in `test_module.py`. Tests run automatically when you hit the "run" button. Alternatively, run the tests by inputting `pytest` in the console.
