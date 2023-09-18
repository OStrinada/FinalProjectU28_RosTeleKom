# Проверка номера телефона

numb10 = '+7950123456'  # 10 цифр
numb_inv11 = '+00000000000'  # 11 цифр
numb_inv12 = '812345678951'  # 12 цифр
numb_12 ='+375XXXXXXXXX'  # 12 цифр + буквы
numb_13 ='+0123456789013'  # 13 цифр
numb_12L ='+Аccidentally'  # 12 букв латиницей
simb_11 = '№;%:?*()_+!'  # 11 символов
numb_v11 = '89832559345'
numb_375 = '+375999999999'


# Проверка электронной почты

# НЕДОПУСТИМЫЕ ФРМАТЫ

mail_K = 'Абв@example.com'  # локальная часть на кириллице
mail_simb = '☺☻◘@example.com'  # локальная часть состоит из символов
mail_SS = '!#$%&*+-/=?^_`{|}~@example.com'  # локальная часть состоит только из спец.символов
mail_Ar = ' صسغذئآصسغذئ@example.com '  # локальная часть на арабском языке
mail_Ch = '龍門大酒家門大酒家酒家@example.com'  # локальная часть на китайском языке
mail_0 = '@example.com'  # локальная часть отсутствует
mail_dom0 = 'kik@.com'  # имя домена отсутствует
mail_B = 'kikexample.com'  # без спецсимвола @
mail_65lok = '14jYuZsGlJjYxOYdPTJ34huJgGgWuaYBpUbxEtxKEhGtXiuBkyCIufWQqTAbaXlA!@example.com' # 65 символов в локальной части
mail_dom256 = 'kik@104jYuZsGlJjYxOYdPTJebhuJgGgWuaYBpUbxEtxKEhGtXiuBkyCIufWQqTAbaXlAQzaZOEvvxRgGaMKTFLduRaouihOuXjxHqPXqbjzkjPSCYbtFaqiDBnzNcJymvCsPTAEWlFBofUqdhmSpOihjBumquPfqWXkmEUSvsXGQAVBwZZsSXsXQYnYPrCbCGoZRoJIBOgSRJpePQWGBlPCnrIlkOdYobRLcXFgbwxRmwySAvfHLiBVyhIudSNenbvy.com'

# ДОПУСТИМЫЕ ФОРМАТЫ

mail_dop = 'abc."defghi".xyz@example.com'  # email допустимого формата
mail_1bL = 'k@example.com'  # локальная часть сосооит из 1 буквы латиницей (допустимое значение)
mail_1numb = '1@example.com'  # локальная часть состоит из 1 цифры (допустимое значение)


# Варианты ввода пароля

Pass_7 = 'Normal7'  # Ввод пароля меньше 8 символов
Pass_21 = 'NormalPassword_21simb'  # Ввод пароля больше 20 символов
Pass_Kir = 'Passwordкириллицей'  # Использование в пароле "кириллицы"
Pass_bA_Z = 'normalpassword20simb'  # Пароль без заглавных букв
Pass_b0_9 = 'normalpasswordsimb'  # Пароль без цифр и/или спецсимволов
Pass_Valid = 'Normalpassword_simb'  # Валидный пароль
Pass_Valid2 = 'Normalpasswordsimb2'  # Пароль для проверки Подтверждения пароля


# Значения для тестирования полей имени

name_V = 'Иван'
name_V_t = 'Жан-Поль'
surname_V = 'Иванов'
surname_Vx2 = 'Петров-Водкин'
name_1L = 'A'  # a латинская
name_1K = 'А'  # кириллицей
number = '13'
simbols = '!@@@%:**!'  # символы
name_2L = 'AB'  # латинские
name_1K_2K = 'А-Бо'  # кириллицей
name_2K_3L = 'Aр-Boo'  # латинские
name_SPx2 = '  '  # два пробела
name_0 = ''  # пустое поле
name_2K = 'Ио'
name_30 = 'Ийцукенгшщзфывапролдячсмитьбюл'  #30 букв (кириллица)
name_31 = 'Айцукенгшщзхфывапролджэячсмитьб'  #31 буква (кириллица)
name_2d = 'Жан--Поль'  # Двойной дефис
name_smail = 'La☺☻•◘☺☻•◘1'  # смайлы
name_Ar = ' سغصسغذئآصسغذئآLa1'  # арабский язык
name_Ch = '龍門大酒家家家家'  # китайский язык
name_Korea = 'La테스트테스트테스트1'  # корейский язык




