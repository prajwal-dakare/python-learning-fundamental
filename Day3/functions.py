# FUNCTION 1

def add(a, b):
    return a + b

# FUNCTION 2

def multiply(a, b):
    return a * b

# FUNCTION 3

def square(n):
    return n * n

# USER INPUT

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("\n----- FUNCTION OUTPUT -----")

print("Addition =", add(x, y))
print("Multiplication =", multiply(x, y))
print("Square of first number =", square(x))
