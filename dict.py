Student={
    "name":"Alice",
    "age":"18",
    "course":"Btech"
}
print(Student)

for i,j in Student.items():
    print(f"{i} : {j}")

del Student["age"]
print(Student)    

Student["DOB"] = "04/07/2006"
print(Student)