# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:27:32 2021

@author: ntesh
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://web3.ncaa.org/hsportal/exec/hsAction")

state_drop = driver.find_element_by_id("state")
state = Select(state_drop)
state.select_by_visible_text("New Jersey")

driver.find_element_by_id("city").send_keys("Galloway")
driver.find_element_by_id("name").send_keys("Absegami High School")
driver.find_element_by_class_name("forms_input_button").send_keys(Keys.RETURN)
driver.find_element_by_id("hsSelectRadio_1").click()

#scraping the caption of the tables
all_sub_head = driver.find_elements_by_class_name("tableSubHeaderForWsrDetail")
header = all_sub_head[1].text

#scraping all the headers of the tables
all_headers = driver.find_elements_by_class_name("tableHeaderForWsrDetail")

#filtering the desired headers
required_headers = all_headers[5:]


#scraoing all the table data
all_contents = driver.find_elements_by_class_name("tdTinyFontForWsrDetail")

#filtering the desired tabla data
required_contents = all_contents[45:]

keys = []
values = []
headers = []

headers.append(header)

for i in range(16):
    keys.append(required_headers[i].text)
    values.append(required_contents[i].text)
    
dictionary = dict(zip(keys, values))

df = pd.DataFrame.from_dict(dictionary , orient='index', columns = headers)

df.to_excel("output.xlsx")

print('EXCEL FILE GENERATED')
print('Execution Completed')