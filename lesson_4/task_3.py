exercise_number = int(input("Кое число искаш да упражняваш?: "))

for number in range(1, 11):
    result = exercise_number * number
    print(f"{number} * {exercise_number} = {result}")
