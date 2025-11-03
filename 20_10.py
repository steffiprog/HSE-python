
# Задача 1. Форматирование ФИО
full_name = "иванов иван иванович"
surname, name, patronymic = full_name.split()
result = f"{surname.title()} {name[0].upper()}.{patronymic[0].upper()}."
print(result)
# Ожидаемый вывод: "Иванов И.И."

# Задача 2. Анализ пароля
password = "Password123"
print(len(password))
# Проверьте:
# - длину не менее 8 символов
# - содержит цифры
# - содержит заглавные буквы
length_ok = len(password) >= 8
has_digits = any(char.isdigit() for char in password)  
has_upper = password != password.lower()
print(f"Длина OK: {length_ok}")
print(f"Есть цифры: {has_digits}")
print(f"Есть заглавные: {has_upper}")

# Задача 3. Обработка пути к файлу
path = "/home/user/documents/report.pdf"
filename = path.split("/")[-1]
filename_2 = filename.split(".")[0]
print("Имя файла без расширения: " + filename_2)
# Ожидаемый вывод: "report"

# Задача 4. Поиск телефона
text = "Звоните по номеру +7-123-456-78-90 или +7-987-654-32-10"
# Найдите все номера телефонов (содержат +7-)
text = text.split()
for word in text:
    if word.startswith("+7"):
        print(word)

# Задача 5. Нормализация текста
text = "   ЭТОТ ТЕКСТ ПИСАЛИ КАПСОМ    "
# Приведите к нормальному виду: первая буква заглавная, остальные маленькие
print(f"До: '{text}'")
print(f"После: '{text.strip().capitalize()}'")
# Ожидаемый вывод: "Этот текст писали капсом"

# Задача 6: Подсчет слов
sentence = "Быстрый рыжий лис прыгает через ленивую собаку"
# Посчитайте количество слов в предложении
word_count = len(sentence.split())
print(word_count)
# Ответ: 7

# Задача 7: Замена даты
text = "Встречаемся 2023-12-31 в 20:00"
# Замените формат даты на 31.12.2023
import re
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3.\2.\1', text)
print(new_text)  # "Встречаемся 31.12.2023 в 20:00"

# Задача 8: Валидация имени файла
filename = "my_document.backup.pdf"
# Проверьте, является ли файл PDF-документом
pdf = filename.endswith('.pdf')
print(pdf)

# Задача 9: Разбор URL
url = "https://example.com/category/product.html"
# Извлеките домен и имя страницы
import re
match = re.search(r'https?://([^/]+)/.*/([^/?#]+)$', url)
domain = match.group(1)
page = match.group(2)
print("Домен:", domain)
print("Имя страницы:", page)

# Задача 10: Генератор логина
full_name = "Maria Ivanova"
# Создайте логин в формате: m_ivanova
full_name = "Maria Ivanova"
login = full_name[0].lower() + "_" + full_name.split()[1].lower()
print(login)