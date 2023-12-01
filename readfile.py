# Writing to a file
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"Error writing to the file: {e}")

# Reading from a file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content read from {file_name}:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading from the file: {e}")

# Example usage
if __name__ == "__main__":
    # Writing to a file
    file_name = "sample_file.txt"
    content_to_write = "Hello, this is a sample content.\nPython File Handling is fun!"

    write_to_file(file_name, content_to_write)

    print("\n")

    # Reading from a file
    read_from_file(file_name)
