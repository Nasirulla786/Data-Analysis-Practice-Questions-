import pandas as pd

data = {"RollNo": [101, 102, 103, 104, 105, 106, 107, 108], "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan", "Kavya", "Arjun", "Simran"], "Department": ["BCA", "BCA", "MCA", "BCA", "MCA", "MCA", "BCA", "MCA"], "Age": [20, 21, 22, 20, 23, 22, 21, 24], "Marks": [85, 92, 67, 78, 88, 95, 55, 73]}
df = pd.DataFrame(data)
df["Rank"] = df["Marks"].rank(ascending=False).astype(int)
df["Grade"] = pd.cut(df["Marks"], bins=[-1, 59, 69, 79, 89, 100], labels=["D", "C", "B", "A", "A+"])
df["Result"] = df["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")
merit_list = df[["Rank", "RollNo", "Name", "Department", "Marks", "Grade", "Result"]].sort_values("Marks", ascending=False)
print(merit_list)
merit_list.to_excel("student_merit_list.xlsx", index=False)
print("Saved as student_merit_list.xlsx")
