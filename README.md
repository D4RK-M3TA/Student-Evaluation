# Student-Evaluation
Collecting workspace information

# Student Marks Evaluation

This project reads student marks from a CSV file, evaluates their performance, and displays the results using a graphical user interface (GUI).

## Files

- `SMTA022 Marks 2024 New update.csv`: CSV file containing student marks.
- 

Student.py

: Python script to read, evaluate, and display student marks.

## Requirements

- Python 3.x
- 

tkinter

 library (usually included with Python)

## Usage

1. Ensure the CSV file (`SMTA022 Marks 2024 New update.csv`) is in the same directory as 

Student.py

.
2. Run the 

Student.py

 script:

```sh
python Student.py
```

## Functionality

### Reading Student Marks

The script reads student marks from the CSV file using the 

read_student_marks

 function. It processes the following columns:

- `STUDENT NO.`
- `T1`, `T2`, `T3` (Test marks)
- `SM` (Semester marks)

### Evaluating Students

The 

evaluate_students

 function categorizes students into three groups:

- **Qualified Students**: Students who are qualified to write the exam.
- **At Risk Students**: Students at risk of failing the exam.
- **Distinction Students**: Students who qualified with distinction.

### Displaying Results

The 

display_results

 function uses 

tkinter

 to display the results in a GUI with three tabs:

- Qualified Students
- At Risk Students
- Distinction Students

It also displays statistics about the total number of students and the percentages of each category.

## Example

After running the script, a window will appear showing the categorized student numbers and statistics.

## License

This project is licensed under the MIT License.