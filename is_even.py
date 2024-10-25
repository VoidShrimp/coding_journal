def main():
    number = int(input("Enter a number: "))
    is_even(number)

def is_even(number):
    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
main()