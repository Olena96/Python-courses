# Задача 1
#
# Напишіть программу "Касир в кінотеватрі", яка попросить користувача ввести свій вік
# (можна використати константу або функцію input(), на екран має бути виведено лише одне повідомлення).
# - якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо від 16 до 65 то зробіть якесь вітальне повідомлення, на ваш розсуд.
# - якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
#
# age = int(input("Скільки тобі років?"))
#
# if age < 7:
#     print("Де твої батьки?")
# elif age < 16:
#     print("Це фільм для дорослих!")
# elif age <= 65:
#     print("Вітаю!")
# else:
#     print("Покажіть пенсійне посвідчення!")
# _______________________________
#
# Задача 2
#
# Текстова в чому різниця між is та ==?
#
# is перевіряє по ID, а == по значенню. Наприклад:
# num_1 = 897
# num_2 = 896 + 1
# print(id(num_1))
# print(id(num_2))
# print(num_1 is num_2) # буде True бо у 2х змінних однакові ID 1271082244400
# print(num_1 == num_2) # буде True бо у змінні мають однакове занчення 897
# _______________________________
#
# Задача 3
#
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат перемножений на три.
# якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.
#
# num_1 = input("Вкажіть число №1")
# num_2 = input("Вкажіть число №2")
# num_type = input("Вкажіть який у вас тип даних?")
#
# if num_type == "str":
#     print(3 * int(num_1 + num_2))
# elif num_type == "int":
#     print(3 * (int(num_1) + int(num_2)))
# else:
#     print("Це якийсь невідомий тип даних :)")
#
#
#