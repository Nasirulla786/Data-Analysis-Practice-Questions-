import pandas as pd

data = {"RollNo": [101, 102, 103, 104, 105, 106, 107, 108], "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan", "Kavya", "Arjun", "Simran"], "Department": ["BCA", "BCA", "MCA", "BCA", "MCA", "MCA", "BCA", "MCA"], "Age": [20, 21, 22, 20, 23, 22, 21, 24], "Marks": [85, 92, 67, 78, 88, 95, 55, 73]}
print(pd.DataFrame(data).columns)
