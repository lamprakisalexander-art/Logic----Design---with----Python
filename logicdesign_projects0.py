x = int(input("Enter 0 or 1 \n")) #inputing the 1rst number
Fx = (x == 1) #transforming the input into a boolean form
print(Fx)
y = int(input("Enter 0 or 1 \n")) #inputing the 2nd number
Fy = (y == 1) #transforming the input into a boolean form
print(Fy)

# AND Gate Truth Table:
# x | y | Output (x · y)
# 0 | 0 | 0 (False)
# 0 | 1 | 0 (False)
# 1 | 0 | 0 (False)
# 1 | 1 | 1 (True)

def AND(Fx,Fy): # function for logic gate AND
    return Fx and Fy

print(f" {x} and {y} is: {int(AND(Fx,Fy))} \n")

# OR Gate Truth Table:
# x | y | Output (x + y)
# 0 | 0 | 0 (False)
# 0 | 1 | 1 (True)
# 1 | 0 | 1 (True)
# 1 | 1 | 1 (True)

def OR(Fx,Fy): # function for logic gate OR
    return Fx or Fy
print(f" {x} or {y} is{int(OR(Fx,Fy))} \n")

# NOT Gate Truth Table:
# x | Output (x')
# 0 | 1 (True)
# 1 | 0 (False)

print(f"not {x} is: {int(not(Fx))} and not {y} is: {int(not(Fy))} \n") #logic gate NOT

# XOR Gate Truth Table:
# 0 XOR 0 = 0 (False)
# 0 XOR 1 = 1 (True) different
# 1 XOR 0 = 1 (True) different
# 1 XOR 1 = 0 (False)

def XOR(Fx,Fy): # function for logic gate XOR
    return (not Fx and Fy) or (Fx and not Fy) # or x'*y + x*y'

print(f"{x} xor {y} is: {int(XOR(Fx,Fy))} \n")

# XNOR Gate Truth Table:
# x | y | Output (!(x ⊕ y))
# 0 | 0 | 1 (True)  same inputs
# 0 | 1 | 0 (False)
# 1 | 0 | 0 (False)
# 1 | 1 | 1 (True) same inputs

def XNOR(Fx,Fy): # function for logic gate XNOR which is just !XOR
    return not XOR(Fx,Fy)

print(f"{x} xnor {y} is: {int(XNOR(Fx,Fy))} \n")