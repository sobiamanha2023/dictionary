students = {
    "101": {"name": "Nishaj", "age": 12,"grade": "6"},
    "102": {"name": "Rahim", "age": 13, "grade": "7"},
    "103": {"name": "Karim", "age": 12, "grade": "6"}
}

print("Original Dictionary: ")
print(students)

#ACCESING ITEMS
print("\nAccess studen 101:", students["101"])
print("Get with .get():", students.get("102"))

#ADDING ITEMS
students["104"] = {"name": "Hasan", "age": 14, "grade": "8"}
print("\nAfter Adding New Students:")
print(students)

# UPDATING ITEMS
students["103"]["age"] = 13
print("\nAfter Updating Student 103's Age: ")
print(students)

# REMOVING ITEMS
#pop by key
removed = students.pop("102")
print("\nRemoved Student 102:", removed)
print("After pop():", students)

#DICTIONARY METHODS
print("\nKeys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())

#copy dictionary
copy_students = students.copy()
print("\nCopy of students:", copy_students)

#update dictionary
students.update({"103": {"name": "Karim", "age": 12, "grade": "6"}})
print("\nAfter update():", students)

#setdefault() get value, or insert default
val = students.setdefault("104", {"name": "Hasan", "age": 14, "grade": "8"})
print("\nAfter setdefault():", students)