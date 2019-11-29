from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mail.text import template


def mail(driver: WebDriver, seller_id, shop_name):
    driver.get(f'https://www.amazon.co.jp/hz/help/contact/{seller_id}/write?subject=2')
    comment_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'comment')))
    comment_field.send_keys(template.format(shop_name=shop_name))
    driver.find_element_by_name('sendEmail').click()
