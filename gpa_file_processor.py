"""
GPA File Processor
------------------
Reads student data from a file, processes GPAs, assigns letter grades,
and writes results to an output file.

Author: Lakulish Saini
"""

def get_letter_grade(gpa):
    """Convert GPA to letter grade."""
    if gpa >= 3.99:
        return "A+"
    elif gpa >= 3.8:
        return "A"
    elif gpa >= 3.5:
        return "B"
    elif gpa >= 3.0:
        return "C"
    elif gpa >= 2.5:
        return "D"
    else:
        return "F"


def main():
    try:
        # Open input and output files
        infile = open("sample_data/CNIT155Input.txt", "r")
        outfile = open("sample_data/CNIT155Output.txt", "w")
        
        # Initialize lists for names and scores
        names = []
        scores = []
        
        # Read and parse data from file
        for line in infile:
            parts = line.strip().split(",")
            names.append(parts[0].title())  # Title case the name
            scores.append(float(parts[1]))
        
        # Display file contents
        print("Printing the contents of the file...")
        print(f"Names: {names}")
        print(f"Scores: {scores}")
        
        # Find and write maximum score
        max_score = max(scores)
        outfile.write(f"Maximum score is {max_score:.2f}\n")
        
        # Write students with maximum score
        for i in range(len(scores)):
            if scores[i] == max_score:
                outfile.write(f"{names[i]}, {scores[i]:.2f}\n")
        
        # Apply curve and assign letter grades
        print()
        outfile.write("\nUpdated scores with letter grade:\n")
        
        for i in range(len(scores)):
            # Add 0.1 curve, cap at 4.0
            new_score = min(scores[i] + 0.1, 4.0)
            grade = get_letter_grade(new_score)
            
            # Write to output file
            outfile.write(f"{names[i]}, {new_score:.2f}, {grade}\n")
        
        # Close files
        infile.close()
        outfile.close()
        
        print("✓ Results written to CNIT155Output.txt")
        
    except FileNotFoundError:
        print("Error: Could not open the file.")
        print("Make sure the input file exists in the sample_data folder.")


if __name__ == "__main__":
    main()

