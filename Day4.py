from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json

url="https://www.ptt.cc/bbs/joke/index.html"

if __name__ == '__main__':
    results = []
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(3)
    eles = driver.find_elements(By.CLASS_NAME, "r-ent")
    for ele in eles:
        title = ele.find_element(By.CLASS_NAME, "title").text
        href = ele.find_element(By.CLASS_NAME, "title").get_attribute("href")
        author = ele.find_element(By.CLASS_NAME, "author").text
        result = {
            'title': title,
            'href': href,
            'author': author
        }
        results.append(result)
    print(results)
    with open('ptt-articles.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, sort_keys=True, ensure_ascii=False)
    driver.quit()
