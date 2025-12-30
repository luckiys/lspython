# Triangle Validator & Area Calculator

Validates if three sides can form a valid triangle and calculates the area using Heron's formula.

## Features

- Triangle inequality validation
- Area calculation using Heron's formula
- Input validation with continue/exit options
- User-friendly prompts and error messages

## Skills Demonstrated

- Functions with return values
- Math library (sqrt)
- Input validation
- While loops with break conditions
- Mathematical computations

## How to Run

```bash
python3 triangle_validator.py
```

## Sample Output

```
==========================================
*       Triangle Validator & Calculator      *
==========================================

Enter the three sides of the triangle:
  Side 1: 3
  Side 2: 4
  Side 3: 5

Validating the triangle...

✓ This is a valid triangle!
  Area = 6.00 square units

Would you like to try another triangle? (y/n):
```

## Algorithm

Uses Heron's formula:
- Semi-perimeter: `s = (a + b + c) / 2`
- Area: `√(s × (s-a) × (s-b) × (s-c))`

