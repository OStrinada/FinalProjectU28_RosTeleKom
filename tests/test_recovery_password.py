import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import numb10, Kir_mail
from settings import numb_v, mail_v
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
def recovpage():

    time.sleep(2)

    pytest.driver.find_element(By.CSS_SELECTOR, "a#forgot_password").click()
    wait = WebDriverWait(pytest.driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
    # Проверяем, что мы оказались на странице восстановления пароля
    assert pytest.driver.find_element(By.XPATH, "//h1").text == "Восстановление пароля"

    print(Fore.GREEN + 'ВХОД НА СТРАНИЦУ ВОССТАНОВЛЕНИЯ ПАРОЛЯ ВЫПОЛНЕН УСПЕШНО' + Fore.RESET)

########################################################################################################################



class TestRecovPassWD:

    def test_recov_form(self, driver, recovpage):
        # Тестирование на содержание формы "Восставноелеение пароля"
        time.sleep(2)
        print(Fore.BLUE + 'Содержание формы "Восстановления пароля".' + Fore.RESET)
        vos_r = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right')
        for i in range(len(vos_r)):
            parts_vs = vos_r[i].text.split("\n")
            print('Форма содержит: ', parts_vs)

    def test_phone_number_field(self, driver, recovpage):

        print(Fore.BLUE + 'Сценарий ввода номера телефона на вкладке "Телефон" ' + Fore.RESET)

        # Ввод номера телефона из 10 цифр
        phone = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
        time.sleep(2)
        phone.send_keys(Keys.CONTROL + "A")
        phone.send_keys(Keys.BACKSPACE)
        phone.send_keys(numb10)
        phone.send_keys(Keys.TAB)
        errnV = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(errnV)):
            parts_errnV = errnV[i].text.split(", ")
            print('Сообщение об ошибке при вводе номера телефона без одной цифры: ', parts_errnV)

        # Ввод валидного зарегестрированного номера телефона
        phone = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
        time.sleep(2)
        phone.send_keys(Keys.CONTROL + "A")
        phone.send_keys(Keys.BACKSPACE)
        phone.send_keys(numb_v)
        phone.send_keys(Keys.TAB)
        errnV = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(errnV)):
            parts_errnV = errnV[i].text.split(", ")
            print('Сообщение об ошибке при вводе валидного номера телефона: ', parts_errnV)

    def test_email_field(self, driver, recovpage):

        print(Fore.BLUE + 'Сценарий ввода электронного адреса на вкладке "Почта"' + Fore.RESET)

        # Ввод email, записанного кирилицей
        pytest.driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
        mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
        time.sleep(2)
        mail.send_keys(Keys.CONTROL + "A")
        mail.send_keys(Keys.BACKSPACE)
        mail.send_keys(Kir_mail)
        mail.send_keys(Keys.TAB)
        erreV = pytest.driver.find_elements(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(erreV)):
            parts_erreV = erreV[i].text.split(", ")
            print('Сообщение об ошибке при вводе невалидного эл.адреса : ', parts_erreV)

        # Ввод валидного зарегестрированного email
        mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
        time.sleep(2)
        mail.send_keys(Keys.CONTROL + "A")
        mail.send_keys(Keys.BACKSPACE)
        mail.send_keys(mail_v)
        mail.send_keys(Keys.TAB)
        erreV = pytest.driver.find_elements(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > span')
        for i in range(len(erreV)):
            parts_erreV = erreV[i].text.split(", ")
            print('Сообщение об ошибке при вводе верного эл.адреса : ', parts_erreV)