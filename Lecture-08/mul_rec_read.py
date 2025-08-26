import struct
with open("records.bin", "rb") as file:
    record_size = struct.calcsize('i20sif')
    while True:
        data = file.read(record_size)
        if not data:
            break
        rec_id, rec_name, rec_age, rec_gpa = struct.unpack('i20sif', data)
        print(f"ID: {rec_id}, Name: {rec_name.decode().strip()}, Age: {rec_age}, GPA: {rec_gpa:.2f}")