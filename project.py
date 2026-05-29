import pandas as pd

data = pd.read_csv("students.csv")

print(data)

print("Average Marks:")
print(data["Marks"].mean())