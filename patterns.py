# Pattern 1: Square
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("* ", end="")
        print()

# Pattern 2: Right-angled Triangle
def print_triangle(size):
    for i in range(1, size + 1):
        for j in range(i):
            print("* ", end="")
        print()

# Pattern 3: Inverted Right-angled Triangle
def print_inverted_triangle(size):
    for i in range(size, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()

# Pattern 4: Pyramid
def print_pyramid(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)

# Pattern 5: Diamond
def print_diamond(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)
    for i in range(size - 1, 0, -1):
        print(" " * (size - i) + "* " * i)

# Change the size based on your preference
size = 5

print("Square:")
print_square(size)
print("\nRight-angled Triangle:")
print_triangle(size)
print("\nInverted Right-angled Triangle:")
print_inverted_triangle(size)
print("\nPyramid:")
print_pyramid(size)
print("\nDiamond:")
print_diamond(size)
