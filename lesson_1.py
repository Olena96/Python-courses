# 1 Арифметичні операції:
# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.

# num_one = float(input("Введіть число 1:"))
# num_two = float(input("Введіть число 2:"))
#
# result_sum = num_one + num_two
# result_difference = num_one - num_two
# result_multiplication = num_one * num_two
# result_fraction = num_one / num_two
#
# print(result_sum)
# print(result_difference)
# print(result_multiplication)
# print(result_fraction)
# _______________________________

# 2 Залишок від ділення:
# Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.

# num_one = float(input("Введіть число 1:"))
# num_two = float(input("Введіть число 2:"))
#
# division_remainder = num_one % num_two
# print("Залишок від відення ваших чисел:", division_remainder)
# _______________________________

# 3 Цілочисельне ділення:
# Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.

# num_one = float(input("Введіть число 1:"))
# num_two = float(input("Введіть число 2:"))

# division_no_remainder = int(num_one // num_two)
# print("Залишок від відення ваших чисел:", division_no_remainder)
# _______________________________

# 4 Перетворення стрічки у число:
# Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.

# str_into_int = int(input("введіть число"))
# print(type(str_into_int))
# _______________________________

# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.

# More code:
# num_one = input("Введіть число 1:")
# num_two = input("Введіть число 2:")
# concat = num_one + num_two
# print(concat)
#
# num_one_int = float(input("Введіть число 1:"))
# num_two_int = float(input("Введіть число 2:"))
# sum = num_one_int + num_two_int
# print(sum)

# Less code:
# num_one = input("Введіть число 1:")
# num_two = input("Введіть число 2:")
#
# concat = num_one + num_two
# sum = int(num_one) + int(num_two)
#
# print(concat)
# print(sum)
# _______________________________

# 6 Вік користувача:
# Запитати у користувача його рік народження, ім'я та який зараз рік (три змінні)
# та вивести на екран два прінти: ім'я та скільки років користувачу.

# name = input("Вкажіть ваше ім'я?")
# birth_year = int(input("Який у вас рік народження?"))
# year = int(input("Який зараз рік?"))
#
# users_age = year - birth_year
#
# print("Ваше ім'я:", name)
# print("Ваш вік:", users_age)
# _______________________________

# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.

# degrees_c = float(input("Скільки градусів по Цельсію?"))
# degrees_f = (degrees_c * 9/5) + 32
# print("По Фаренгейту це буде",degrees_f, "градусів")
# _______________________________

# 8 Перевод з фаренгейта в цельсій:
# Напишіть програму, яка запитує в користувача кількість градусів в фаренгейтах і повертає в цельсіях.
# Вам може здатися, що ця задача така ж, як попередня, але будьте уважні і перевірте результат вручну.

# degrees_f = float(input("Скільки градусів по Фаренгейту?"))
# degrees_с = (degrees_f - 32) * 5/9
# print("По Цельсію це буде",degrees_с, "градусів")
# _______________________________

# 9 Теорема Піфагора:
# Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)

# a = float(input("Скільки см один катет?"))
# c = a * (2**(1/2))
# print(c)
# _______________________________

# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.

# apples = int(input("Яка кількість яблук?"))
# students = int(input("Яка кількість учнів?"))
#
# qnt_p_student = apples // students
# apples_left = apples % students
#
# print("Кожний студент отримає",qnt_p_student, "яблук")
# print(apples_left,"залишиться в корзині")
# _______________________________

# 11 Магазин канцелярських товарів
# Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# Вхідні дані
# просимо користувача ввести три змінні
# кожне з яких не перевищує 109.
# Вихідні дані
# виведіть одне ціле число – вартість покупки в гривнях.
# приклад для перевірки програми 1
# ввів: 1 1 1
# отримав: 20

# pencils = int(input("Введіть к-сть олівці?"))
# pens = int(input("Введіть к-сть ручок?"))
# markers = int(input("Введіть к-сть фломастерів?"))
#
# if pencils > 109:
#     print("Кількість олівців перевищує 109. Введіть менше значення")
#     pencils = int(input("Введіть к-сть олівці?"))
#
# if pens > 109:
#     print("Кількість ручок перевищує 109. Введіть менше значення")
#     pens = int(input("Введіть к-сть олівці?"))
#
# if markers > 109:
#     print("Кількість маркерів перевищує 109. Введіть менше значення")
#     markers = int(input("Введіть к-сть олівці?"))
#
# total_cost = (pencils * 3) + (pens * 5) + (markers * 12)
# print("Сума, яку ви витратили на канцтовари:",total_cost,"грн")
# _______________________________

# 12 Циферблад
# Запитайте в користувача скільки хвилин пройшло з початку доби.
# Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# приклад для перевірки програми 1
# користувач ввів:150
# користувач отримує: 2, 30
# приклад для перевірки програми 2
# користувач ввів:1441
# користувач отримує: 0, 1

# qty_minutes = input("Скільки хвилин пройшло з початку доби?")
# hours = int(qty_minutes) // 60
# minutes = int(qty_minutes) % 60
#
# print(hours, "годин")
# print(minutes, "хвилин")
# _______________________________

# 13 Журавлики
# Петро, Катя та Сергій роблять з паперу журавликів. Разом вони зробили S журавликів.
# Скільки журавликів зробила кожна дитина, якщо відомо, що Петро та Сергій зробили однакову кількість журавликів,
# а Катя зробила в два рази більше журавликів, ніж Петро та Сергій разом.
# Вхідні дані
# Юзер вводить загальну кількість журавликів. Отримує три значення скільки зробив кожен (Петро, Катя та Сергій).
# У єдиному рядку вхідного файлу INPUT.TXT записано одне натуральне число S – загальна кількість зроблених журавликів (S < 106).

# total = int(input("Скільки журавликів всього?"))
#
# if total  > 106:
#     print("Кількість журавликів перевищує 106. Введіть менше значення")
#     total = int(input("Скільки журавликів всього?"))
#
# petro = total // 4
# serhii = petro
# katya = total // 2
#
# print("Кількість журавликів Петра:", petro)
# print("Кількість журавликів Каті:", katya)
# print("Кількість журавликів Сергія:", serhii)
# _______________________________

# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба податків сплатити. Не забудьте ЄСВ(4422)

# salary = float(input("Введіть зарплату:"))
# single_tax = float(input("Введіть процент податку:"))
# euv = 4422
#
# total_salary_per = (salary * (single_tax / 100)) + euv
# print(total_salary_per)