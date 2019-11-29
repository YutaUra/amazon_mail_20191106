from selenium import webdriver
from mail.text import template

mail = '<login email>'
pw = '<login password>'
driver = webdriver.Chrome(r'C:\Users\yuuta\PycharmProjects\work\amazon_mail_20191106\chromedriver.exe')

login_url = r'https://www.amazon.co.jp/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fgp%2Fhelp%2Fcustomer%2Fdisplay.html%3FnodeId%3D201889530%26ref_%3Dnav_signin&switch_account='

url = r'https://www.amazon.co.jp/sp?_encoding=UTF8&asin=&isAmazonFulfilled=1&isCBA=&marketplaceID=A1VC38T7YXB528&orderID=&seller=A2YDMU5FISBSPF&tab=&vasStoreID='

shop_name = 'あああ'
message = template.format(shop_name=shop_name)

# ログイン
driver.get(login_url)
driver.find_element_by_id('ap_email').send_keys(mail)
driver.find_element_by_id('continue').click()
driver.find_element_by_id('ap_password').send_keys(pw)
driver.find_element_by_id('signInSubmit').click()

# 移動
driver.get(url)

# 質問する
driver.find_element_by_id('seller-contact-button').click()

# タブの切り替え
driver.switch_to.window(driver.window_handles[1])

# お問い合わせ内容の選択
driver.find_element_by_id('a-autoid-0-announce').click()
driver.find_element_by_id('preOrderSubject_0').click()

# メッセージを入力ボタンのクリック
driver.find_element_by_id('writeButton').click()

# メッセージの入力
driver.find_element_by_id('comment').send_keys(message)

# メールの送信
driver.find_element_by_id('a-autoid-2').click()
