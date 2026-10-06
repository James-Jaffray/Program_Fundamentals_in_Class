word = input('Enter a word for us to count vowels: ').lower()
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
vowelcount = 0


for letter in word:
    print(letter)
    if letter in vowel:
        vowelcount = vowelcount + 1

print(f'There are {vowelcount} vowels in {word}')

    
        