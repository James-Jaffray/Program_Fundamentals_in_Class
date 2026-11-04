import csv

def read_books(file_path):
    books = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
            return books

books = read_books("books.csv")
for book in books:
    print(book["Title"], "-", book["Author"])




import csv

def save_scores(file_path, scores):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ["Name", "Score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in scores:
            writer.writerow(entry)

scores = [{"Name": "Alice", "Score": 95}, {"Name": "Bob", "Score": 88}]
save_scores("scores.csv", scores)





students = read_books("students.csv") # Assume each row has "Grade" and "Name"
passed = [s for s in students if int(s["Grade"]) >= 60]
print("Students who passed:")
for s in passed:
    print(s["Name"])




def update_prices(file_path):
    products = read_books(file_path)
    for p in products:
        p["Price"] = str(float(p["Price"]) * 1.1) # Increase price by 10%
    save_scores(file_path, products)
update_prices("products.csv")