# For цикъл
for number in range(1, 11):
    print(number)


# While цикъл
hungry = True  # False
bites = 0  # хапки

while hungry:
    print("Още една хапка")
    bites = bites + 1  # bites += 1

    if bites > 3:
        hungry = False

print("Вече не съм гладна.")
