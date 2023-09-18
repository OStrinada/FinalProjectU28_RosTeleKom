import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import numb_v
from data import Smb_mail
from colorama import init, Fore



init(autoreset=True)

driver = webdriver.Chrome()
action = ActionChains(driver)

########################################################################################################################

@pytest.fixture(autouse=True)
def driver():
    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(10)  # Все операции будут ждать 10 секунд
    # Переходим на страницу авторизации по временному коду
    pytest.driver.get('https://lk.rt.ru')

    yield

    pytest.driver.quit()

########################################################################################################################



class TestAuthForm:

    def test_authpage_form(self, driver):

        wait = WebDriverWait(pytest.driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        # Проверяем, что мы оказались на странице авторизации по коду
        assert pytest.driver.find_element(By.XPATH, "//h1").text == "Авторизация по коду"

        print(Fore.GREEN + '\nВХОД НА СТРАНИЦУ РЕГИСТРАЦИИ ВЫПОЛНЕН УСПЕШНО')

        time.sleep(2)

        print(Fore.BLUE + '\nСодержание страницы "Авторизация по коду"\n' + Fore.RESET)

        reg_r = pytest.driver.find_elements(By.ID, 'page-right')
        for i in range(len(reg_r)):
            part_r = reg_r[i].text.split("\n")
            print('Содержание правой части: ', part_r)

        reg_l = pytest.driver.find_elements(By.ID, 'page-left')
        for i in range(len(reg_l)):
            part_l = reg_l[i].text.split("\n")
            print('Содержание левой части: ', part_l)

    def test_auth_on_phone_numb(self, driver):

        print(Fore.BLUE + '\nТестирование поля "Email или мобильный телефон".\nПозитивный тест с валидным номером телефона.\n' + Fore.RESET)

        time.sleep(2)

        # Вводим валидный номер телефона
        pytest.driver.find_element(By.CSS_SELECTOR,
                                   'section#page-right > div > div > div > form > div > div > div > input').send_keys(
            numb_v)
        # Нажимаем кнопку "Получить код"
        pytest.driver.find_element(By.CSS_SELECTOR, 'button[name="otp_get_code"]').click()
        # Проверяем, что мы оказались на странице ввода кода
        assert pytest.driver.find_element(By.XPATH, "//h1").text == "Код подтверждения отправлен"

        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right>div>div>div>form>div>div>span')

        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе номера: ', parts_err)

    def test_auth_on_invalid_email(self, driver):

        print(Fore.BLUE + '\nТестирование поля "Email или мобильный телефон".\nНегативный тест с невалидной электронной почтой.\n' + Fore.RESET)

        time.sleep(2)

        # Вводим невалидный адрес email
        pytest.driver.find_element(By.CSS_SELECTOR,
                                   'section#page-right > div > div > div > form > div > div > div > input').send_keys(
            Smb_mail)
        # Нажимаем кнопку "Получить код"
        pytest.driver.find_element(By.CSS_SELECTOR, 'button[name="otp_get_code"]').click()

        err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right>div>div>div>form>div>div>span')
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('Сообщение об ошибке при вводе некорректного email: ', parts_err)

    def test_entrance_VK(self, driver):

        print(Fore.BLUE + '\nТестирование ссылки на соцсети на примере "ВКонтакте".' + Fore.RESET)

        time.sleep(2)
        # Нажимаем на сслыку "ВКонтакте"
        pytest.driver.find_element(By.ID, "oidc_vk").click()

        # Проверяем, что оказались на страницы авторизации через "ВКонтакте"
        if pytest.driver.find_element(By.XPATH, "//h1").text == "В сервис «РТК Паспорт» можно войти через VK ID":
            print('ВХОД НА ФОРМУ "Вход в VK ID" ВЫПОЛНЕН УСПЕШНО')
        else:
            print('ОШИБКА ВХОДА')

    def test_transition_on_authpage(self, driver):

        print(Fore.BLUE + '\nТестирование кнопки "Войти с паролем".' + Fore.RESET)

        time.sleep(2)
        # Нажимаем на кнопку "Войти с паролем"
        pytest.driver.find_element(By.XPATH, "//button[@id='standard_auth_btn']").click()
        # Проверяем, что оказались на странице "Авторизация"

        if pytest.driver.find_element(By.XPATH, "//h1").text == "Авторизация":
            print('ВХОД НА ФОРМУ "Авторизация" ВЫПОЛНЕН УСПЕШНО')
        else:
            print(Fore.RED + 'ОШИБКА ВХОДА' + Fore.RESET)








