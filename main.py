
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    lowercase = file_contents.lower()
    letter_counts = {}
    for letter in lowercase:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


def get_words_from_file(file_path):
    with open(file_path) as f:
        return f.read()



def main():
    book = "books/frankenstein.txt"
    file_contents = get_words_from_file(book)
    print(f"--- Begin report of {book} ---")
    print(f"{count_words(file_contents)} words found in document")
    count_dictionary = count_characters(file_contents)
    keys = list(count_dictionary.keys())
    keys.sort()
    for key in keys:
        if key.isalpha():
            print(f"The '{key}' was found {count_dictionary[key]} times")
    print(f"--- End report of {book} ---")

main()

