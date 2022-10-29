from appium.webdriver.common.appiumby import By


class ElementPosition:
    skip_btn = (By.ID, 'hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip')
    close_btn = (By.XPATH, '//android.widget.ImageView[@content-desc="Close"]')
    menu_btn = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    nine_days_forecast = (By.XPATH, '//android.widget.LinearLayout[11]')
