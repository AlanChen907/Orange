import unittest

from appium import webdriver

from common_action import CommonAction
from element_position import ElementPosition


class BaseTest(unittest.TestCase):
    test_phone = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "FEC5T19B04001006",
        "appPackage": "hko.MyObservatory_v1_0",
        "appActivity": "hko.homepage.Homepage2Activity",
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", test_phone)

    @classmethod
    def setUpClass(cls) -> None:
        menu_present = CommonAction.is_element_present(
            cls.driver, ElementPosition.menu_btn)
        if not menu_present:
            CommonAction.skip_guide(cls.driver)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
