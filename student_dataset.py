import csv

students = [
           {
            "Student ID": "ST001",
            "Department": "Computer Science",
            "Level": 200,
            "Attendance percentage": 85,
            "Average Examination Score": 85
           },
           {
            "Student ID": "ST002",
            "Department": "Accounting",
            "Level": 100,
            "Attendance percentage": 65,
            "Average Examination Score": 75
           },
           {
            "Student ID": "ST003",
            "Department": "Cybersecurity",
            "Level": 300,
            "Attendance percentage": 25,
            "Average Examination Score": 15
           },
           {
            "Student ID": "ST004",
            "Department": "Architecture",
            "Level": 200,
            "Attendance percentage": 85,
            "Average Examination Score": 85
           },
           {
            "Student ID": "ST005",
            "Department": "Mass Communication",
            "Level": 300,
            "Attendance percentage": 76,
            "Average Examination Score": 74
           },
           {
            "Student ID": "ST006",
            "Department": "Software Engineering",
            "Level": 400,
            "Attendance percentage": 95,
            "Average Examination Score": 89
           },
           ]

print(students)

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file,
fieldnames=["Student ID",
            "Department",
            "Level",
            "Attendance percentage",
            "Average Examination Score"
            ])
    writer.writeheader()
    writer.writerows(students)

print("Dataset caved successfully!")