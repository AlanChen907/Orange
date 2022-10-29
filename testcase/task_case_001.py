import time
import unittest

from element_position import ElementPosition
from testcase.base_test import BaseTest


class TaskCase001(BaseTest):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_case_001(self):
        self.driver.find_element(*ElementPosition.menu_btn).click()
        time.sleep(0.5)

        self.driver.find_element(*ElementPosition.nine_days_forecast).click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
