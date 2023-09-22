words = []
search_words =  ['Python', 'C', 'OOP', 'Hello', 'Java', 'PHp']

file_path = 'input.txt'

with open(file_path, 'r') as file:
    file_content = file.read()
    words = file_content.split()

lowercase_words = [word.lower() for word in words]

for word in search_words:
    occurrence = lowercase_words.count(word.lower())
    print('{} -> {}'.format(word, occurrence))