from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
#import requests
import os
import time
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as req
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import schedule
import datetime

def job():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(3)

    url_login = "http://boxfresh.site/"
    browser.get(url_login)
    time.sleep(3)

    element = browser.find_element_by_css_selector("body > div > div > div > div.col-xs-12.custom-button > form > button")
    time.sleep(1)
    element.click()

    username = "*****@gmail.com"
    Pass = "*****"

    element = browser.find_element_by_css_selector("#username_or_email")
    element.clear()
    element.send_keys(username)

    element1 = browser.find_element_by_css_selector("#password")
    element1.clear()
    element1.send_keys(Pass)

    Signin = browser.find_element_by_css_selector("#allow")
    time.sleep(1)
    Signin.click()

    soup = BeautifulSoup(browser.page_source, features="html.parser")
    found = soup.find_all('a', class_="question-content")
    Found = [x.text for x in found]
    print(Found)
    Found_length = len(Found)
    found_df = pd.DataFrame({'質問':Found})
    #found_df.to_excel('sitsumonbako.xlsx', sheet_name='shitsumonbako')

    #ここからはスプレッドシートに出力していきます。

    #import sys, subprocess
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gspread','oauth2client'])

    scope = ['*****',
             '*****']


    credentials = ServiceAccountCredentials.from_json_keyfile_name('*****', scope)
    gc = gspread.authorize(credentials)
    workbook = gc.open('質問箱')
    wks = workbook.add_worksheet(title=str(datetime.datetime.now()), rows=100, cols=26)
    #wks = gc.open('質問箱').sheet1
    time.sleep(3)



    for i in range(int(Found_length)):
        index=i+1
        wks.update_acell('A'+str(index), Found[i])
        print(wks.acell('A'+str(index)))
        time.sleep(1)

    print("本日のスクレイピング完了")
    print("I'm working...")

    time.sleep(3)
    ws = workbook.get_worksheet(0)
    df = pd.DataFrame(ws.get_all_values())
    #df
    dfl = df[0]
    dfl = dfl.values.tolist()
    new_df = dfl + Found

    string = ",".join(new_df)
    string_new = string.replace('\n', '')
    str_list_new =  string_new.split(",")
    #print(string_new)
    df_new = string_new.split(',')
    outcome = list(dict.fromkeys(df_new))
    time.sleep(3)

    for i in range(int(len(outcome))):
        index=i+1
        ws.update_acell('A'+str(index), outcome[i])
        print(ws.acell('A'+str(index)))
        time.sleep(1)



    print('完了しました。')
    print(datetime.datetime.now())
    print("I'm working...")

def confirmation():
    print(datetime.datetime.now())
    print("I'm working...")

schedule.every().day.at("17:57").do(job)
schedule.every().hours.do(confirmation)

while True:
    schedule.run_pending()
    time.sleep(3)
