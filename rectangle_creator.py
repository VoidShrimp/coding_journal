rows = int(input("How many rows do you want? "))
columns = int(input("How many columns? "))

for x in range(rows):
    for y in range (columns):
        print("*", end="")
    print("")

