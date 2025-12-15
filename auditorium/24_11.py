#1

password = input("Введите пароль: ")
while len(password) < 8:
    print("Пароль слишком короткий. Попробуйте снова")
    password = input("Введите пароль:")
print("Пароль принят!")

#2

commands = ('start', 'stop', 'pause', 'quit')

print("Доступные команды:", ', '.join(commands))
print("Для выхода введите 'quit'")

while True:
    new_command = input("Введите команду: ").strip().lower()
    if new_command in commands:
        print(f"Выполняю команду: {new_command}")
        
        if new_command == 'quit':
            print("Выход из программы.")
            break
    else:
        print("Неизвестная команда.")

#3
shopping_list = []

while True:
    print("Выберите действие:")
    print("1 - Добавить товар")
    print("2 - Удалить товар")
    print("3 - Показать список")
    print("4 - Выйти")
    
    choice = input("Ваш выбор (1-4): ").strip()
    
    if choice == '1':
        item = input("Введите название товара для добавления: ").strip()
        if item:
            shopping_list.append(item)
    
    elif choice == '2':
        item = input("Введите название товара для удаления: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"Товар '{item}' не найден в списке")
    
    elif choice == '3':
        if not shopping_list:
            print("Список покупок пуст")
        else:
            print("Ваш список покупок: ")
            for i, item in enumerate(shopping_list, 1):
                print(f"  {i}. {item}")
            print(f"Всего товаров: {len(shopping_list)}")
    
    elif choice == '4':
        print("До свидания!")
        break

    #4
emails = set( )
while True:
    email = input("Введите email адрес: ")
    emails.add(email)

    if email == "":
        break
print(f"Все адреса: {sorted(list(emails))}")

#5

phrases = ["Hi there!",  "Bye! Have a nice day", "I'm a program, but thanks for asking"]

while True:
    text = input("Напишите что-нибудь: ")
    if text == "hello":
        print(phrases[0])
    elif text == question:
        print(phrases[2])
    elif text == "exit":
        print(phrases[1])
        break

#6

numbers = [2, 4, 6, 8, 10]
total = sum(numbers)
print(total)

#7

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Длина слова: {len(fruit)}")

#8

text = "Python"
i = 0
for i in range(len(text)):
print(f"Символ {i+1}: {text[i]}")
i = i + 1

#9
numbers = [3, 7, 2, 9, 5]
result = [number * 2 for number in numbers]
print(result)  

animals = ["cat", "elephant", "dog", "butterfly"]
print([animal for animal in animals if len(animal) > 3])

person = ("Иванов", "Иван", "Иванович")
result = tuple(word.lower() for word in person)
print(result)