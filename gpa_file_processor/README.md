# GPA File Processor

Reads student data from a file, processes GPAs, assigns letter grades, and writes results to an output file.

## Features

- Read and parse CSV-formatted data
- Find maximum scores
- Apply grade curves (+0.1 with 4.0 cap)
- Convert GPA to letter grades (A+, A, B, C, D, F)
- Write formatted results to output file
- Exception handling for missing files

## Skills Demonstrated

- File I/O (reading and writing)
- Exception handling (try/except)
- String parsing with split()
- List operations
- Data processing

## How to Run

```bash
python3 gpa_file_processor.py
```

## Input File Format (student_data.txt)

```
john smith,3.5
jane doe,3.8
bob wilson,2.9
```

## Output

Results are written to `results.txt` with:
- Maximum score identification
- Updated scores with letter grades

