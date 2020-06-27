'''
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
5. Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
'''


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
# Формула для расчета
def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) # What is ln(abs(12*sin(x))), where x = ?

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока цена в поле price не станет равна 100
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")

        )
    # как только цена станет 100 Находим кнопку book
    input3 = browser.find_element_by_css_selector('#book')
    # Кликаем её
    input3.click()
    # Находим по id="input_value" значение которое присвоим x_element
    x_element = browser.find_element_by_css_selector('#input_value')
    # значение x_element присваивается иксу и производится расчет по формуле str(math.log(abs(12*math.sin(int(x)))))
    x = x_element.text
    # присваеваем производное формулы, переменной y
    y = calc(x)
    # Находим по id поле для ввода (в коде это: id="answer")
    input2 = browser.find_element_by_css_selector('#answer')
    # Заполняем поле значением "y" то которое мы получили по формуле
    input2.send_keys(y)
    # Находим кнопку отправить (Submit) и кликаем её
    input3 = browser.find_element_by_css_selector('#solve').click()

finally:

    # успеваем скопировать код за 20 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()