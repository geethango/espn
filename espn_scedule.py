from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import numpy as np
import os
from selenium.webdriver.common.action_chains import ActionChains

DRIVER_PATH =r'C:\\Users\\geeth\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.espn.in/nhl/team/schedule/_/name/ana')

element_year = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div[1]/section/div/section/div[2]/div[1]/select[1]')
element_calendar = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div[1]/section/div/section/div[2]/button')
element_teams = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div[1]/section/div/section/div[1]/div/select[1]')


sel_year=Select(element_year)
#sel_calendar=Select(element_calendar)
sel_teams=Select(element_teams)

options_year=sel_year.options
options_teams=sel_teams.options


# for index3 in range(0,)
# d= driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div[1]/section/div/section/div[2]/button")
# d.click()

for index1 in range(0,len(options_teams)):
  team=options_teams[index1].text
  
  path='C:/Users/geeth/Desktop/new/'
  path = os.path.join(path,team)
  os.mkdir(path)

  for index2 in range(0,len(options_year)):
      
    year=options_year[index2].text
    # path1 = os.path.join(path,year)
    # os.mkdir(path1)
    
    all_tables=pd.read_html(driver.page_source)
    df=all_tables[0]
    df.to_csv('C:/Users/geeth/Desktop/new/'+team+'/'+year+'.csv')