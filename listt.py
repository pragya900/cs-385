# List Printing Program

# Sample list
my_list = [1, 2, 3, 4, 5]

# Method 1: Print the entire list
print("1. Print the entire list:")
print(my_list)

# Method 2: Iterate and print each element using a for loop
print("\n2. Iterate and print each element using a for loop:")
for item in my_list:
    print(item, end=" ")
print()

# Method 3: Print using the join method to concatenate elements with a separator
print("\n3. Print using the join method to concatenate elements with a separator:")
print(' '.join(map(str, my_list)))

# Method 4: Using list comprehension to print each element
print("\n4. Using list comprehension to print each element:")
[print(item, end=" ") for item in my_list]
print()

# Method 5: Using the * operator to print each element with a custom separator
print("\n5. Using the * operator to print each element with a custom separator:")
print(*my_list, sep=" ")

# Method 6: Using the format function with a formatted string
print("\n6. Using the format function with a formatted string:")
print("List: {}".format(my_list))

# Method 7: Using f-strings for a concise and readable format
print("\n7. Using f-strings for a concise and readable format:")
print(f"List: {my_list}")
