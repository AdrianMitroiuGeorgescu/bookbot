def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def get_words_count(text: str) -> int :
    words = text.split()
    return len(words)

def get_words_appearence(text: str) -> dict:
    char_appenrence = {}
    
    for char in text:
        char = char.lower()
        if not char.isalpha():
            continue 
        if char in char_appenrence:
            char_appenrence[char] += 1
        else:
            char_appenrence[char] = 1
    
    return char_appenrence

def sort_on(d):
    return d["num"]

def sort_dict(char_dict: dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(words_count: int, char_list: list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print("")
    
    for char in char_list:
        print(f"The '{char['char']}' character was found {char['num']}")
    
    print("--- End report ---")

def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = get_words_count(text)
    char_appenrence = get_words_appearence(text)
    char_list = sort_dict(char_appenrence)
    
    report(words_count, char_list)

main()
