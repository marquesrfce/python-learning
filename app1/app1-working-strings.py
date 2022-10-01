# Python program that takes input from the user, apply string methods and display it to the user

# Get input from the user asking for the full name
name = input("Enter your full name: ")

# Apply the 'title' method to the given string in order to make each word begin with a capital letter
name_in_title = name.title()

# Apply the 'upper' method in order to make all letters upper case
name_in_upper = name.upper()

# Apply the 'lower' method in order to make all letters lower case
name_in_lower = name.lower()

# Print the variables values to the user
print(f"The name as you typed: {name}")
print(f"The name with each word starting with upper case: {name_in_title}")
print(f"The name with each letter in upper case: {name_in_upper}")
print(f"The name with each letter in lower case: {name_in_lower}")
