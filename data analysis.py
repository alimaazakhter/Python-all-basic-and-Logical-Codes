import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("employees.csv")

job_counts = df['JOB_ID'].value_counts()
dept_counts = df['DEPARTMENT_ID'].value_counts().sort_index()

#Bar Graph
plt.bar(job_counts.index, job_counts.values, color='green')
plt.xlabel("Job ID")
plt.ylabel("Number of Employees")
plt.title("Employees per Job ID")
plt.show()

#Line Graph
plt.plot(dept_counts.index, dept_counts.values, marker="o", color="green")
plt.xlabel("Department ID")
plt.ylabel("Number of Employees")
plt.title("Employees by Department (Line Plot)")
plt.show()

#Histogram
plt.hist(df['DEPARTMENT_ID'], bins=10, color='orange', edgecolor='black')
plt.xlabel("Department ID")
plt.ylabel("Number of Employees")
plt.title("Department Frequency")
plt.show()

#Scatter Plot
plt.scatter(df['DEPARTMENT_ID'], df['SALARY'], color='blue', alpha=0.6)
plt.xlabel("Department ID")
plt.ylabel("Salary")
plt.title("Salary Distribution by Department")
plt.show()

#pie chart
subjects=['c', 'java', 'python', 'maths', 'mysql']
marks=[20, 45, 60, 30, 70]

col = ['Blue', 'Red', 'Green', 'Yellow', 'Purple']
ex=[0, 0.1, 0, 0]
plt.pie(marks, labels=subjects, colors=col explode=ex, autopct='%1.1f%%', shadow=True)
plt.title("Marks of all Subjects")
plt.show()


