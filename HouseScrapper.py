from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HouseScrapper:
    def __init__(self, localization, min_price=1000000, max_price=2000000):
        self.localization = localization
        self.min_price = min_price
        self.max_price = max_price

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_houses(self):
        self.driver.get("https://www.nieruchomosci-online.pl")

        accept_cookies = self.driver.find_element(
            By.XPATH, value='//*[@id="ckInfoBox"]/div/div/ul/li[2]/span'
        )
        accept_cookies.click()
        sleep(2)

        self.open_dropdown()
        sleep(2)
        self.choose_houses()
        sleep(2)
        self.fill_localization()
        sleep(2)

    def open_dropdown(self):
        open_dropdown = self.driver.find_element(
            By.XPATH, value='//*[@id="categoryAliasSingle"]'
        )
        open_dropdown.click()

    def choose_houses(self):
        choose_house = self.driver.find_element(
            By.XPATH, value='//*[@id="categoryAliasSingle"]/span[2]/span/span[3]'
        )
        choose_house.click()

    def fill_localization(self):
        type_localization = self.driver.find_element(By.ID, value="cityTip")
        type_localization.send_keys(self.localization)
        type_localization.send_keys(Keys.ENTER)

    def get_current_url(self):
        return self.driver.current_url