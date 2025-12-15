#1

hse_coordinates = (59.9339, 30.3061) 
math_constants = (3.14159, 2.71828, 1.61803)
students_id = (22234, 22235, 22236)

x = "программирование"
print(tuple(x))

#2

numbers = [10, 20, 30]
numbers.append(40)        
numbers.remove(20)   
numbers.insert(0, 5)    
print(numbers)

#3

rgb = (255, 128, 0)
print(rgb[1])
rgb[0] = 200 
TypeError: 'tuple' object does not support item assignment

#4
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1 & set2
print("1. Общие элементы (пересечение):", intersection)
union = set1 | set2
print("2. Все уникальные элементы (объединение):", union)
difference = set1 - set2
print("3. Элементы из set1, которых нет в set2:", difference)

#5
mixed_data = [
    1, "hello", 3.14, [1, 2], 42, "world", 0, (5, 6),
    {"name": "John"}, True, {7, 8, 9}
]

int_list = []
str_list = []
float_list = []
list_list = []
tuple_list = []
dict_list = []
bool_list = []
set_list = []
other_list = []

for item in mixed_data:
    if isinstance(item, int) and not isinstance(item, bool):
        int_list.append(item)
    elif isinstance(item, str):
        str_list.append(item)
    elif isinstance(item, float):
        float_list.append(item)
    elif isinstance(item, list):
        list_list.append(item)
    elif isinstance(item, tuple):
        tuple_list.append(item)
    elif isinstance(item, dict):
        dict_list.append(item)
    elif isinstance(item, bool):
        bool_list.append(item)
    elif isinstance(item, set):
        set_list.append(item)
    else:
        other_list.append(item)

print("Целые числа:", int_list)
print("Строки:", str_list)
print("Дробные числа:", float_list)
print("Списки:", list_list)
print("Кортежи:", tuple_list)
print("Словари:", dict_list)
print("Логические значения:", bool_list)
print("Множества:", set_list)
print("Другие типы:", other_list)

#6
count = 1
while count <= 5:
    print(count)
    count += 1

print("Цикл завершен!")

#7
while True:
    word = input("Введите слово: ")
    
    if word.lower() == "стоп":
        break
    
    letters = list(word)
    print(letters)

#8
correct_password = "secret123"
logged_in = False
attempts = 0
max_attempts = 3

while logged_in == False and attempts < max_attempts:
    user_password = input("Введите пароль: ")
    attempts = attempts + 1

    if user_password == correct_password:
        logged_in = True
        attempts = 0
        print("Вы успешно вошли в систему")
    else:
        print("Пароль неверный")
    if attempts == max_attempts:
        print("Количество попыток истекло")