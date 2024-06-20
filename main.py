def main():
    book_to_count = "./books/frankenstein.txt"
    
    print(f"----- Beginning of book report for {book_to_count} -----")

    book = get_book(book_to_count)

    print(f"Total number of words: {count_words(book)}")
    character_count_dict = count_characters(book)
    ch_list = char_dict_to_list(character_count_dict)

    for char_count in ch_list:
        print(f"The character {char_count['char']} appears {char_count['num']} times")


def count_words(text):
    return len(text.split())

def get_book(path):
    with open(path) as file:
        return file.read()

def count_characters(text):
    character_count = {}
    
    for character in text:
        character = character.lower()
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

def char_dict_to_list(ch_dict):

    ch_list = []

    for char in ch_dict:
        if char.isalpha():
            ch_list.append(
                    {"char":char,
                     "num":ch_dict[char]})
    
    def sort_criteria(dict):
        return dict["num"]


    ch_list.sort(reverse=True, key=sort_criteria)

    return ch_list

main()
