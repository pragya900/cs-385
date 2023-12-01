#arithematic operator
#declearing two variables a and b initialising their values as 10 and 5 reapectively
a = 10
b = 5

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor_division = a // b
exponentiation = a ** b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Floor Division:", floor_division)
print("Exponentiation:", exponentiation)

#compariosn operators
x = 10
y = 20

print("Is x equal to y?", x == y)
print("Is x not equal to y?", x != y)
print("Is x less than y?", x < y)
print("Is x greater than y?", x > y)
print("Is x less than or equal to y?", x <= y)
print("Is x greater than or equal to y?", x >= y)

#assignment operator
x = 10

x += 5  # Equivalent to x = x + 5
print("x after addition:", x)

x -= 3  # Equivalent to x = x - 3
print("x after subtraction:", x)

x *= 2  # Equivalent to x = x * 2
print("x after multiplication:", x)

x /= 4  # Equivalent to x = x / 4
print("x after division:", x)

x %= 2  # Equivalent to x = x % 2
print("x after modulus:", x)

x //= 3 # Equivalent to x = x // 3
print("x after floor division:", x)

x **= 3 # Equivalent to x = x ** 3
print("x after exponentiation:", x)

#logical operator
p = True
q = False

logical_and = p and q
logical_or = p or q
logical_not_p = not p
logical_not_q = not q

print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT for p:", logical_not_p)
print("Logical NOT for q:", logical_not_q)

#memnership operator
my_list = [1, 2, 3, 4, 5]

print("Is 3 in the list?", 3 in my_list)
print("Is 6 not in the list?", 6 not in my_list)

#identity operator 
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("Are x and y the same object?", x is y)
print("Are x and z the same object?", x is z)
print("Are x and z different objects?", x is not z)
print(y is z)
