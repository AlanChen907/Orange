import json
import unittest
import warnings
from datetime import date, timedelta

import requests

warnings.filterwarnings('ignore')


class TaskCase002(unittest.TestCase):
    url = 'https://www.hko.gov.hk/wxinfo/json/one_json_uc.xml'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_case_002(self):
        res = requests.get(self.url, headers=self.headers, verify=False)
        self.assertEqual(200, res.status_code)

        weather_forecast = json.loads(res.content).get('F9D').get('WeatherForecast')
        in_2_days = (date.today() + timedelta(days=2)).strftime('%Y%m%d')

        in_2_days_weather = list(
            filter(lambda item: item['ForecastDate'] == in_2_days, weather_forecast)
        )[0]

        max_rh = in_2_days_weather.get('ForecastMaxrh')
        min_rh = in_2_days_weather.get('ForecastMinrh')

        print('relative humidity is {}% - {}%'.format(min_rh, max_rh))


if __name__ == '__main__':
    unittest.main()
