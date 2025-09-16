import numpy as np

random_matrix = np.random.randint(1, 11,(3, 3))
print(f"Random Array:\n{random_matrix}")

matrix_sum = np.sum(random_matrix)
print(f"Sum of all elements: {matrix_sum}")

matrix_mean = np.mean(random_matrix)
print(f"Mean of all elements: {matrix_mean}")

transposed_matrix = np.transpose(random_matrix)  
print(f"Transposed Matrix:\n{transposed_matrix}")