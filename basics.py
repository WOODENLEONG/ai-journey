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