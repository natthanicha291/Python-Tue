import os

print(f'Operating System: {os.name}')
print(f'Current Working Directory: {os.getcwd()}')
os.mkdir("test_dir")
print(f"Directory 'test_dir' created.")