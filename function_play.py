def main():
    health = 100
    name = input("What is your name? ")
    i = 0
    while i < 10:
        print(name[i::])
        i+=1

main()