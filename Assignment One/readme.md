# 🐍 Python String Class Assignment  

## 📌 Overview  
This assignment covers Python string fundamentals, including string literals, methods, and formatting techniques. It consists of four parts:  

1️⃣ **String Literals** – Single, double, and triple quotes  
2️⃣ **String Methods** – Modifying and manipulating text  
3️⃣ **F-Strings** – String interpolation  
4️⃣ **Combining Methods with F-Strings** – Creating a user profile  

---

## 📖 Topics Covered  

### **1️⃣ String Literals**  
🔹 **Single Quotes (`'...'`)** – Used for short strings.  
🔹 **Double Quotes (`"..."`)** – Used when a string contains an apostrophe.  
🔹 **Triple Quotes (`'''...'''` or `"""..."""`)** – Used for multi-line strings and docstrings.  

Example:  
```python
single = 'Hello, Python!'
double = "It's a great language!"
triple = """This is 
a multi-line string."""
```

---

### **2️⃣ String Methods**  
✅ **Case Conversion:** `.upper()`, `.lower()`, `.title()`  
✅ **Trimming & Replacing:** `.strip()`, `.replace("old", "new")`  
✅ **Counting & Searching:** `.count("char")`, `.startswith("word")`, `.find("word")`  

Example:  
```python
text = "  Python is amazing!  "
print(text.strip())  # Removes spaces
print(text.replace("amazing", "powerful"))  # Replaces a word
print(text.count("i"))  # Counts occurrences of 'i'
```

---

### **3️⃣ F-Strings (String Interpolation)**  
Used for formatting strings dynamically.  

Example:  
```python
name = "Taha"
age = 16
language = "Python"

print(f"My name is {name} and I am {age} years old.")
print(f"I love coding in {language}!")
```

---

### **4️⃣ Combining String Methods & F-Strings**  
📌 **User Profile Generator** – Takes user input, formats it, and generates a profile.  

Example:  
```python

current_year = 2025
first = input("First Name: ").capitalize()
last = input("Last Name: ").capitalize()
birth_year = int(input("Birth Year: "))

username = f"{first[0].lower()}{last.lower()}{birth_year}"
age = current_year - birth_year

print(f"Profile: {first} {last}, Age: {age}, Username: {username}")
```

---

## 🔥 Run the Assignment  
Clone the repository and execute the script:  
```bash
git clone https://github.com/Tahasaif3/Python-Class-Assignments.git
cd Python-Class-Assignments
python python_string_class_assignment_1.py
```

---

## 📌 Completed By  
**Taha Saif** 🚀  

---

⭐ **If you found this useful, give it a star on GitHub!** ⭐  
