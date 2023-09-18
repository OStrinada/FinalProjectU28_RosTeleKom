import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *
from data import *
from colorama import init, Fore

init(autoreset=True)

driver = webdriver.Chrome()
action = ActionChains(driver)

@pytest.fixture(autouse=True)
def driver():
    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(10)  # Все операции будут ждать 10 секунд
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=f499a934-9322-4f0a-a6e2-3cd054acca4a&theme&auth_type')

    yield driver

    pytest.driver.quit()

########################################################################################################################

@pytest.fixture(autouse=True)
def regpage():

    pytest.driver.find_element(By.ID, "kc-register").click()
    wait = WebDriverWait(pytest.driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
    # Проверяем, что мы оказались на странице регистрации нового пользователя
    assert pytest.driver.find_element(By.XPATH, "//h1").text == "Регистрация"

    print(Fore.GREEN + ' ВХОД НА СТРАНИЦУ РЕГИСТРАЦИИ ВЫПОЛНЕН УСПЕШНО')

    time.sleep(2)

########################################################################################################################


class TestRegForm:

    def test_regpage_form(self, driver, regpage):

        time.sleep(2)
        print(Fore.BLUE + ' Содержание страницы "Регистрация"\n' + Fore.RESET)

        reg_r = pytest.driver.find_elements(By.ID, 'page-right')
        for i in range(len(reg_r)):
            part_r = reg_r[i].text.split("\n")
            print('Содержание правой части: ', part_r)

        reg_l = pytest.driver.find_elements(By.ID, 'page-left')
        for i in range(len(reg_l)):
            part_l = reg_l[i].text.split("\n")
            print('Содержание лнвой части: ', part_l)

    def test_name_field(self, driver, regpage):

        print(Fore.BLUE + 'Тестирование поля "Имя" на ограничения. Негативные тесты: ' + Fore.RESET)

        reg_r = pytest.driver.find_elements(By.ID, 'page-right')

        # Данные имени = 1 буква латиницей
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_1L)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе 1 буквы на латинице: ', parts_err)

        # Данные имени = 1 буква кириллицей
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL+"A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_1K)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе 1 буквы на кириллице: ', parts_err)

        # Данные имени = число
        name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(number)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе числа: ', parts_err)

        # Данные имени = набор символов
        name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(simbols)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе символов: ', parts_err)

        # Данные имени = 2 буквы латиницей
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_2L)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе 2 букв на латинице: ', parts_err)

        # Данные имени = 1 буква кириллицей - 2 буквы кириллицей
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_1K_2K)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе А-Бо кириллицей: ', parts_err)

        # Данные имени = 2 буквы кириллицей - 3 буквы латиницей
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_2K_3L)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе Aр(кириллица)-Boo(латиница): ', parts_err)

        # Данные имени = двойной пробел
        name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_SPx2)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        if err in reg_r:
            for i in range(len(err)):
                parts_err = err[i].text.split(", ")
                print('Сообщение об ошибке при вводе двух пробелов: ', parts_err)
            else:
                print(Fore.RED + 'При вводе двух пробелов в поле "Имя" система не выдаёт ошибку' + Fore.RESET)

        # Данные имени = двойной дефис в имени
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_2d)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке, когда в имени стоит два дефиса: ', parts_err)

        # Данные имени = более 30 букв кириллицей
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_31)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе более 30 букв: ', parts_err)

        # Данные имени = пустое поле
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_0)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        if err in reg_r:
            for i in range(len(err)):
                parts_err = err[i].text.split(", ")
                print('Сообщение об ошибке, когда поле остаётся пустым: ', parts_err)
        else:
            print(Fore.RED + 'Если поле "Имя" оставить пустым, система не выдаст ошибку.' + Fore.RESET)

        # Данные имени = смайлы
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_smail)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе смайлов: ', parts_err)

        # Данные имени = ввод китайских символов
        name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_Ch)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR,'#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе китайских символов: ', parts_err)

        # Данные имени = ввод арабских символов
        name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_Ar)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR,'#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе арабских символов: ', parts_err)

        # Данные имени = ввод корейских букв
        name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_Korea)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе корейских букв: ', parts_err)

        ################################################################################################################
        print(Fore.BLUE + 'Тестирование поля "Имя". Позитивные тесты: ' + Fore.RESET)

        # Данные имени = имя из 2 букв кириллицей
        print('Тест 1. Ввод имени из 2 букв кириллицей.')
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        time.sleep(2)
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_2K)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

        # Данные имени = имя из 30 букв кириллицей
        print('Тест 2. Ввод имени из 30 букв кириллицей.')
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        time.sleep(2)
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_30)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

        # Данные имени = 2 < имя < 30 символов кириллицей без дефиса
        print('Тест 3. Ввод валидного имени кириллицей без дефиса.')
        name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
        time.sleep(2)
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_V)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

        print('Тест 4. Ввод валидного двойного имени кириллицей с использованием дефиса.')
        name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
        time.sleep(2)
        name.send_keys(Keys.CONTROL + "A")
        name.send_keys(Keys.BACKSPACE)
        name.send_keys(name_V_t)
        name.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

    def test_surname_field(self, driver, regpage):

        print(Fore.BLUE + 'Тестирование поля "Фамилия" на ограничения. Негативные тесты: ' + Fore.RESET)

        reg_r = pytest.driver.find_elements(By.ID, 'page-right')

        # Данные фамилии = корейские буквы
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_Korea)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе корейских букв: ', parts_err)

        # Данные фамилии = номер телефона
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                             'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(numb_inv12)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе номера телефона: ', parts_err)

        # Данные фамилии = 1 буква латиницей
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                                'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_1L)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе одной латинской буквы: ', parts_err)

        # Данные фамилии = 1 буква кириллицей
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                                 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_1K)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR,
                                              'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе одной буквы кириллицей: ', parts_err)

        # Данные фамилии = число
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(number)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе числа: ', parts_err)

        # Данные фамилии = набор символов
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(simbols)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе символов: ', parts_err)

        # Данные фамилии = 2 буквы латиницей
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_2L)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе двух букв латиницей: ', parts_err)

        # Данные фамилии = 1 буква кириллицей - 2 буквы кириллицей
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_1K_2K)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе А-Бо кириллицей: ', parts_err)

        # Данные фамилии = 2 буква кириллицей - 3 буквы латиницей
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_2K_3L)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе Aр(кириллица)-Boo(латиница): ', parts_err)

        # Данные фамилии = более 30 букв кириллицей
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_31)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе более 30 букв кириллицей: ', parts_err)

        # Данные фамилии = двойное имя кириллицей с двумя дефисами подряд
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_2d)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе двойного имени кириллицей с двумя дефисами: ', parts_err)

        # Данные фамилии = смайлы
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_smail)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе смайлов: ', parts_err)

        # Данные фамилии = арабские символы
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_Ar)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе арабских символов: ', parts_err)

        # Данные фамилии = китайские символы
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_Ch)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе китайских символов: ', parts_err)

        # Данные фамилии = двойной пробел
        surname = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_SPx2)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        if err in reg_r:
            for i in range(len(err)):
                parts_err = err[i].text.split(", ")
                print('Сообщение об ошибке при вводе двух пробелов: ', parts_err)
        else:
            print(Fore.RED + 'При вводе двух пробелов в поле "Фамилия" система не выдаёт ошибку' + Fore.RESET)

        # Данные фамилии = пустое поле
        surname = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_0)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        if err in reg_r:
            for i in range(len(err)):
                parts_err = err[i].text.split(", ")
                print('Сообщение об ошибке, если оставить поле пустым: ', parts_err)
        else:
            print(Fore.RED + 'Если поле "Фамилия" остается пустым, система не выдаёт ошибку' + Fore.RESET)

########################################################################################################################

        print(Fore.BLUE + '\nТестирование поля "Фамилия". Позитивные тесты: ' + Fore.RESET)

        # Данные фамилии = 2 буквы кириллицей
        print('Тест 1. Ввод имени из 2 букв кириллицей.')

        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_2K)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

        # Данные фамилии = 2 буквы кириллицей
        print('Тест 2. Ввод имени из 30 букв кириллицей.')
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(name_30)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

        # Данные фамилии = валидная фамилия кириллицей
        print('Тест 3. Ввод валидной фамилии без использования дефиса.')
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(surname_V)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

        # Данные фамилии = валидная двойная фамилия кириллицей
        print('Тест 4. Ввод валидной двойной фамилии с использованием дефиса.')
        surname = pytest.driver.find_element(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
        time.sleep(2)
        surname.send_keys(Keys.CONTROL + "A")
        surname.send_keys(Keys.BACKSPACE)
        surname.send_keys(surname_Vx2)
        surname.send_keys(Keys.TAB)
        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_err)

    def test_email_and_phone_data(self, driver, regpage):

        print(Fore.BLUE + 'Тестирование поля "E-mail или мобильный телефон" на ограничения. Негативные тесты. ' + Fore.RESET)

        reg_r = pytest.driver.find_elements(By.ID, 'page-right')

        print('\nПроверка ввода номера телефона: ')

        # Данные = 10 цифр номера телефона
        Adress = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        Adress.send_keys(numb10)
        Adress.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе 10 цифр номера телефона: ', parts_errm)

        # Данные = 11 цифр, не соответствующих номеру телефона
        Adress = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Adress.send_keys(Keys.CONTROL + "A")
        Adress.send_keys(Keys.BACKSPACE)
        Adress.send_keys(numb_inv11)
        Adress.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе 11 цифр, не соответсвующих номеру телефона: ', parts_errm)

        # Данные = 12 цифр, не соответствующих номеру телефона
        Adress = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Adress.send_keys(Keys.CONTROL + "A")
        Adress.send_keys(Keys.BACKSPACE)
        Adress.send_keys(numb_inv12)
        Adress.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе 12 цифр, не соответсвующих номеру телефона: ', parts_errm)

        # Данные = 13 цифр, не соответствующих номеру телефона
        Adress = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Adress.send_keys(Keys.CONTROL + "A")
        Adress.send_keys(Keys.BACKSPACE)
        Adress.send_keys(numb_13)
        Adress.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе 13 цифр, не соответсвующих номеру телефона: ', parts_errm)

        # Данные = 12 знаков (цифры + буквы)
        Adress = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Adress.send_keys(Keys.CONTROL + "A")
        Adress.send_keys(Keys.BACKSPACE)
        Adress.send_keys(numb_12)
        Adress.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе 12 знаков (буквы + цифры), не соответствующих номеру телефона: ', parts_errm)

        # Данные = 12 букв латиницей
        Adress = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Adress.send_keys(Keys.CONTROL + "A")
        Adress.send_keys(Keys.BACKSPACE)
        Adress.send_keys(numb_12L)
        Adress.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе 12 знаков (буквы + цифры), не соответствующих номеру телефона: ', parts_errm)

        # Данные = 11 символов
        Adress = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Adress.send_keys(Keys.CONTROL + "A")
        Adress.send_keys(Keys.BACKSPACE)
        Adress.send_keys(simb_11)
        Adress.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе 11 символов: ', parts_errm)

        print('\nПроверка ввода e-mail: ')

        # Данные = локальная часть на кириллице
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_K)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе локальной части email кириллицей', parts_errm)

        # Данные = локальная часть содержит смайлы
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_simb)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе локальной части email смайлами: ', parts_errm)

        # Данные = локальная часть состоит только из спец.символов
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_SS)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе локальной части email спец.символами: ', parts_errm)

        # Данные = локальная часть состоит из арабских символов
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_Ar)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе локальной части email арабскими символами: ', parts_errm)

        # Данные = локальная часть состоит из китайских символов
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_Ch)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при вводе локальной части email китайскими символами: ', parts_errm)

        # Данные = локальная часть отсутствует
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_0)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при отсаутствии локальной части email: ', parts_errm)

        # Данные = доменная часть отсутствует
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_dom0)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при отсутствии доменной части email: ', parts_errm)

        # Данные = в адресе email отсутствует знак @
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_dom0)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке при отсутствии знака @ в email: ', parts_errm)

        # Данные = имя доменной части состоит из более чем 255 символов
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_dom256)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        if errm in reg_r:
            for i in range(len(errm)):
                parts_errm = errm[i].text.split(", ")
                print('Сообщение об ошибке при вводе доменной части, состоящей из более чем 255 символов: ', parts_errm)
        else:
            print('Система не выдает ошибку, если доменное имя содержит более 255 символов.')

        # Данные = имя локальной части состоит из более чем 64 символов
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_65lok)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        if errm in reg_r:
            for i in range(len(errm)):
                parts_errm = errm[i].text.split(", ")
                print('Сообщение об ошибке при вводе имени локальной части, состоящем из более чем 64 символов: ',
                        parts_errm)
            else:
                print('Система не выдает ошибку, если локальное имя содержит более 64 символов.')

########################################################################################################################

        print(Fore.BLUE + 'Тестирование поля "E-mail или мобильный телефон". Позитивные тесты. ' + Fore.RESET)

        print('\nПРОВЕРКА ВВОДА НОМЕРА ТЕЛЕФОНА: ')

        # Данные = валидный номер телефона в формате 8ХХХХХХХХХХ
        print('Тест 1. Ввод номера телефона в формате 8ХХХХХХХХХХ')
        Phone = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Phone.send_keys(Keys.CONTROL + "A")
        Phone.send_keys(Keys.BACKSPACE)
        Phone.send_keys(numb_v11)
        Phone.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_errm)

        # Данные = валидный номер телефона в формате +7ХХХХХХХХХХ
        print('Тест 2. Ввод номера телефона в формате +7ХХХХХХХХХХ')
        Phone = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Phone.send_keys(Keys.CONTROL + "A")
        Phone.send_keys(Keys.BACKSPACE)
        Phone.send_keys(numb_v)
        Phone.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_errm)

        # Данные = валидный номер телефона в формате +375XXXXXXXXX
        print('Тест 3. Ввод номера телефона в формате +375XXXXXXXXX')
        Phone = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Phone.send_keys(Keys.CONTROL + "A")
        Phone.send_keys(Keys.BACKSPACE)
        Phone.send_keys(numb_375)
        Phone.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_errm)

        print('\nПРОВЕРКА ВВОДА ЭЛЕКТРОННОЙ ПОЧТЫ: ')

        # Данные = локальная часть сосооит из 1 буквы латиницей (допустимое значение)
        print('Тест 1. Локальная часть состоит из одной латинской буквы.')
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_1bL)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_errm)

        # Данные = локальная часть состоит из 1 цифры (допустимое значение)
        print('Тест 2. Локальная часть состоит из 1 цифры.')
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_1numb)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('Сообщение об ошибке: ', parts_errm)

        # Данные = email допустимого формата
        print('Тест 3. Допустимый формат email("abc."defghi".xyz@example.com") с использованием допустимой последовательности символов.')
        Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
        time.sleep(1)
        Mail.send_keys(Keys.CONTROL + "A")
        Mail.send_keys(Keys.BACKSPACE)
        Mail.send_keys(mail_dop)
        Mail.send_keys(Keys.TAB)
        errm = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')

        if errm in reg_r:
            for i in range(len(errm)):
                parts_errm = errm[i].text.split(", ")
                print('ТЕСТ ПРОЙДЕН', parts_errm)
        else:
            print('Система выдает ошибку при вводе допустимого формата email.')

########################################################################################################################

    def test_password_data(self, driver, regpage):

        print(Fore.BLUE + 'Тестирование поля "Пароль" на ограничения. Негативные тесты. ' + Fore.RESET)

        # Ввод пароля меньше 8 символов
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_7)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе пароля меньше 8 символов: ', partp_errp)

        # Ввод пароля больше 20 символов
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_21)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе пароля более 20 символов: ', partp_errp)

        # Использование в пароле "кириллицы"
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_Kir)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при использовании в пароле кириллицы: ', partp_errp)

        # Пароль без заглавных букв
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_bA_Z)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе пароля без заглавных букв: ', partp_errp)

        # Пароль без цифр и/или спецсимволов
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_b0_9)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе пароля без цифр и/или символов: ', partp_errp)

        # Ввод только спец.символов
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(simbols)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе пароля, состоящего только из спец.символов: ', partp_errp)

        # Ввод смайлов
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(name_smail)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе смайлов: ', partp_errp)

        # Ввод арабских символов
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(name_Ar)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе арабских символов: ', partp_errp)

        # Ввод корейских букв
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(name_Korea)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке при вводе корейских букв:: ', partp_errp)

 #######################################################################################################################

        print(Fore.BLUE + 'Тестирование поля "Пароль". Позитивные тесты. ' + Fore.RESET)

        # Ввод валидного пароля с использованием цифр без символов
        print('Тест 1. Ввод валидного пароля с использованием цифр без символов.')
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_Valid)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке: ', partp_errp)

        # Ввод валидного пароля с использованием символов без цифр
        print('Тест 2. Ввод валидного пароля с использованием символов без цифр.')
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_Valid2)
        Parol.send_keys(Keys.TAB)
        errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                           'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
        for i in range(len(errp)):
            partp_errp = errp[i].text.split(", ")
            print('Сообщение об ошибке: ', partp_errp)
########################################################################################################################

    def test_password_confirmation(self, driver, regpage):

        print(Fore.BLUE + 'Тестирование поля "Подтверждение пароля".' + Fore.RESET)

        # Ввод отличающихся значений пароля
        print('Тест 1. Значение в поле "Подтверждение пароля" отличается от значения в поле "Пароль".')
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_Valid)
        Parol.send_keys(Keys.TAB)
        NParol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password-confirm')
        time.sleep(1)
        NParol.send_keys(Keys.CONTROL + "A")
        NParol.send_keys(Keys.BACKSPACE)
        NParol.send_keys(Pass_Valid2)
        but_reg = pytest.driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > button")
        but_reg.click()
        errnp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                            'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > span')
        for i in range(len(errnp)):
            partp_errnp = errnp[i].text.split(", ")
            print('Сообщение об ошибке: ', partp_errnp)

        # Ввод идентичных паролей
        print('Тест 2. Значения паролей в полях "Пароль" и "Подтверждение пароля" идентичны.')
        Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
        time.sleep(1)
        Parol.send_keys(Keys.CONTROL + "A")
        Parol.send_keys(Keys.BACKSPACE)
        Parol.send_keys(Pass_Valid)
        Parol.send_keys(Keys.TAB)
        NParol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password-confirm')
        time.sleep(1)
        NParol.send_keys(Keys.CONTROL + "A")
        NParol.send_keys(Keys.BACKSPACE)
        NParol.send_keys(Pass_Valid)
        but_reg = pytest.driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > button")
        but_reg.click()
        errnp = pytest.driver.find_elements(By.CSS_SELECTOR,  'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > span')
        for i in range(len(errnp)):
            partp_errnp = errnp[i].text.split(", ")
            print('Сообщение об ошибке: ', partp_errnp)
