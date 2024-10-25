def main():
    n = int(input("Enter a number: "))
    fizz_buzz(n)

def fizz_buzz(n):
    x = 1
    a = []
    i = 1
    for x in range(1, n + 1):
        a.append(x)

    for i in a:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
main()