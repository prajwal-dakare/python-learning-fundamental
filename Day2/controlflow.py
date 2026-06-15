marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
#Upgrade to if-elif-else
marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Distinction")

elif marks >= 60:
    print("First Class")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")
#Learn For Loop
print("\nFOR LOOP")

for i in range(1, 6):
    print(i)
#Learn While Loop
print("\nWHILE LOOP")

i = 1

while i <= 5:
    print(i)
    i += 1  
#Learn Break
print("\nBREAK EXAMPLE")

for i in range(10):

    if i == 5:
        break

    print(i)
#Learn Continue
print("\nCONTINUE EXAMPLE")

for i in range(10):

    if i == 5:
        continue

    print(i)
