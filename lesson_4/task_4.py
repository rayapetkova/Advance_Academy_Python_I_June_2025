name = input("Как се казваш?: ")
color = input("Кой ти е любимият цвят?: ")
food = input("Коя е любимата ти храна?: ")
animal = input("Кое е любимото ти животно?: ")
favourite_number = int(input("Кое е любимото ти число от 1 до 15?: "))

for number in range(1, favourite_number + 1):
    print(f"Ти сега имаш {number} опашки.")

print(f"Ти си {color} {food}{animal} с {favourite_number} опашки! Супергерой с име {name}!💥")
