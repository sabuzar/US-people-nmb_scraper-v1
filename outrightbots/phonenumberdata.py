import threading
from selenium import webdriver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
start_time = time.time()


def selenium_bot(bot_id,start_numb,end_numb):
    options = webdriver.ChromeOptions()
    options.binary_location = 'divers/chrome-win/chrome.exe'
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-logging')
    Agent = webdriver.Chrome(options=options)
    agent=webdriver.Chromium()

    data_file_phonenumb = pd.read_excel('inputfile/800k-FE-Xfers.xlsx')

    number_of_iteration_Phone_number = end_numb
    numberend=start_numb
    nmber_file = 1
    for index in range(numberend, number_of_iteration_Phone_number):
        file_name = 'outputfiles/data{}.csv'.format(nmber_file)

        number = data_file_phonenumb['Phone'][index]
        Agent.get('https://api1.uspeoplesearch.net/person/v1?x={}&pi=110.37.78.20'.format(number))

        try:
            data = WebDriverWait(Agent, 1).until(
                EC.presence_of_element_located((By.XPATH, '/html/ body/pre')))
            data_store = data.text
            appending_data = [
                [number, data_store]
            ]
            storing_file = open('outputfiles/data{}.csv'.format(nmber_file), 'a', newline="")
            writer = csv.writer(storing_file)
            writer.writerow(appending_data)
            storing_file.close()
        except:
            continue
data_file_phonenumb = pd.read_excel('inputfile/800k-FE-Xfers.xlsx')
num_bots = 20

# Create and start threads
threads = []
start=0
end=len(data_file_phonenumb)/num_bots
end=round(end)
zem=2
for i in range(num_bots):
    if i == zem:
        start=end
        end+=end
        zem=zem+1
    thread = threading.Thread(target=selenium_bot,args=(i+1,start,end))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

end_time = time.time()
runtime = end_time - start_time
print(f"Program runtime: {runtime:.5f} seconds")