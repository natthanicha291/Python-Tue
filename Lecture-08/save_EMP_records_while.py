num_emps = int(input("Enter number of employees: "))
with open("employees.txt", "w") as emp_file:
    for count in range(1, num_emps + 1):
        print(f"Enter details of employee ,count:")
        emp_name = input("Employee Name: ")
        emp_id = input("Employee ID: ")
        emp_sdept = input("Department: ")
        emp_file.write(emp_name + "\n" + emp_id + "\n" + emp_sdept + "\n")
print("Employee details saved to employees.txt")