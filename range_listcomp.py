#1

print(list(range(0,9)))
print(list(range(2,20)))
print (list(range(10, 1, -1)))

#2

words = ["apple", "banana", "cherry", "date", "fig", "grape"]
modified = ["FOUND" if "a" in word else word for word in words]
print(modified)

#3

products = ["Ноутбук", "Мышь", "Клавиатура", "Монитор"]
prices = [50000, 2500, 4000, 30000]
quantities = [8, 45, 25, 12]

total_for_each = [0,0,0,0]

for i in range(len(total_for_each)):
    total_for_each[i] = prices[i] * quantities[i]
    print(f"{products[i]}: {total_for_each[i]} руб.")
print(f"Товар с максимальной выручкой: {max(total_for_each)} руб.")

#4
products = ["Телефон", "Планшет", "Ноутбук", "Наушники"]
prices = [30000, 45000, 80000, 15000]
stock = [15, 8, 5, 20]
discounts = [10, 15, 20, 5]  # Скидки в процентах
reduced_prices = []
for i in range(len(products)):
    reduced = prices[i] - prices[i] / 100 * discounts[i]
    reduced_prices.append(reduced)
    
    print(f"Продукт: {products[i]}; Новая цена: {reduced}; Осталось: {stock[i]}")

#5
fruits = ["apple", "banana", "cherry"]
print("Фpукты в корзине:")
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}. {fruit}")

#6
num_list = [i for i in range(0, 21, 2)]
print(num_list)

#7
words = ["python", "data", "science", "list"]
words_len = [len(word) for word in words]
print(words_len)

#8
words = ["cat", "elephant", "dog", "butterfly", "ox"]
long_words = [word for word in words if len(word) > 4]
print(long_words)

#9
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
        print("Обнаружено нецелое число или текст. Продолжаем...")
print("Итоговый список: ")
print(numbers)