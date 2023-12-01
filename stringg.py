# String Operations Program

# Function to check if a string is a palindrome
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Function to count the occurrence of each character in a string
def count_characters(string):
    char_count = {}
    for char in string:
        if char.isalpha():
            char_lower = char.lower()
            char_count[char_lower] = char_count.get(char_lower, 0) + 1
    return char_count

# Function to reverse words in a sentence
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

# Example usage
input_string = "Python is awesome! Do you agree?"

print("Original String:", input_string)
print("Is Palindrome:", is_palindrome(input_string))
print("Character Count:", count_characters(input_string))
print("Reversed Words:", reverse_words(input_string))
