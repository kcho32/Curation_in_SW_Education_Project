import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
driver = webdriver.Edge("msedgedriver.exe")

driver.get("https://www.udacity.com/courses/all")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

lecture = driver.find_elements_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li')

result = []


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_css_selector(xpath)
    except NoSuchElementException:
        return False
    return True


def main():
    for i in range(1, len(lecture)+1):
        print('{0}번'.format(i))
        list = []
        link = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a')
        title = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div:nth-child(1) > h2').text
        content = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div:nth-child(1) > p').text
        category = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div:nth-child(1) > h3').text
        level = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > ul > li:nth-child(1)').text
        period = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > ul > li:nth-child(2)').text
        list.append(link.get_attribute('href'))
        list.append(title)
        list.append(content)
        list.append(category)
        list.append(level)
        list.append(period)

        try:
            student = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > ul > li:nth-child(3) > div > small').text
            skill_covered = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div.card_overview__G6gIz > section:nth-child(1) > p').text
            pre_ready = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div.card_overview__G6gIz > section:nth-child(2) > p').text
            list.append(student)
            list.append(skill_covered)
            list.append(pre_ready)

        except NoSuchElementException as e: #검색결과 없을 시
            if not check_exists_by_xpath('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > ul > li:nth-child(3) > div > small'):
                list.append('None')
            else:
                student = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > ul > li:nth-child(3) > div > small').text
                list.append(student)

            if not check_exists_by_xpath('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div.card_overview__G6gIz > section:nth-child(1) > p'):
                list.append('None')
            else:
                skill_covered = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div.card_overview__G6gIz > section:nth-child(1) > p').text
                list.append(skill_covered)

            if not check_exists_by_xpath('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div.card_overview__G6gIz > section:nth-child(2) > p'):
                list.append('None')
            else:
                pre_ready = driver.find_element_by_css_selector('#__next > div > div > div.us_content__2MArY > div.catalog_catalogPage__1q6yU > div.catalog_catalogPageContent__3wM3J > main > div.catalog_catalogCards__3CNHp > ul > li:nth-child(' + str(i) + ') > a > article > div.card_body__1fi66 > div.card_overview__G6gIz > section:nth-child(2) > p').text
                list.append(pre_ready)

        finally:
            result.append(list)

    file = open('udacity.csv', 'w', encoding='windows-1252', newline='')
    csvfile = csv.writer(file)
    csvfile.writerow(['link', 'title', 'content', 'category', 'level', 'period', 'student', 'skill_covered', 'pre_ready'])
    for r in result:
        csvfile.writerow(r)
    file.close()


if __name__ == '__main__':
    main()
    driver.close()