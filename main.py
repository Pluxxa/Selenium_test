from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def main():
    try:
        que = input("Введите запрос: ")

        browser = webdriver.Firefox()
        browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

        search_box = browser.find_element(By.ID, "searchInput")
        search_box.send_keys(que)
        search_box.send_keys(Keys.RETURN)

        # Дождемся загрузки результатов поиска
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'mw-search-result-heading'))
        )

        # Находим первый результат поиска и переходим по ссылке
        search_results = browser.find_elements(By.CLASS_NAME, 'mw-search-result-heading')
        link1 = search_results[0].find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link1)

        while True:
            action = input("Что вы хотите делать?\n1 - ввести новый запрос\n2 - листать данную статью\n3 - перейти на случайную ссылку\n4 - выйти из программы\n")
            if action == '1':
                browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
                que = input("Введите запрос: ")
                search_box = browser.find_element(By.ID, "searchInput")
                search_box.send_keys(que)
                search_box.send_keys(Keys.RETURN)
                time.sleep(3)
                search_results = browser.find_elements(By.CLASS_NAME, 'mw-search-result-heading')
                link1 = search_results[0].find_element(By.TAG_NAME, "a").get_attribute("href")
                browser.get(link1)
            elif action == '2':
                paragraphs = browser.find_elements(By.TAG_NAME, "p")
                for paragraph in paragraphs:
                    print(paragraph.text)
                    input("Нажмите Enter для продолжения...")
            elif action == '3':
                # Собираем все ссылки на текущей странице
                links = browser.find_elements(By.TAG_NAME, "a")
                if links:
                    random_link = random.choice(links).get_attribute("href")
                    browser.get(random_link)
                else:
                    print("Нет доступных ссылок на текущей странице.")
            elif action == '4':
                break
            else:
                print("Введено неверное значение, попробуйте снова.")

    finally:
        browser.quit()
        print("Программа завершена.")

if __name__ == "__main__":
    main()
