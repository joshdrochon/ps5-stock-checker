import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

# from pushover import Client

refresh_time = 300

amazon_link = "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_3?crid=2UMN3X88T2I8R&dchild=1&keywords=ps5+console&qid=1618549771&s=videogames&sprefix=ps5%2Cvideogames%2C253&sr=1-3"

# chromedriver needs to match chrome version ex. v89
PATH = '/Users/joshrochon/Downloads/chromedriver'


class Stocker:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(" - incognito")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
        self.timeout = 30

    def amazon(self, link):
        self.driver.get(link)
        time.sleep(1)

        try:
            avail = WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.presence_of_element_located((By.ID, 'availability'))
            ).text

            if 'In Stock' in avail:
                status = 'In Stock'
            else:
                status = 'Item unavailable'
        except:
            status = "Availability unknown"

        return status


def main():
    s = Stocker()

    while True:
        amazon_status = s.amazon(amazon_link)

        if amazon_status == 'In Stock':
            print('Do something amazing!')
        else:
            print(amazon_status)
        #check every 5 minutes
        time.sleep(refresh_time)


if __name__ == "__main__":
    main()
