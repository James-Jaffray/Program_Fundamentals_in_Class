people = {
    'dan' : 'april 14th',
    'gary' : 'june 23rd',
    'richard' : 'february 2nd',
    'jessica' : 'october 30th',
    'mary' : 'december 25th'
}


name = input("Who's birthday do you want to look up?").lower()

if name in people:
    print(f"{name}'s Birthday is", people[name])
else:
    print(f"Sorry, we don't have {name}'s birthday.")

