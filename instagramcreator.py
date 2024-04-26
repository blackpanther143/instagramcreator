from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import pandas as pd


def instacreater():
    options = Options()
    options.add_argument("-headless")
    driver1 = webdriver.Firefox(options=options)
    driver1.get("https://temp-mail.org/")
    WebDriverWait(driver1, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#tm-body > div.section-top-qr > div > div > div.col-xs-12.col-sm-12.col-md-12.col-lg-12.col-xl-6 > div.temp-emailbox > form > div.input-box-col.hidden-xs-sm > button"))
        ) 
    time.sleep(10)
    print("pranjal")
    
    copymail = driver1.find_elements(By.CSS_SELECTOR, "#tm-body > div.section-top-qr > div > div > div.col-xs-12.col-sm-12.col-md-12.col-lg-12.col-xl-6 > div.temp-emailbox > form > div.input-box-col.hidden-xs-sm > button")
    copymail[0].click()
    print(pyperclip.paste())
    clipboard_content = pyperclip.paste()
    a1 = clipboard_content.index("@")
    b1 = clipboard_content[:a1] + "_pdd"

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.instagram.com/accounts/emailsignup")
    time.sleep(5)

    mobile = driver.find_element(By.NAME, "emailOrPhone")
    name = driver.find_element(By.NAME, "fullName")
    username = driver.find_element(By.NAME, "username")
    passw = driver.find_element(By.NAME, "password")

    MN = pyperclip.paste()
    FN = b1
    USER = b1
    PASS = "password@12345"

    mobile.send_keys(MN)
    name.send_keys(FN)
    username.send_keys(USER)
    passw.send_keys(PASS)
    time.sleep(2)
    pran = driver.find_elements(
        By.CSS_SELECTOR, "div.x1xmf6yo:nth-child(1) > button:nth-child(1)"
    )

    print("pranjal")
    pran[0].click()
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[title="Month:"]'))
        )

        print("Page loaded successfully.")
    except Exception as e:
        print("Page load timeout:", e)
        username.clear()
        username.send_keys(USER + "964814")
        pran[0].click()

    time.sleep(5)
    select = driver.find_element(By.CSS_SELECTOR, '[title="Month:"]')
    select = Select(select)
    select.select_by_value("6")
    select = driver.find_element(By.CSS_SELECTOR, '[title="Day:"]')
    select = Select(select)
    select.select_by_value("15")

    select = driver.find_element(By.CSS_SELECTOR, '[title="Year:"]')
    select = Select(select)
    select.select_by_value("2001")

    prand = driver.find_elements(By.CSS_SELECTOR, "._acap")

    prand[0].click()

    # time.sleep(20)
    while True:
        verify = driver1.find_elements(By.CLASS_NAME, "viewLink")
        for element in verify:
            p= element.text
            print("Element text:", element.text)
            if "Instagram code" in element.text:
                verify1 = element.text
                break
        if "Instagram code" in p:
            break  

    print(verify1)
    textsss = verify1

    otp = ""
    for i in range(len(textsss)):
        if textsss[i : i + 6].isdigit():
            otp = textsss[i : i + 6]
            break

    print(otp)
    fillcode = driver.find_elements(By.CSS_SELECTOR, "._aaie")

    fillcode[0].send_keys(otp)
    finalsubmit = driver.find_elements(By.CSS_SELECTOR, ".x1lq5wgf")
    finalsubmit[0].click()

    while True:
        current_url = driver.current_url
        print(current_url)
        expected_url = "https://www.instagram.com/"
        if current_url == expected_url:
            print("Current URL matches the expected URL.")
            time.sleep(10)
            break
        else:
            print(current_url)
            continue

    data1 = {
    'user': "[]",
    'password': "[]",
    'name': "[]",
    'email': "[]" }

    data1['user']=[USER]
    data1["password"]=[PASS]
    data1["name"]=[FN]
    data1["email"]=[MN]
    print(data1)
    mains = pd.DataFrame(data1)
    existing_data = pd.read_excel('user.xlsx')   
    appended_data = pd.concat([existing_data, mains], ignore_index=True)
    appended_data.to_excel('user.xlsx', index=False)
    driver1.quit()
    driver.quit()


for i in range(5):
    instacreater()