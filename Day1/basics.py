# VARIABLES

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
# STRING

print("\n----- STRING -----")
print("Upper Case:", name.upper())
print("Lower Case:", name.lower())
print("Length:", len(name))

# LIST

print("\n----- LIST -----")
subjects = ["Maths", "Physics", "Python"]
subjects.append("Electronics")

print(subjects)

# TUPLE

print("\n----- TUPLE -----")
colors = ("Red", "Green", "Blue")

print(colors)

# DICTIONARY

print("\n----- DICTIONARY -----")
student = {
    "Name": name,
    "Age": age,
    "Branch": "ENTC"
}

print(student)
