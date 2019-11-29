from selenium import webdriver
from driver.conf import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mail.text import template
import logging


def wait_by_id(driver, _id):
    return WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, _id)))


def wait_by_ids(driver, *ids):
    for _id in ids:
        wait_by_id(driver, _id)


def create_driver():
    driver = webdriver.Chrome(r'C:\Users\yuuta\PycharmProjects\work\amazon_mail_20191106\chromedriver.exe')
    return driver


def login(driver):
    driver.get(
        'https://www.amazon.co.jp/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fgp%2Fhelp%2Fcustomer%2Fdisplay.html%3FnodeId%3D201889530%26ref_%3Dnav_signin&switch_account=')
    logging.info('ログインページへ移動中')
    wait_by_ids(driver, 'ap_email', 'continue')
    driver.find_element_by_id('ap_email').send_keys(mail)
    logging.info('パスワード入力画面へ移動中')
    driver.find_element_by_id('continue').click()
    wait_by_ids(driver, 'ap_password', 'signInSubmit')
    driver.find_element_by_id('ap_password').send_keys(pw)
    driver.find_element_by_id('signInSubmit').click()


def send_answer(driver, url, message):
    driver.get(url)
    wait_by_id(driver, 'seller-contact-button').click()

    # change tab
    driver.switch_to.window(driver.window_handles[1])

    # 選択
    wait_by_id(driver, 'a-autoid-0-announce').click()
    wait_by_id(driver, 'preOrderSubject_0').click()

    wait_by_id(driver, 'writeButton').click()

    wait_by_id(driver, 'comment').send_keys(message)

    wait_by_id(driver, 'a-autoid-2').click()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def main(driver, url, shop_name):
    send_answer(driver, url, template.format(shop_name=shop_name))
