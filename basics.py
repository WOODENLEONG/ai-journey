# 1. return vs print
# 2. Why print(result) gave NameError: result is local to c_to_f
# 3. git add / commit / push

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
    result=(temp*9/5) +32
    return result
# Example usage
print(c_to_f(0))  # Should print 32.0
print(c_to_f(100))  # Should print 212.0
print(c_to_f(-40))  # Should print -40.0


# Part 4: Break it on purpose
# WIrh print: c_to_f(30) shows 86.0, but gives back None, because print() does not return a value.  
# so f = None and f+1 gives TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'  
# With return: f = 86.0 and f+1 gives 87.0
f=c_to_f(30)
print(f+1) 


#Part 5: for loops
for c in range (0,101,10):
    print(c, "C = ", c_to_f(c), "F")

# Part 6: Scope test
# Prediction: print(result) will fail, because result only lives inside c_to-f().
print(c_to_f(25))
# print(result) #NameError: result is local to c_to_f
f = c_to_f(25)
print(f)  
# works: 77.0, return brings the value out
