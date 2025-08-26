def example_w_plus_mode():
    with open("example_w+.txt", "w+") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.seek(0)
        comtent = file.read()
        print(comtent)
example_w_plus_mode()