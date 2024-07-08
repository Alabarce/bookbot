def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    ordered_characters = sort_dict(characters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document ")
    for char, count in ordered_characters:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    split_text = text.split()
    return len(split_text)

def character_count(text):
    char_dictionary = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for char in text.lower():
        if char in char_dictionary:
            char_dictionary[char] += 1
    return char_dictionary

def sort_dict(dictionary):
    new_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse = True)
    return new_dictionary

main()