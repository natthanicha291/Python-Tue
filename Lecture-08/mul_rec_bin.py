import struct
num_records = int(input("Hoe many record do you want to create: "))
with open("records.bin", "wb") as file:
    for i in range(num_records):
        rec_id = int(input("ID : "))
        rec_name = input("Name : ")
        rec_age = int(input("Age : "))
        rec_gpa = float(input("GPA : "))
        data = struct.pack('i20sif', rec_id, rec_name.encode(), rec_age, rec_gpa)
        file.write(data)