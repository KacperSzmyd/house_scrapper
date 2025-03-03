from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class HouseDataManager:
    def __init__(self, price, area, ppm2, link):
        self.price = price
        self.area = area
        self.price_per_m2 = ppm2
        self.link = link

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def pass_to_form(self):
        self.driver.get("https://forms.gle/sBZUMHgz3piHQjpk9")
        self.driver.maximize_window()

        price_element = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        price_element.send_keys(self.price)

        area_element = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        area_element.send_keys(self.area)

        price_per_m2_element = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        price_per_m2_element.send_keys(self.price_per_m2)

        link_element = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        link_element.send_keys(self.link)

        submit_button = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span',
        )
        submit_button.click()

    def quit(self):
        self.driver.quit()
