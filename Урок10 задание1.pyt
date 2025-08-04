pets = {}

name = input("Введите имя питомца: ")
type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")


pets[name] = {
    'Вид питомца': type,
    'Возраст питомца': age,
    'Имя владельца': owner
}

if age % 10 == 1 and age % 100 != 11:
    year = "год"
elif 2 <= age % 10 <= 4 and not (11 <= age % 100 <= 14):
    year = "года"
else:
    year = "лет"

print(f"Это {name}.")
print(f"{name} — {pets[name]['Вид питомца']}.")
print(f"Его возраст: {age} {year}.")
print(f"Имя владельца: {pets[name]['Имя владельца']}.")

print("\nИнформация о питомце через keys() и values():")
keys_list = list(pets[name].keys())
values_list = list(pets[name].values())

print("Ключи:", keys_list)
print("Значения:", values_list)