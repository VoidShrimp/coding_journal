def binary_search(numbers, target):
    l = 0
    h = len(numbers) - 1

    while l <= h:
        m = int((h + l) / 2)
        if numbers[m] == target:
            print(numbers[m])
            break
        elif numbers[m] > target:
            h = m - 1
        else:
            l = m + 1

binary_search([0,1,2,3,4,5,6,7,8,9], 2)