with open('employees.txt', 'r') as emp_file:
    line = emp_file.readline()
    while line != '':
        print(line.strip())
        line = emp_file.readline()