# Dictionary Methods Program

# Create a dictionary
student_info = {
    'name': 'John Doe',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'English', 'Science']
}

# Method 1: Accessing values
print("1. Accessing values:")
print("Name:", student_info['name'])
print("Age:", student_info.get('age'))
print("Courses:", student_info.get('courses'))

# Method 2: Adding a new key-value pair
print("\n2. Adding a new key-value pair:")
student_info['gender'] = 'Male'
print("Updated Dictionary:", student_info)

# Method 3: Updating a value
print("\n3. Updating a value:")
student_info['age'] = 21
print("Updated Age:", student_info['age'])

# Method 4: Removing a key-value pair
print("\n4. Removing a key-value pair:")
removed_grade = student_info.pop('grade')
print("Removed Grade:", removed_grade)
print("Updated Dictionary:", student_info)

# Method 5: Checking if a key exists
print("\n5. Checking if a key exists:")
has_course_key = 'courses' in student_info
print("Does 'courses' key exist?", has_course_key)

# Method 6: Getting keys, values, and items
print("\n6. Getting keys, values, and items:")
keys = student_info.keys()
values = student_info.values()
items = student_info.items()
print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Method 7: Clearing the dictionary
print("\n7. Clearing the dictionary:")
student_info.clear()
print("Cleared Dictionary:", student_info)
