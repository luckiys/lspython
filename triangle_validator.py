"""
Triangle Validator & Area Calculator
-------------------------------------
Validates if three sides can form a valid triangle and
calculates the area using Heron's formula.

Author: Lakulish Saini
"""

import math


def display_header():
    """Display program header."""
    print("=" * 42)
    print("*       Triangle Validator & Calculator      *")
    print("=" * 42)
    print()


def is_valid_triangle(side1, side2, side3):
    """
    Check if three sides can form a valid triangle.
    Triangle inequality: sum of any two sides must be greater than the third.
    """
    return (side1 + side2 > side3 and 
            side1 + side3 > side2 and 
            side2 + side3 > side1)


def calculate_area(side1, side2, side3):
    """
    Calculate the area of a triangle using Heron's formula.
    Area = sqrt(s * (s-a) * (s-b) * (s-c))
    where s is the semi-perimeter.
    """
    semi_perimeter = (side1 + side2 + side3) / 2
    area = math.sqrt(semi_perimeter * 
                     (semi_perimeter - side1) * 
                     (semi_perimeter - side2) * 
                     (semi_perimeter - side3))
    return area


def get_yes_no_input(prompt):
    """Get and validate yes/no input from user."""
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def main():
    display_header()
    
    running = True
    while running:
        # Get triangle sides from user
        print("Enter the three sides of the triangle:")
        side1 = float(input("  Side 1: "))
        side2 = float(input("  Side 2: "))
        side3 = float(input("  Side 3: "))
        
        print()
        print("Validating the triangle...")
        
        # Validate and calculate
        if is_valid_triangle(side1, side2, side3):
            area = calculate_area(side1, side2, side3)
            print()
            print("✓ This is a valid triangle!")
            print(f"  Area = {area:.2f} square units")
        else:
            print()
            print("✗ Invalid triangle. The sides do not satisfy the triangle inequality.")
            print("  (Sum of any two sides must be greater than the third)")
        
        print()
        running = get_yes_no_input("Would you like to try another triangle? (y/n): ")
    
    print()
    print("Thank you for using Triangle Validator!")


if __name__ == "__main__":
    main()

