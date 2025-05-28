class Department:
    total_departments = 0

    def __init__(self, dept_id, name, location, dept_head):
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.dept_head = dept_head
        Department.total_departments += 1

    def display_dept(self):
        print("\nDepartment Information")
        print("----------------------")
        print(f"ID        : {self.dept_id}")
        print(f"Name      : {self.name}")
        print(f"Location  : {self.location}")
        print(f"Head      : {self.dept_head}")


departments = []


num_departments = int(input("Enter the number of departments: "))
for i in range(num_departments):
    print(f"\nEnter details for department {i+1}:")
    dept_id = int(input("ID: "))
    name = input("Name: ")
    location = input("Location: ")
    dept_head = input("Department Head: ")
    dept = Department(dept_id, name, location, dept_head)
    departments.append(dept)


print("\nAll Departments:")
for dept in departments:
    dept.display_dept()


print(f"\nTotal departments: {Department.total_departments}")


search_id = int(input("\nEnter dept ID to search: "))
found = False
for dept in departments:
    if dept.dept_id == search_id:
        print("\nDepartment Found:")
        dept.display_dept()
        found = True
        break
if not found:
    print("Department with that ID not found.")


search_name = input("\nEnter dept name to search: ").lower()
found = False
for dept in departments:
    if dept.name.lower() == search_name:
        print("\nDepartment Found:")
        dept.display_dept()
        found = True
        break
if not found:
    print("Department with that name not found.")


"""Enter the number of departments: 2

Enter details for department 1:
ID: 1
Name: CSE
Location: Hyd
Department Head: Hod

Enter details for department 2:
ID: 2
Name: IT
Location: Banglore
Department Head: Hod2

All Departments:

Department Information
----------------------
ID        : 1
Name      : CSE
Location  : Hyd
Head      : Hod

Department Information
----------------------
ID        : 2
Name      : IT
Location  : Banglore
Head      : Hod2

Total departments: 2

Enter dept ID to search: 2

Department Found:

Department Information
----------------------
ID        : 2
Name      : IT
Location  : Banglore
Head      : Hod2

Enter dept name to search: CSE

Department Found:

Department Information
----------------------
ID        : 1
Name      : CSE
Location  : Hyd
Head      : Hod"""