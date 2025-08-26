def example_a_plus_mode():
    with open("example_w+.txt", "a+") as file:
        file.seek(0)
        
        content = file.read()
        print("Before appending:")
        print(content)

        file.write("Appending a new line.\n")

        file.seek(0)
        updated_content = file.read()
        print("After appending:")
        print(updated_content)
example_a_plus_mode()