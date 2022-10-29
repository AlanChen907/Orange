import time

from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException

from element_position import ElementPosition


class CommonAction:

    @staticmethod
    def is_element_present(driver: WebDriver, element) -> bool:
        """
        Check the element present or not
        :param driver: the instance of appium driver
        :param element: element's position
        :return:
        """
        is_present = True
        try:
            driver.find_element(*element)
        except NoSuchElementException:
            is_present = False

        return is_present

    @classmethod
    def skip_guide(cls, driver: WebDriver) -> None:
        """
        Skip the beginner's guide
        :param driver: the instance of appium driver
        :return:
        """
        is_present = cls.is_element_present(driver, ElementPosition.skip_btn)
        while is_present:
            driver.find_element(*ElementPosition.skip_btn).click()
            time.sleep(0.5)
            is_present = cls.is_element_present(driver, ElementPosition.skip_btn)

        is_present = cls.is_element_present(driver, ElementPosition.close_btn)
        if is_present:
            driver.find_element(*ElementPosition.close_btn).click()
            time.sleep(0.5)
