def nasobeni(numbers):
    total = 1
    for x in numbers:
        total = total * x
    return total
print(nasobeni((-1,5,20,17)))