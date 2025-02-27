from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HouseScrapper:
    def __init__(self, localization):
        self.localization = localization

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_houses(self):
        self.driver.get("https://www.nieruchomosci-online.pl")
        self.driver.maximize_window()

        try:
            accept_cookies = self.driver.find_element(
                By.XPATH, value='//*[@id="ckInfoBox"]/div/div/ul/li[2]/span'
            )
            accept_cookies.click()
            sleep(1)
        except ElementNotInteractableException:
            print("Cookies already accepted")

        self.open_dropdown()
        self.choose_houses()
        self.fill_localization()

    def open_dropdown(self):
        open_dropdown = self.driver.find_element(
            By.XPATH, value='//*[@id="categoryAliasSingle"]'
        )
        open_dropdown.click()
        sleep(1)

    def choose_houses(self):
        choose_house = self.driver.find_element(
            By.XPATH, value='//*[@id="categoryAliasSingle"]/span[2]/span/span[3]'
        )
        choose_house.click()
        sleep(1)

    def fill_localization(self):
        type_localization = self.driver.find_element(By.ID, value="cityTip")
        type_localization.send_keys(self.localization)
        type_localization.send_keys(Keys.ENTER)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_filtered_houses_count(self) -> int:
        filtered_houses_counter = self.driver.find_element(By.ID, value="boxOfCounter")
        number_of_houses = filtered_houses_counter.text
        return int(number_of_houses.split()[0])

    def apply_filters(self, min_price=1000000, max_price=2000000):
        filter_menu = self.driver.find_element(
            By.XPATH, value='//*[@id="searchHandlePopup"]/div/div[4]/div/span[1]'
        )
        filter_menu.click()
        sleep(2)

        filter_minimum = self.driver.find_element(
            By.XPATH, value='//*[@id="pricefrom"]'
        )
        filter_minimum.send_keys(min_price)
        filter_minimum.send_keys(Keys.ENTER)
        sleep(0.5)

        filter_maximum = self.driver.find_element(By.XPATH, value='//*[@id="priceto"]')
        filter_maximum.send_keys(max_price)
        filter_minimum.send_keys(Keys.ENTER)
        sleep(0.5)

        submit_filters = self.driver.find_element(
            By.XPATH, value='//*[@id="search-action-popup-submit"]'
        )
        submit_filters.click()

    def get_house_tiles(self) -> dict:
        ignored_exceptions = (
            NoSuchElementException,
            StaleElementReferenceException,
        )
        house_counter = self.get_filtered_houses_count()
        houses_data = {}
        sleep(2)

        for x in range(1, house_counter + 1):
            tile = WebDriverWait(
                self.driver, 300, ignored_exceptions=ignored_exceptions
            ).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, f'//*[@id="tertiary-name_{x}"]')
                )
            )
            tile.click()
            sleep(2)
            houses_data[x] = self.get_house_data()

            exit_btn = self.driver.find_element(
                By.XPATH, value='//*[@id="top-layer-close"]/em'
            )
            exit_btn.click()

        return houses_data

    def get_house_data(self) -> dict:
        offer_url = self.get_current_url()
        house_price = self.driver.find_element(
            By.XPATH, value='//*[@id="bottomBox"]/p[2]/span[1]'
        ).text
        area = self.driver.find_element(
            By.XPATH, value='//*[@id="bottomBox"]/p[2]/span[2]'
        ).text
        price_per_m2 = self.driver.find_element(
            By.XPATH, value='//*[@id="bottomBox"]/p[2]/span[3]'
        ).text
        house_data = {
            "url": offer_url,
            "price": house_price,
            "area": area,
            "price per m2": price_per_m2,
        }
        return house_data
