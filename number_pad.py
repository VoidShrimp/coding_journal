number_pad = [[1,2,3],[4,5,6],[7,8,9],["#",0,"*"]]
for number in number_pad:
    for digit in number:
        print(digit, end=" ")
    print()