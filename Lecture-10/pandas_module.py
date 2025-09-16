import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

arverage_age = df['Age'].mean()
print(f"\nAverage Age: {arverage_age}")

filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):\n", filtered_df)

df['Salary'] = [70000, 80000, 60000, 90000]
print("\nDataFrame with Salary:\n", df)