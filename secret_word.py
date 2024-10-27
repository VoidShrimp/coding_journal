part_one = "LMN"
part_two = "EO"
part_one_length = len(part_one)
part_two_length = len(part_two)
secret_word = "PIZZA"
counter_one = 0
counter_two = 0
secret = []

while counter_one < part_one_length or counter_two < part_two_length:
    if counter_one < part_one_length:
        secret.append(part_one[counter_one])
        counter_one+=1
    if counter_two < part_two_length:
        secret.append(part_two[counter_two])
        counter_two += 1

for letters in secret:
    print(letters, end="")