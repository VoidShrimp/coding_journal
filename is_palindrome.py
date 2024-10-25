def main():
    word = input("Enter a word: ")
    is_palindrome(word)

def is_palindrome(word):
    new_word = word.lower()
    if new_word  == new_word[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
    print(new_word[::-1])

main()