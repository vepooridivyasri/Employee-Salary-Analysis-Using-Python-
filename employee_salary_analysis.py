import pandas as pd

# Load the dataset
df = pd.read_csv("employee_salary.csv")

# Display the dataset
print("Employee Dataset")
print(df)

print("\nTotal Employees:", len(df))

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nDepartment-wise Employee Count:")
print(df["Department"].value_counts())
import matplotlib.pyplot as plt
import seaborn as sns

# Bar Chart - Department-wise Employee Count
plt.figure(figsize=(6,4))
sns.countplot(x="Department", data=df)
plt.title("Department-wise Employee Count")
plt.show()

# Bar Chart - Salary by Employee
plt.figure(figsize=(8,4))
sns.barplot(x="Name", y="Salary", data=df)
plt.title("Employee Salary")
plt.xticks(rotation=45)
plt.show()