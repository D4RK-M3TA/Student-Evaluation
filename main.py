import csv
import tkinter as tk
from tkinter import ttk

def read_student_marks(file_path):
    students = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                t1 = float(row['T1'].replace(',', '.')) if row['T1'] else 0
                t2 = float(row['T2'].replace(',', '.')) if row['T2'] else 0
                t3 = float(row['T3'].replace(',', '.')) if row['T3'] else None
                if t3 is not None:
                    test_marks = (t1 + t2 + t3) / 3
                else:
                    test_marks = (t1 + t2) / 2
                students.append({
                    'StudentNo': row['STUDENT NO.'],
                    'TestMarks': test_marks,
                    'T1': t1,
                    'T2': t2,
                    'T3': t3,
                    'SemesterMarks': float(row['SM'].replace(',', '.'))
                })
            except ValueError as e:
                print(f"Skipping row due to error: {e}")
    return students

def evaluate_students(students):
    qualified_students = []
    at_risk_students = []
    distinction_students = []

    for student in students:
        if student['T1'] < 25 or student['T2'] < 25 or (student['T3'] is not None and student['T3'] < 25):
            if student['SemesterMarks'] >= 40:
                qualified_students.append(student['StudentNo'])
            else:
                at_risk_students.append(student['StudentNo'])
        else:
            qualified_students.append(student['StudentNo'])
        
        if student['SemesterMarks'] >= 75:
            distinction_students.append(student['StudentNo'])
            
    return qualified_students, at_risk_students, distinction_students, len(students)

def display_results(qualified_students, at_risk_students, distinction_students, total_students):
    root = tk.Tk()
    root.title("Student Evaluation Results")

    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='Qualified Students')
    tab_control.add(tab2, text='At Risk Students')
    tab_control.add(tab3, text='Distinction Students')

    tab_control.pack(expand=1, fill='both')

    qualified_label = tk.Label(tab1, text="Qualified to write the exam:")
    qualified_label.pack(pady=10)

    qualified_listbox = tk.Listbox(tab1)
    for student_no in qualified_students:
        qualified_listbox.insert(tk.END, student_no)
    qualified_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    at_risk_label = tk.Label(tab2, text="At risk of failing the exam:")
    at_risk_label.pack(pady=10)

    at_risk_listbox = tk.Listbox(tab2)
    for student_no in at_risk_students:
        at_risk_listbox.insert(tk.END, student_no)
    at_risk_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    distinction_label = tk.Label(tab3, text="Qualified with distinction:")
    distinction_label.pack(pady=10)

    distinction_listbox = tk.Listbox(tab3)
    for student_no in distinction_students:
        distinction_listbox.insert(tk.END, student_no)
    distinction_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Display statistics
    qualified_count = len(qualified_students)
    at_risk_count = len(at_risk_students)
    distinction_count = len(distinction_students)
    qualified_percentage = (qualified_count / total_students) * 100
    at_risk_percentage = (at_risk_count / total_students) * 100
    distinction_percentage = (distinction_count / total_students) * 100

    stats_label = tk.Label(root, text=f"Total Students: {total_students}\n"
                                      f"Qualified Students: {qualified_count} ({qualified_percentage:.2f}%)\n"
                                      f"At Risk Students: {at_risk_count} ({at_risk_percentage:.2f}%)\n"
                                      f"Distinction Students: {distinction_count} ({distinction_percentage:.2f}%)")
    stats_label.pack(pady=10)

    root.mainloop()

def main():
    file_path = "SMTA022 Marks 2024 New update.csv"
    students = read_student_marks(file_path)
    qualified_students, at_risk_students, distinction_students, total_students = evaluate_students(students)
    display_results(qualified_students, at_risk_students, distinction_students, total_students)

if __name__ == "__main__":
    main()
