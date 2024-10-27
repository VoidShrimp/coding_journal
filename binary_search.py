def binary_search(numbers, target):
    l = 0
    h = len(numbers) - 1

    while l <= h:
        m = int((h + l) / 2)
        guess = [m]
        counter = 0
        if guess[counter] == target:
            print(guess[counter])
            break
        elif guess[counter] > target:
            h = m - 1
            counter+=1
        else:
            l = m + 1
            counter += 1

binary_search([0,1,2,3,4,5,6,7,8,9], 5)