def main():
    sentence = (input("Enter a sentence: "))
    count_vowels(sentence)

def count_vowels(sentence):
    counter = 0
    for x in sentence:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            counter = counter + 1
    print(counter)

main()