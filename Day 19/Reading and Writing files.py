# Reading a file
def read_file(filename):
    with open(filename, 'r') as f: # We use the open() function to open the file, and use the 'r' mode to read.
        lines = f.readlines() # f.readline() reads one line at a time.
    return lines

for line in read_file("notes.txt"):
    print(line.strip())

# Handling Missing Files
def safe_read(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

print(safe_read("missing.txt"))

# Writing to a file
def write_file(filename, text):
    with open(filename, 'a') as f:
        # 'w' overwrites
        # 'a' appends to it.
        f.write(text + "\n")

write_file("notes.txt", "Remember to review Python file I/O.")

# User Interaction Example
filename = "todo.txt"
while True:
    action = input("Add (a), Read (r), or Quit (q)? ").lower()
    if action == "a":
        item = input("Enter a to-do item: ")
        write_file(filename, item)
    elif action == "r":
        for line in read_file(filename):
            print("-", line.strip())
    elif action == "q":
        break