#0

numbers = []
while True:
    user_numbers = int(input("Введите числа через пробел: "))
    elements = user_numbers.split()
    if '0' in elements:
        break
    try:
        filtered_numbers = [
            int(elem) for elem in elements 
            if int(elem) >= 0  
        ]
        else
        print("Обнаружено нецелое число или текст")
print("Итоговый список: ")
print(numbers)

#1

celsius = [0, 15, 25, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print("Температуры в Фаренгейтах:", fahrenheit)

grades = [45, 85, 92, 33, 67, 78, 90, 55, 29, 88]
passed = [grade for grade in grades if grade >= 60]
print("Проходные оценки (≥60):", passed)

#2
transactions = [100, -50, 200, -30, 150, -20, 300]
taxes = [transaction * 0.15 for transaction in transactions if transaction > 0]
print("Транзакции:", transactions)
print("Налоги (15% от доходов):", taxes)

#3
products = ['футболка', 'кружка', 'блокнот']
colors = ['красный', 'синий', 'зеленый']
combinations = [f"{product} - {color}" for product in products for color in colors]
print("Все возможные комбинации товаров и цветов:")
for combi in combinations:
    print(combi)
print(f"Всего комбинаций: {len(combinations)}")

#4
employees = [('Иван', 45), ('Мария', 92), ('Петр', 33), ('Анна', 67)]
status = [('Отлично'), ('Хорошо'), ('Требует улучшения')]
performance = [
    (name, percent, 
     "Отлично" if percent >= 90 
     else "Хорошо" if percent >= 60 
     else "Требует улучшения")
    for name, percent in employees]
print("Результаты:")
for name, percent, status in performance:
    print(f"{name}: {percent}% - {status}")

#5
sales = [
    {'name': 'Алексей', 'sales': 150, 'returns': 10},
    {'name': 'Ольга', 'sales': 200, 'returns': 5},
    {'name': 'Дмитрий', 'sales': 80, 'returns': 25},
    {'name': 'Елена', 'sales': 300, 'returns': 8}
]

top_managers = [
    manager['name']
    for manager in sales
    if (manager['sales'] - manager['returns'] >= 150) and 
       (manager['returns'] / manager['sales'] * 100 < 10)
]

print("Успешные менеджеры:")
for manager in top_managers:
    print(f"{manager}")
