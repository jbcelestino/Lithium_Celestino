#Code 1
def greet_students(name, nChar):
    for i in range(nChar):
        print(name[i])

name = input("Enter a Name: ") 
nChar = input("Input any numeric number: ")
nChar = int(nChar)
greet_students(name, nChar)

#a. The output will be:   J, o, s, e, p (printed on seperate lines). This is because the code loops 5 times and it prints characters from index 0-4 of the string.

#b. An error occurs after printing the full name because the code loops 20 times but the string only has 18 characters (0-17, accessing 18 throws an error).

#c. You can use try-except or the len() function.

#Fixed code using len()
def greet_students(name, nChar):
    limit = min(nChar, len(name))
    for i in range(limit):
        print(name[i])

name = input("Enter a Name: ") 
nChar = input("Input any numeric number: ")
nChar = int(nChar)
greet_students(name, nChar)

#Code 2
def greet_students(name, nChar):
    for i in range(nChar):
        print(name[0: nChar])

name = input("Enter a Name: ") 
greet_students(name, len(name))

#a. The error is that the line for i in range (nChar) is missing a colon. I fixed simply by adding one.

#b.
def greet_students(name, nChar):
    for i in range(nChar):
        print(name[0: nChar - i]) 

name = input("Enter a Name: ") 
greet_students(name, len(name))

#Code 3
n = 0
while n < 1 or n > 100:
    n = input("Enter a number from 1 to 100: ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))

#a. Code with function/s that will return the sum of all squared numbers from 1 to n
def sum_of_squared(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 2
    return total_sum

n = 0
while n < 1 or n > 100:
    n = input("Enter a number from 1 to 100: ")
    n = int(n)

print(f"Sum of all squared numbers is {sum_of_squared(n)}.")

 