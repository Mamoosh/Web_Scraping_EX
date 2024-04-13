import requests
from bs4 import BeautifulSoup


def find_label_by_element(url, xpath):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    css_selector = xpath.replace('/', ' > ').replace('html > body > ', '').replace(' > ', ' ').replace('[', ':nth-of-type(').replace(']', ')')

    element = soup.select_one(css_selector)
  
    if element:
        print(element.get_text())
    else:
        print("Element not found.")
    
if __name__ == '__main__':
    find_label_by_element('https://realpython.com/beautiful-soup-web-scraper-python/', '/html/body/div[1]/div/aside/div[4]/div[1]/p/a')
