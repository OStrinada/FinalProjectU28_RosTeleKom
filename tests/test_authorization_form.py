import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Pass_20
from settings import numb_v, mail_v, Pass_v
from colorama import init, Fore, Style

init(autoreset=True)


driver = webdriver.Chrome()
action = ActionChains(driver)

########################################################################################################################
@pytest.fixture(autouse=True)
def driver():
    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(10)  # Все операции будут ждать 10 секунд
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=f499a934-9322-4f0a-a6e2-3cd054acca4a&theme&auth_type')

    yield

    pytest.driver.quit()

########################################################################################################################

class TestAuthForm:

        def test_authpage(self, driver):
            time.sleep(2)
            wait = WebDriverWait(pytest.driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
            # Проверяем, что мы оказались на главной странице пользователя
            assert pytest.driver.find_element(By.XPATH, "//h1").text == "Авторизация"

            print(Fore.GREEN + ' ВХОД НА САЙТ ВЫПОЛНЕН УСПЕШНО')


        def test_authpage_form(self, driver):

            print(Fore.BLUE + ' Содержание формы Авторизации\n' + Fore.RESET)

            # Проверка содержания формы "Авторизации"
            avt_r = pytest.driver.find_elements(By.ID, 'page-right')
            for i in range(len(avt_r)):
                part_r = avt_r[i].text.split('\n')
                print('Содержание правой части: ', part_r)

            avt_l = pytest.driver.find_elements(By.ID, 'page-left')
            for i in range(len(avt_l)):
                part_l = avt_l[i].text.split('\n')
                print('Содержание левой части: ', part_l)

        def test_auth_phone_number_form(self, driver):

            # Проверка авторизацию на вкладке "Телефон"
            print(Fore.BLUE + ' Авторизация клиента на вкладке "Телефон":' + Fore.RESET)

            print('\nПроверка при вводе значений в поле "Пароль":')
            print('\n1. Тест c использованием невалидного пароля.')

            # Ввод валидного номера телефона
            tpar = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
            time.sleep(1)
            tpar.send_keys(Keys.CONTROL + "A")
            tpar.send_keys(Keys.BACKSPACE)
            tpar.send_keys(numb_v)
            tpar.send_keys(Keys.TAB)

            # Вводим невалидный пароль
            Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
            time.sleep(1)
            Parol.send_keys(Keys.CONTROL + "A")
            Parol.send_keys(Keys.BACKSPACE)
            Parol.send_keys(Pass_20)
            but_autn = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
            but_autn.click()
            errp = pytest.driver.find_elements(By.CSS_SELECTOR, 'span#form-error-message')
            for i in range(len(errp)):
                partp_errp = errp[i].text.split(", ")
                print(Fore.RED + 'текст ошибки при вводе 20 латинских букв: ', partp_errp + Fore.RESET)  # Выводится сообщение об ошибке ввода неверного пароля/логина

            print('2. Тест c использованием валидного пароля.')
            # Ввод валидного номера телефона
            tpar = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
            time.sleep(1)
            tpar.send_keys(Keys.CONTROL + "A")
            tpar.send_keys(Keys.BACKSPACE)
            tpar.send_keys(numb_v)
            tpar.send_keys(Keys.TAB)

            # Ввод валидного пароля
            Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
            time.sleep(1)
            Parol.send_keys(Keys.CONTROL + "A")
            Parol.send_keys(Keys.BACKSPACE)
            Parol.send_keys(Pass_v)
            but_autn = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
            but_autn.click()
            errp = pytest.driver.find_elements(By.CSS_SELECTOR, 'span#form-error-message')
            for i in range(len(errp)):
                partp_errp = errp[i].text.split(", ")
                print(Fore.RED + 'текст ошибки при вводе неверного пароля: ', partp_errp + Fore.RESET)

        def test_auth_email_form(self, driver):
            # Проверка авторизации на вкладке "Почта"
            print(Fore.BLUE + ' Авторизация клиента на вкладке "Почта".\n' + Style.RESET_ALL)

            print('Проверка при вводе значений в поле "Пароль":')
            print('\n1. Тест с использованием невалидного пароля.')

            # Ввод валидного emal
            pytest.driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
            EM = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
            time.sleep(1)
            EM.send_keys(Keys.CONTROL + "A")
            EM.send_keys(Keys.BACKSPACE)
            EM.send_keys(mail_v)
            EM.send_keys(Keys.TAB)

            # Вводим невалидный пароль
            ParoEl = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
            time.sleep(1)
            ParoEl.send_keys(Keys.CONTROL + "A")
            ParoEl.send_keys(Keys.BACKSPACE)
            ParoEl.send_keys(Pass_20)
            but_autn_El = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
            but_autn_El.click()
            errel = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > span')
            for i in range(len(errel)):
                partp_errel = errel[i].text.split(", ")
                print(Fore.RED + 'текст ошибки при вводе 20 латинских букв: ', partp_errel + Fore.RESET)  # Сообщение при вводе невалидного пароля

            print('2. Тест с использованием валидного пароля.')
            # Ввод валидного emal
            pytest.driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
            EM = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
            time.sleep(1)
            EM.send_keys(Keys.CONTROL + "A")
            EM.send_keys(Keys.BACKSPACE)
            EM.send_keys(mail_v)
            EM.send_keys(Keys.TAB)

            # Ввод валидного пароля
            ParoEl = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
            time.sleep(1)
            ParoEl.send_keys(Keys.CONTROL + "A")
            ParoEl.send_keys(Keys.BACKSPACE)
            ParoEl.send_keys(Pass_v)
            but_autn_El = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
            but_autn_El.click()
            errel = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > span')
            for i in range(len(errel)):
                partp_errel = errel[i].text.split(", ")
                print('текст ошибки при вводе верного пароля:  ', partp_errel)  # Сообщение об ошибке при вводе невалидного логина/пароля