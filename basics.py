# Part 1: Variables
age = int(input("Age?"))
print(age+1)


# Part 2: if/else
temp=int(input("Temperature?"))
if temp > 35:
    print("Overheat")
else:
    print("OK")


# Part 3: Functions
def c_to_f(temp):
    return (temp *9/5) +32
# Example usage
print(c_to_f(0))  # Should print 32.0
print(c_to_f(100))  # Should print 212.0
print(c_to_f(-40))  # Should print -40.0


# Part 4: Break it on purpose
# Try calling the function with a string instead of a number
# print(c_to_f("0"))  # This will cause a TypeError
def c_to_f(temp):
    return (temp *9/5) +32
f=c_to_f(30)
print(f+1)  # This will cause a TypeError because f is None


#Part 5: for loops
for c in range (0,101,10):
    print(c, "C = ", c_to_f(c), "F")
