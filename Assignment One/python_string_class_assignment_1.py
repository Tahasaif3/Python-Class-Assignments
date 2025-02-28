# -*- coding: utf-8 -*-
"""python_string_class_assignment_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15QNwSTSU_ZhSSR6LEUy5FnVFu0BO6Gro

**Python Strings Assignment Part 1**
"""

# Part 1: Understanding String Literals
# Q1. Create three different strings using each type of quotation:
# Single quotes ('example')
# Double quotes ("example")
# Triple quotes ("""example""")

# Single Quotes
single_quote_string = 'Hello, World! I am Learning Python'
print(single_quote_string);

# Double Quotes
double_quote_string = "\nPython is a powerful language and easy to learn"
print(double_quote_string);

# Triple Quotes
triple_quote_string = """
He said, "Python is awesome!"
Isn't it?
Yeah it is awesome!
"""
print(triple_quote_string);

# Q2. Explain in your own words: What is the advantage of each type of quotation?
# Answer:
### **Single, Double, and Triple Quotes in Python**  

#### **1. Single Quotes (`'...'`)**  
# Single Quotes are used for short, one-line strings.  
# They are used when the string does not contain apostrophes (`'`) to keep code neat and clean.  
# name = 'John'
# message = 'Hello, world!'

#### **2. Double Quotes (`"..."`)**  
# Double Quotes are also used for short, one-line strings.  
# They are used when the string contains an apostrophe (`'`) to avoid escaping.
# text = "It's a sunny day"
# quote = "She said, \"Python is great!\""

#### **3. Triple Quotes (`'''...'''` or `"""..."""`)**  
# Triple Quotes are used for multi-line strings and documentation (docstrings).  
# They are used when writing multi-line text or function/class documentation.  
# multi_line = '''This is  
# a multi-line string.'''

# def greet():
#     """Prints a greeting message."""
#     print("Hello!")

# ✔ **Single/Double for short strings**  
# ✔ **Triple for multi-line & docstrings** 

# Q3. Write a string that contains both single and double quotes inside it.
text = '''Today I learned advanced OOP in Python, and I had an amazing experience!
"It's really fun and useful in python.'''
print(text);

# Q4. Create a multi-line string using triple quotes that describes your favorite
# hobby.
my_hobbies = """
My favorite hobbies are:

1. Coding: I enjoy solving problems and building applications
   that can make life easier or more enjoyable. The process
   of writing code and debugging it gives me a sense of
   accomplishment and it is a fun doing coding.

2. Traveling: Exploring new places and experiencing different
   cultures broadens my perspective. I love travelling at night especially long
   drives. at night are the best moment in my life

3. Spending Time Alone: I value my alone time as it allows
   me to reflect, recharge, and engage in personal interests
   such as reading using mobile watching movies and learning new things.
"""

print(my_hobbies);

"""**Python String Assignment Part 2**"""

# Part 2: String Methods Practice
# Q1. Create a variable full_name with your full name (first and last name).Then
# write code to:
# Print your name in all uppercase letters
# Print your name in all lowercase letters
# Print your name with the first letter of each name capitalized

full_name = "Taha saif"
print(full_name.upper());
print(full_name.lower());
print(full_name.title());

# Q2. Create a variable messy_text = " Python programming is fun! " Then write
# code to:
# Remove all the extra spaces at the beginning and end
# Replace "fun" with "amazing"
# Count how many times the letter 'i' appears

messy_text = " Python programming is fun! "
print(messy_text.strip());
print(messy_text.replace("fun","amazing"));
print(messy_text.count("i"));


# Q3. Create a variable sentence = "The quick brown fox jumps over the lazy dog"
# Then write code to:
# Split this sentence into a list of words
# Join the words back together with dashes between them
# Check if the sentence starts with "The"
# Find the position of the word "fox"

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.split());
print('-'.join(sentence.split()));
print(sentence.startswith("The"));
print(sentence.find("fox"));

"""**Python String Assignment Part 3**"""

# Part 3: F-Strings
# Q1. Create variables for:
# Your name
# Your age
# Your favorite programming language
# Then use f-strings to create these sentences:
# "My name is {your_name} and I am {your_age} years old."
# "I enjoy programming in {language}, it's my favorite!"
# Create a math expression inside an f-string: "In 5 years, I will be {age + 5}
# years old."

my_name = "Taha Saif"
my_age = 16
language = "Python"

print(f"My name is {my_name} and I am {my_age} years old.");
print(f"I enjoy programming in {language}, it's my favorite!");

"""**Python String Assignment Part 4**"""

# Part 4: Combining String Methods with F-Strings
# Create a program that:
# 1. Asks for user input about their first name, last name, and birth year
# 2. Uses string methods to properly capitalize their name
# 3. Uses f-strings to create a profile message: "Profile: {First Last}, Age:
# {calculated age},
# Username: {first initial + last name + birth year}


current_year = 2025

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))

first_name = first_name.capitalize()
last_name = last_name.capitalize()

age = current_year - birth_year

username = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"

profile_message = f"Profile: {first_name} {last_name}, Age: {age}, Username: {username}"

print(profile_message)

""" Completed By Taha Saif"""
