greet_text = "Привет,"
print(greet_text)

name = input("Введите имя: ")
print("Привет," + name + "!")

surname = input("Введите фамилию: ")
name +=  surname
print("Привет," + name + "!")

age = input("Введите возраст: ")
print("User:", name + surname, "\n", "Age:" + age)