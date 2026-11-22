import pickle
import shelve
import os


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Create an object
student = Student("Vikash", 241505, 92)

# Save and restore using pickle
pickle_file = "student_data.pkl"

with open(pickle_file, "wb") as file:
    pickle.dump(student, file)

with open(pickle_file, "rb") as file:
    restored_student = pickle.load(file)

print("OBJECT RESTORED USING PICKLE")
restored_student.display()

# Save and restore using shelve
shelf_file = "student_records"

with shelve.open(shelf_file) as database:
    database["student_1"] = student

with shelve.open(shelf_file) as database:
    saved_student = database["student_1"]

print("\nOBJECT RESTORED USING SHELVE")
saved_student.display()

# Remove generated files after demonstration
if os.path.exists(pickle_file):
    os.remove(pickle_file)

for extension in ("", ".db", ".dat", ".bak", ".dir"):
    path = shelf_file + extension
    if os.path.exists(path):
        os.remove(path)
