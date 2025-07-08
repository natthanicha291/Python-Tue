hours_work = int(input("Enter the number of hours worked: "))
pay_rate = int(input("Enter the hourly pay rate: "))
    
if hours_work <= 40:
    gross_pay = ((hours_work - 40) * 1.5 * pay_rate) + (40 * pay_rate)
else:
    gross_pay = hours_work * pay_rate
    
print("The gross pay is: ",gross_pay)