#Implement Python programs to perform string manipulation, text processing, and file handling for real-world applications.
text = input("Enter a string: ")

print("Original string:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Reversed string:", text[::-1])
print("Length:", len(text))
print("Number of words:", len(text.split()))

# Search for a substring
word = input("Enter a word to search: ")

if word.lower() in text.lower():
    print("Word found")
else:
    print("Word not found")

# Replace a word
old = input("Enter word to replace: ")
new = input("Enter replacement: ")

print("Updated string:", text.replace(old, new))

import re
from collections import Counter

text = input("Enter a sentence or paragraph: ")

# Extract words and normalize to lowercase
words = re.findall(r"\b\w+\b", text.lower())

word_count = Counter(words)

print("Total words:", len(words))
print("Unique words:", len(word_count))
print("Word frequencies:")

for word, count in word_count.most_common():
    print(word, ":", count)
    
#file Manipulation Function
filename = "sample.txt"

# Write to a file
with open(filename, "w", encoding="utf-8") as file:
    file.write("Python is easy to learn.\n")
    file.write("Python supports file handling.\n")

print("Data written successfully.")

# Append to the file
with open(filename, "a", encoding="utf-8") as file:
    file.write("File handling is useful.\n")

print("Data appended successfully.")

# Read the entire file
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile contents:")
print(content)

# Count lines
print("Number of lines:", len(content.splitlines()))

#Real world Example: Text File analyzer
import re
from collections import Counter
from pathlib import Path

def analyze_file(filename):
    path = Path(filename)

    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except OSError as error:
        print("Error reading file:", error)
        return

    words = re.findall(r"\b\w+\b", text.lower())
    frequencies = Counter(words)

    report = [
        "TEXT ANALYSIS REPORT",
        "--------------------",
        f"File: {filename}",
        f"Lines: {len(text.splitlines())}",
        f"Words: {len(words)}",
        f"Characters: {len(text)}",
        f"Unique words: {len(frequencies)}",
        "",
        "Top 10 words:"
    ]

    for word, count in frequencies.most_common(10):
        report.append(f"{word}: {count}")

    report_text = "\n".join(report)

    try:
        Path("report.txt").write_text(
            report_text + "\n", encoding="utf-8"
        )
    except OSError as error:
        print("Error writing report:", error)
        return

    print(report_text)
    print("\nReport saved to report.txt")

if __name__ == "__main__":
    analyze_file("article.txt")
#file
from pathlib import Path

def search_replace(input_file, output_file, old_word, new_word):
    try:
        text = Path(input_file).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print("Unable to read file:", error)
        return

    count = text.count(old_word)
    updated_text = text.replace(old_word, new_word)

    try:
        Path(output_file).write_text(
            updated_text, encoding="utf-8"
        )
    except OSError as error:
        print("Unable to save file:", error)
        return

    print("Occurrences replaced:", count)
    print("Updated file saved as:", output_file)

source = input("Enter input filename: ")
destination = input("Enter output filename: ")
old = input("Enter word to find: ")
new = input("Enter replacement word: ")

search_replace(source, destination, old, new)from pathlib import Path

def search_replace(input_file, output_file, old_word, new_word):
    try:
        text = Path(input_file).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print("Unable to read file:", error)
        return

    count = text.count(old_word)
    updated_text = text.replace(old_word, new_word)

    try:
        Path(output_file).write_text(
            updated_text, encoding="utf-8"
        )
    except OSError as error:
        print("Unable to save file:", error)
        return

    print("Occurrences replaced:", count)
    print("Updated file saved as:", output_file)

source = input("Enter input filename: ")
destination = input("Enter output filename: ")
old = input("Enter word to find: ")
new = input("Enter replacement word: ")

search_replace(source, destination, old, new)
