from selenium.webdriver.common.by import By

from locators.inventory_locators import InventoryLocators


class InventoryPages:
    def __init__(self, driver):
        self.driver = driver

    def check_title(self):
        title = self.driver.find_element(By.XPATH, InventoryLocators.title_text).text
        return title

    def check_url(self):
        url = self.driver.current_url
        return url