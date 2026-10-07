fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

fruits.append("mango")
print("After append:", fruits)

fruits.insert(1, "orange")
print("After insert:", fruits)

fruits.extend(["grape", "kiwi"])
print("After extend:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.pop()
print("After pop:", fruits)

fruits.sort()
print("After sort:", fruits)

fruits.reverse()
print("After reverse:", fruits)

print("Index of cherry:", fruits.index("cherry"))
print("Count of apple:", fruits.count("apple"))

print()

t = (10, 20, 30, 20, 40)
print("Tuple:", t)
print("First element:", t[0])
print("Slice t[1:4]:", t[1:4])
print("Length:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Max:", max(t))
print("Min:", min(t))
print("Sum:", sum(t))

t = t + (50,)
print("After adding 50:", t)

temp = list(t)
temp.remove(20)
t = tuple(temp)
print("After removing 20:", t)

print()

student = {"name": "Amit", "age": 20, "course": "Python"}
print("Dictionary:", student)

student["city"] = "Pune"
print("After adding city:", student)

student["age"] = 21
print("After changing age:", student)

print("Get name:", student.get("name"))

student.update({"grade": "A", "year": 2})
print("After update:", student)

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

student.pop("year")
print("After pop:", student)

student.popitem()
print("After popitem:", student)

del student["course"]
print("After del:", student)

student.clear()
print("After clear:", student)
