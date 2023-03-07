from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import string

# Функция ожидания элементов
def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
    

def auth_user(user_name, user_email, current_address, permanent_address, driver):
    # Поиск и ожидание элементов и присваивание к переменным.
    input_username = wait_of_element_located(xpath='//*[@id=\"userName\"]', driver=driver)
    input_email = wait_of_element_located(xpath='//*[@id=\"userEmail\"]', driver=driver)
    input_user_current_address = wait_of_element_located(xpath='//*[@id=\"currentAddress\"]', driver=driver)
    input_permanent_address = wait_of_element_located(xpath='//*[@id=\"permanentAddress\"]', driver=driver)
    button_submit = wait_of_element_located(xpath='//*[@id=\"submit\"]', driver=driver)

    # Действия с формами
    input_username.send_keys(user_name)
    input_email.send_keys(user_email)
    input_user_current_address.send_keys(current_address)
    input_permanent_address.send_keys(permanent_address)
    button_submit.send_keys(Keys.RETURN)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

