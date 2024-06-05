# Завдання 1
a = float(input("Введіть перше число : "))
b = float(input("Введіть друге число : "))
c = float(input("Введіть третє число : "))
d = float(input("Введіть четверте число : "))

# Завдання 2
addition = a + b
subtraction = c - d
multiplication = a * c
division = b / d if d != 0 else None  
exponentiation = a ** b
integer_division = c // d if d != 0 else None  
modulus = a % b

results = [addition, subtraction, multiplication, division, exponentiation, integer_division, modulus]
print("Отримані результати:", results)

# Завдання 3
length_of_results = len(results)
print("Кількість елементів у списку результатів:", length_of_results)

print("Парні елементи списку результатів:")
for result in results:
    if isinstance(result, (int, float)) and result % 2 == 0:
        print(result)

# Завдання 4
if length_of_results >= 5:
    results[1], results[4] = results[4], results[1]

print("Список після заміни другого та п'ятого елементів:", results)

# Завдання 5
name = input("Введіть ваше прізвище та ім'я: ")

print("\nВиконав дану лабораторну роботу:")
print(name)
