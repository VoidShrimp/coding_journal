def main():
    run = True

    while run:
        print("Enter a non-negative number: ")
        n = int(input())
        if n < 0:
            print("Invalid number, try again")
            run = True
        elif n >= 0:
            answer = factorial(n)
            print(f"The factorial of {n} is {answer}.")
            run = False
        else:
            print("Error, please try again")
            run = True

def factorial(n):

    total = n
    for i in range(1, n):
        total *= i
    return total

main()