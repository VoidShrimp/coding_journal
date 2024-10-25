def main():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = int(input("Enter your third number: "))
    find_max(a, b, c)

def find_max(a, b, c):
    finder = (a, b, c)
    if finder[0] >= finder[1] and finder[0] >= finder [2]:
        print(finder[0])
    elif finder[1] >= finder[0] and finder[1] >= finder [2]:
        print(finder[1])
    elif finder[2] >= finder[0] and finder[2] >= finder [1]:
        print(finder[2])
    else:
        print("Error")

main()