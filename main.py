from driver.mail import mail
from driver.main import create_driver, login
import pandas as pd
import urllib.parse
import logging

driver = create_driver()

csv_name = 'test (1).csv'

data = pd.read_csv(csv_name)
login(driver)

if 'is_done' not in data.columns:
    data.insert(2, 'is_done', False)
    data.to_csv(csv_name, index=False)

not_done = data[data.is_done == False]
length = len(not_done)
for i, row in not_done.iterrows():
    print(f'\r {i} / {length + 1}', end='')
    try:
        seller_id = urllib.parse.parse_qs(row.URL).get('seller')[0]
        mail(driver, seller_id=seller_id, shop_name=row['店舗名'])
    except Exception as e:
        logging.error(''.join(e.args))
    else:
        not_done.loc[i, 'is_done'] = True

driver.close()
not_done.to_csv(csv_name, index=False)
