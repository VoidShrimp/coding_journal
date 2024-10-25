foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (or press q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for {food}: $"))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food)

for price in prices:
    total += price

print(total)
