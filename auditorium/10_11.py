#1

score = 75
premium = False
if score >= 60 or premium:
    print("Доступ получен!")
else: print("Нет доступа")

#2

purchase, promocode = 6000, False
if purchase >= 5000 and promocode:
    print(f"Промокод активирован: {purchase*0.9}")

#3

password = "secure123"
if len(password) >=8 and any(char.isdigit () for char in password):
print "Пароль безопасен"

#4

score = 4.7
debts = False
scholarship = score >= 4.5 and debts == False

#5
comment = "Отличный пост! Спасибо за информацию."
banned_words = ["спам", "реклама", "вирус"]
has_banned_words = any(word in comment.lower() for word in banned_words)
print(f"Комментарий разрешен к публикации: {len(comment) <= 500 and not has_banned_words}")

#6 
message = "Мне нужно срочно отправить письмо клиенту"
if 'срочно' in message.lower() or len(message) > 50:
    print('high priority')
elif '?' in message:
    print('question')
else:
    print(len(message))

#7
budget, cuisine, vegetarian = "mid", "Italian", False
if budget == "low" and cuisine == "Italian":
    print("Рекомендую пиццерию")
elif vegetarian:
    print("Рекомендую вегетарианское кафе")
elif budget == 'high':
    print("Рекомендую премиум-ресторан")
else:
    print("Ищу другие варианты")

#8
temperature = 22
preference = 23
outside_t = 15
customer_at_home = True

if temperature < preference and customer_at_home:
    print("Turn on the heating")
elif temperature > 30:
    print("Turn on cooling")
elif customer_at_home == False:
    print("Energy saving modus")
else:
    print("Supporting current state")

#9

door_closed = True
window_closed = False
move_detection = True
night = True

if move_detection and night:
    print("Тревога")
elif not window_closed and night:
    print("Предупреждение")
elif door_closed and window_closed:
    print("Все в норме")
else:
    print("Стандартный режим")

#10
traffic_level = 8
distance_left = 35
time_left = 45
alternative = True

if traffic_level > 7 and alternative:
    print("Искать объезд")
elif distance_left < 10:
    print(time_left)
elif traffic_level > 5 and not alternative:
    print("Предупреждаю о пробках")
else:
    print("Продолжать по текущему маршруту")

#11
age = 20
subscription = True
if age >= 18:
    if subscription:
        print("Полный доступ")
    else:
        print("Только бесплатный контент")
else:
    print("Доступ ограничен")

order_done = True
print("Завершен" if order_done else "В обработке")

purchase, promocode = 6000, True
print("Скидка 15%" if purchase > 5000 and promocode else "Скидка 5%")

#12
email = "user@example.com"
email_type = "валидный" if any("@" for word in email) and any("." for word in email) else "невалидный"
print(email_type)
