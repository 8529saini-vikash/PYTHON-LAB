import pandas as pd
import os

file_name = input("Enter CSV file name: ")

if not os.path.exists(file_name):
    data = {
        "Name": ["Aman", "Ravi", "Vikash", "Neha", "Rahul"],
        "Age": [20, 21, 20, 22, 21],
        "Marks": [85, 72, 91, 68, 88],
        "City": ["Delhi", "Jaipur", "Alwar", "Delhi", "Jaipur"]
    }

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print("\nSample CSV file created.")

df = pd.read_csv(file_name)

print("\nDataset:")
print(df)

print("\nDataset Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

column = input("\nEnter column name for filtering: ")
value = input("Enter value to filter: ")

filtered_data = df[df[column].astype(str) == value]

print("\nFiltered Data:")
print(filtered_data)

output_file = "filtered_data.csv"
filtered_data.to_csv(output_file, index=False)

print("\nFiltered data saved to:", output_file)
