import functools

def log_activity(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

student_records = []
@log_activity
def add_student(name, age, *grades, **additional_info):
    student = {
        "name": name,
        "age": age,
        "grades": list(grades),
    }
    student.update(additional_info)
    student_records.append(student)

# Function to calculate and display results
@log_activity
def calculate_results():
    for student in student_records:
        grades = student.get("grades", [])
        if grades:
            average = sum(grades) / len(grades)
            student["average"] = average
            student["status"] = "Pass" if average >= 50 else "Fail"
        else:
            student["average"] = None
            student["status"] = "No grades available"

@log_activity
def display_records():
    for student in student_records:
        print("-" * 30)
        for key, value in student.items():
            print(f"{key.capitalize()}: {value}")

# Example Usage
add_student("Harshini", 21, 75, 90, 75, major="Computer Science")
add_student("Charitha", 21, 45, 50, 55, major="Mathematics")
add_student("Manaswini", 22, 70, 65, major="Physics")
add_student("Sindhu", 24, major="History") 

calculate_results()
display_records()

"""Function 'add_student' called with args: ('Harshini', 21, 75, 90, 75) kwargs: {'major': 'Computer Science'}
Function 'add_student' returned: None
Function 'add_student' called with args: ('Charitha', 21, 45, 50, 55) kwargs: {'major': 'Mathematics'}
Function 'add_student' returned: None
Function 'add_student' called with args: ('Manaswini', 22, 70, 65) kwargs: {'major': 'Physics'}
Function 'add_student' returned: None
Function 'add_student' called with args: ('Sindhu', 24) kwargs: {'major': 'History'}
Function 'add_student' returned: None
Function 'calculate_results' called with args: () kwargs: {}
Function 'calculate_results' returned: None
Function 'display_records' called with args: () kwargs: {}
------------------------------
Name: Harshini
Age: 21
Grades: [75, 90, 75]
Major: Computer Science
Average: 80.0
Status: Pass
------------------------------
Name: Charitha
Age: 21
Grades: [45, 50, 55]
Major: Mathematics
Average: 50.0
Status: Pass
------------------------------
Name: Manaswini
Age: 22
Grades: [70, 65]
Major: Physics
Average: 67.5
Status: Pass
------------------------------
Name: Sindhu
Age: 24
Grades: []
Major: History
Average: None
Status: No grades available
Function 'display_records' returned: None"""