import sys
import string

def get_book_content(book_path):
    with open(book_path) as book:
        return book.read()

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_char_dic(book_text):
    book_text = book_text.lower()
    char_dic = {}
    
    # loop through the string and record characters
    for char in book_text:
        if (char not in char_dic):
            char_dic[char] = 1
        else:
            char_dic[char] = char_dic[char] + 1
    return char_dic

def print_report(char_dic):
    char_list = []

    # remove characters not in the alphabet
    for c, num in char_dic.items():
        if (c.isalpha()):
            char_list.append({"char": c, "num": num})

    def sort_on(dic):
        return dic["num"]

    char_list.sort(reverse=True, key=sort_on)
    
    # print report
    for dic in char_list:
        print(f"The character {dic["char"]} was found {dic["num"]} times")

def main() -> None:
    book_path = "books/frankenstein.txt"
    frank_book = get_book_content(book_path)

    # word and character counts
    word_count = get_word_count(frank_book)
    char_dic = get_char_dic(frank_book)
    
    # Report
    print(f"""
--- Begin report of {book_path} ---
{word_count} words found in the document
          """)

    print_report(char_dic)

    print(f"""
 --- End report --- 
    """)



if __name__ == "__main__":
    sys.exit(main())
